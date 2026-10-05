import os
import asyncio
from typing import Any, Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from app.database import db
from app.data.clinic_data import (
    CLINIC_OVERVIEW, CLINIC_PATIENTS, CLINIC_APPOINTMENTS,
    CLINIC_DOCTORS, CLINIC_INVOICES, MONTHLY_FINANCIAL_REPORT
)
from app.schemas.databaseSchema import (
    ClinicOverview, Patient, Appointment, Doctor, Invoice, FinancialReport
)

load_dotenv()
groq_api_key = os.getenv("GROQ_API")

class DatabaseOperation(BaseModel):
    collection: Literal["overview", "patients", "appointments", "doctors", "invoices", "financial_reports"]
    operation: str = Field(default="find")
    filter: dict[str, Any] = Field(default_factory=dict)
    projection: dict[str, Any] | None = None

    @field_validator("collection", mode="before")
    @classmethod
    def normalize_collection(cls, v):
        if isinstance(v, str):
            clean = v.strip().lower()
            alias_map = {
                "patient": "patients",
                "appointment": "appointments",
                "doctor": "doctors",
                "invoice": "invoices",
                "financial_report": "financial_reports",
                "financialreport": "financial_reports",
                "financial_reports": "financial_reports",
                "financials": "financial_reports",
                "report": "financial_reports",
                "reports": "financial_reports",
            }
            return alias_map.get(clean, clean)
        return v

def query_local_dataset(collection_name: str, filter_dict: dict | None = None, projection: dict | None = None) -> list[dict]:
    mapping = {
        "patients": CLINIC_PATIENTS,
        "appointments": CLINIC_APPOINTMENTS,
        "doctors": CLINIC_DOCTORS,
        "invoices": CLINIC_INVOICES,
        "financial_reports": [MONTHLY_FINANCIAL_REPORT],
        "overview": [CLINIC_OVERVIEW]
    }
    data = mapping.get(collection_name, [])
    if not filter_dict:
        return list(data)
    
    results = []
    for item in data:
        match = True
        for k, v in filter_dict.items():
            if k not in item:
                match = False
                break
            if isinstance(v, dict) and "$in" in v:
                if item[k] not in v["$in"]:
                    match = False
                    break
            elif item[k] != v:
                match = False
                break
        if match:
            results.append(item)
    return results

async def Database_query(question: str):
    print("this is the question", question)

    # Initialize Groq with active model
    model = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.1,
        api_key=groq_api_key
    )

    # Native structured output in json_mode for Groq compatibility
    structured_model = model.with_structured_output(DatabaseOperation, method="json_mode")

    today = "2026-08-29"

    prompt = PromptTemplate.from_template("""
You are Clini, the expert AI operations assistant for PulseClinic Healthcare Center.
Active clinic operating date: {today} (Saturday, August 29, 2026)
Active Financial & Operational Period: August 2026

Database Collections & Schemas:
OVERVIEW: {overview_schema}
PATIENTS: {patient_schema}
APPOINTMENTS: {appointment_schema}
DOCTORS: {doctor_schema}
INVOICES: {invoice_schema}
FINANCIAL REPORTS: {financial_report_schema}

Guidelines for queries:
1. When asked about doctors on duty or how many doctors are on duty ("how many doctors are on duty", "which doctors are working", "doctors on duty right now"), query the "doctors" collection with {{"status": "on_duty"}}, or query "overview" collection for stats. There are 14 doctors currently on duty (out of 18 total doctors: 14 on_duty, 2 on break, 2 off duty).
2. When asked about appointments today ("how many appointments today", "today's appointments"), query "overview" collection with {{}} (overview stats has 42 today_appointments: 34 completed, 8 upcoming/active), or query "appointments" with {{"date": "{today}"}}.
3. When asked about no-show patients ("who didn't show up", "didn't show up on time", "no-shows"), query "patients" with {{"attendance_status": "no-show"}}. There are 4 no-show patients: Brenda Diaz, Mark Spencer, Angela Martin, Kevin Malone.
4. When asked about monthly revenue, earnings, or financial reports ("monthly earnings", "gross revenue", "collected revenue"), query "financial_reports" or "overview" with {{}} to get the summary figures ($32,450 gross, $29,240 collected, $3,210 pending).
5. Always use "find" as the operation.

Understand the user's question and map it to a MongoDB database operation.
Respond ONLY with a valid JSON object conforming to the schema with keys: collection, operation, filter, projection.

User question: {question}
JSON Output:
""")

    chain = prompt | structured_model

    operation = chain.invoke({
        "overview_schema": ClinicOverview.model_json_schema(),
        "patient_schema": Patient.model_json_schema(),
        "appointment_schema": Appointment.model_json_schema(),
        "doctor_schema": Doctor.model_json_schema(),
        "invoice_schema": Invoice.model_json_schema(),
        "financial_report_schema": FinancialReport.model_json_schema(),
        "question": question,
        "today": today
    })

    print("\nAI DATABASE OPERATION:", operation)

    # Database fetching logic
    documents = []
    try:
        collection = db[operation.collection]
        cursor = collection.find(operation.filter, operation.projection)
        async for document in cursor:
            if "_id" in document:
                document["_id"] = str(document["_id"])
            documents.append(document)
        print(f"\nDATABASE RESULT ({len(documents)} records fetched from MongoDB):")
    except Exception as db_err:
        print(f"\n[Database Notice] MongoDB query failed: {db_err}. Falling back to local dataset...")
        documents = query_local_dataset(operation.collection, operation.filter, operation.projection)
        print(f"\nLOCAL DATASET RESULT ({len(documents)} records found):")

    # Final Answer Generation
    prompt_finalanswer = PromptTemplate.from_template("""
        You are Clini, the AI assistant for PulseClinic Healthcare Center.
        Convert the database result into a clear, natural, and helpful answer.

        User Question: {question}
        Database Result: {documents}

        Rules:
        1. Answer using the database result accurately.
        2. Keep it clear, concise, and easy to read.
    """)

    final_chain = prompt_finalanswer | model
    try:
        final_answer = final_chain.invoke({
            "question": question,
            "documents": documents
        })
        return final_answer.content
    except Exception as llm_err:
        print("LLM final answer error:", llm_err)
        return f"Found {len(documents)} records matching your query."