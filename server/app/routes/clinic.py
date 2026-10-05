from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
import uuid
from datetime import date

from app.database import (
    overview_collection,
    patients_collection,
    appointments_collection,
    doctors_collection,
    invoices_collection,
    financial_reports_collection
)
from app.data.clinic_data import (
    CLINIC_OVERVIEW,
    CLINIC_PATIENTS,
    CLINIC_APPOINTMENTS,
    CLINIC_DOCTORS,
    CLINIC_INVOICES,
    MONTHLY_FINANCIAL_REPORT
)

router = APIRouter(prefix="/api")

def serialize_doc(doc: dict) -> dict:
    if not doc:
        return doc
    clean = dict(doc)
    clean.pop("_id", None)
    return clean

def to_camel_case_patient(p: dict) -> dict:
    return {
        "id": p.get("id", ""),
        "name": p.get("name", ""),
        "age": p.get("age", 0),
        "gender": p.get("gender", "Other"),
        "bloodGroup": p.get("blood_group", p.get("bloodGroup", "")),
        "blood_group": p.get("blood_group", p.get("bloodGroup", "")),
        "phone": p.get("phone", ""),
        "email": p.get("email", ""),
        "condition": p.get("condition", ""),
        "allergies": p.get("allergies", []),
        "chronicDiseases": p.get("chronic_diseases", p.get("chronicDiseases", [])),
        "chronic_diseases": p.get("chronic_diseases", p.get("chronicDiseases", [])),
        "lastVisit": p.get("last_visit", p.get("lastVisit", "")),
        "last_visit": p.get("last_visit", p.get("lastVisit", "")),
        "totalVisits": p.get("total_visits", p.get("totalVisits", 1)),
        "total_visits": p.get("total_visits", p.get("totalVisits", 1)),
        "insuranceProvider": p.get("insurance_provider", p.get("insuranceProvider", "None")),
        "insurance_provider": p.get("insurance_provider", p.get("insuranceProvider", "None")),
        "attendanceStatus": p.get("attendance_status", p.get("attendanceStatus", "regular")),
        "attendance_status": p.get("attendance_status", p.get("attendanceStatus", "regular")),
        "address": p.get("address", "")
    }

def to_camel_case_appointment(a: dict) -> dict:
    return {
        "id": a.get("id", ""),
        "token": a.get("token", "T-001"),
        "appointmentTime": a.get("appointment_time", a.get("appointmentTime", "")),
        "appointment_time": a.get("appointment_time", a.get("appointmentTime", "")),
        "date": a.get("date", ""),
        "patientId": a.get("patient_id", a.get("patientId", "")),
        "patient_id": a.get("patient_id", a.get("patientId", "")),
        "patientName": a.get("patient_name", a.get("patientName", "")),
        "patient_name": a.get("patient_name", a.get("patientName", "")),
        "phone": a.get("phone", ""),
        "doctorId": a.get("doctor_id", a.get("doctorId", "")),
        "doctor_id": a.get("doctor_id", a.get("doctorId", "")),
        "doctorName": a.get("doctor_name", a.get("doctorName", "")),
        "doctor_name": a.get("doctor_name", a.get("doctorName", "")),
        "department": a.get("department", ""),
        "specialty": a.get("department", a.get("specialty", "")),
        "room": a.get("room", "Suite 101"),
        "visitType": a.get("visit_type", a.get("visitType", "General Consultation")),
        "visit_type": a.get("visit_type", a.get("visitType", "General Consultation")),
        "status": a.get("status", "scheduled"),
        "completedTime": a.get("completed_time", a.get("completedTime")),
        "completed_time": a.get("completed_time", a.get("completedTime")),
        "diagnosis": a.get("diagnosis"),
        "fee": a.get("fee", 120),
        "billingStatus": a.get("billing_status", a.get("billingStatus", "unbilled")),
        "billing_status": a.get("billing_status", a.get("billingStatus", "unbilled")),
        "notes": a.get("notes"),
        "noShowReason": a.get("no_show_reason", a.get("noShowReason"))
    }

def to_camel_case_doctor(d: dict) -> dict:
    return {
        "id": d.get("id", ""),
        "name": d.get("name", ""),
        "specialty": d.get("specialty", ""),
        "room": d.get("room", ""),
        "status": d.get("status", "on_duty"),
        "avatar": d.get("avatar", "DR"),
        "patientsToday": d.get("patients_today", d.get("patientsToday", 0)),
        "patients_today": d.get("patients_today", d.get("patientsToday", 0)),
        "experience": d.get("experience", "5 years"),
        "phone": d.get("phone", "")
    }

def to_camel_case_invoice(inv: dict) -> dict:
    return {
        "id": inv.get("id", ""),
        "invoiceNumber": inv.get("invoice_number", inv.get("invoiceNumber", "")),
        "invoice_number": inv.get("invoice_number", inv.get("invoiceNumber", "")),
        "date": inv.get("date", ""),
        "patientId": inv.get("patient_id", inv.get("patientId", "")),
        "patient_id": inv.get("patient_id", inv.get("patientId", "")),
        "patientName": inv.get("patient_name", inv.get("patientName", "")),
        "patient_name": inv.get("patient_name", inv.get("patientName", "")),
        "doctorName": inv.get("doctor_name", inv.get("doctorName", "")),
        "doctor_name": inv.get("doctor_name", inv.get("doctorName", "")),
        "services": inv.get("services", []),
        "totalAmount": inv.get("total_amount", inv.get("totalAmount", 0)),
        "total_amount": inv.get("total_amount", inv.get("totalAmount", 0)),
        "status": inv.get("status", "paid"),
        "paymentMethod": inv.get("payment_method", inv.get("paymentMethod", "Credit Card")),
        "payment_method": inv.get("payment_method", inv.get("paymentMethod", "Credit Card"))
    }

# --- 1. OVERVIEW ---
@router.get("/overview")
async def get_overview():
    try:
        doc = await overview_collection.find_one({}, {"_id": 0})
        if not doc:
            doc = CLINIC_OVERVIEW
        return {"success": True, "data": doc}
    except Exception as e:
        print(f"[API] Error loading overview: {e}, using local data")
        return {"success": True, "data": CLINIC_OVERVIEW}


# --- 2. PATIENTS ---
@router.get("/patients")
async def get_patients():
    try:
        docs = await patients_collection.find({}, {"_id": 0}).to_list(length=200)
        if not docs:
            docs = CLINIC_PATIENTS
        mapped = [to_camel_case_patient(p) for p in docs]
        return {"success": True, "data": mapped}
    except Exception as e:
        print(f"[API] Error loading patients: {e}, using local data")
        mapped = [to_camel_case_patient(p) for p in CLINIC_PATIENTS]
        return {"success": True, "data": mapped}

class CreatePatientRequest(BaseModel):
    name: str
    age: int
    gender: str
    bloodGroup: Optional[str] = "O+"
    blood_group: Optional[str] = None
    phone: str
    email: str
    condition: str
    allergies: Optional[List[str]] = Field(default_factory=list)
    chronicDiseases: Optional[List[str]] = Field(default_factory=list)
    chronic_diseases: Optional[List[str]] = None
    address: Optional[str] = ""
    insuranceProvider: Optional[str] = "None"
    insurance_provider: Optional[str] = None

@router.post("/patients", status_code=status.HTTP_201_CREATED)
async def create_patient(payload: CreatePatientRequest):
    try:
        new_id = f"P-{uuid.uuid4().hex[:4].upper()}"
        today_str = date.today().isoformat()
        blood = payload.blood_group or payload.bloodGroup or "O+"
        chronic = payload.chronic_diseases or payload.chronicDiseases or []
        insurance = payload.insurance_provider or payload.insuranceProvider or "None"

        patient_doc = {
            "id": new_id,
            "name": payload.name,
            "age": payload.age,
            "gender": payload.gender,
            "blood_group": blood,
            "phone": payload.phone,
            "email": payload.email,
            "condition": payload.condition,
            "allergies": payload.allergies or [],
            "chronic_diseases": chronic,
            "last_visit": today_str,
            "total_visits": 1,
            "insurance_provider": insurance,
            "attendance_status": "new",
            "address": payload.address or ""
        }
        await patients_collection.insert_one(patient_doc)
        patient_doc.pop("_id", None)
        return {"success": True, "data": to_camel_case_patient(patient_doc)}
    except Exception as e:
        print(f"[API] Error creating patient: {e}")
        raise HTTPException(status_code=500, detail="Failed to create patient")


# --- 3. APPOINTMENTS ---
@router.get("/appointments")
async def get_appointments():
    try:
        docs = await appointments_collection.find({}, {"_id": 0}).to_list(length=300)
        if not docs:
            docs = CLINIC_APPOINTMENTS
        mapped = [to_camel_case_appointment(a) for a in docs]
        return {"success": True, "data": mapped}
    except Exception as e:
        print(f"[API] Error loading appointments: {e}, using local data")
        mapped = [to_camel_case_appointment(a) for a in CLINIC_APPOINTMENTS]
        return {"success": True, "data": mapped}

class CreateAppointmentRequest(BaseModel):
    patientName: str
    phone: Optional[str] = ""
    doctorId: str
    date: Optional[str] = "2026-08-29"
    appointmentTime: Optional[str] = "10:00 AM"
    visitType: Optional[str] = "General Consultation"
    fee: Optional[float] = 120.0
    notes: Optional[str] = ""

@router.post("/appointments", status_code=status.HTTP_201_CREATED)
async def create_appointment(payload: CreateAppointmentRequest):
    try:
        # Lookup doctor name
        doc = await doctors_collection.find_one({"id": payload.doctorId}, {"_id": 0})
        doctor_name = doc.get("name") if doc else "Dr. Sarah Jenkins"
        room = doc.get("room") if doc else "Suite 101"
        dept = doc.get("specialty") if doc else "General Medicine"

        count = await appointments_collection.count_documents({})
        token_num = 40 + count + 1
        new_apt = {
            "id": f"apt-{uuid.uuid4().hex[:6]}",
            "token": f"T-0{token_num}",
            "appointment_time": payload.appointmentTime or "10:00 AM",
            "date": payload.date or date.today().isoformat(),
            "patient_id": f"P-{uuid.uuid4().hex[:4].upper()}",
            "patient_name": payload.patientName,
            "phone": payload.phone or "",
            "doctor_id": payload.doctorId,
            "doctor_name": doctor_name,
            "department": dept,
            "room": room,
            "visit_type": payload.visitType or "General Consultation",
            "status": "scheduled",
            "fee": payload.fee or 120.0,
            "billing_status": "unbilled",
            "notes": payload.notes or ""
        }
        await appointments_collection.insert_one(new_apt)
        new_apt.pop("_id", None)
        return {"success": True, "data": to_camel_case_appointment(new_apt)}
    except Exception as e:
        print(f"[API] Error creating appointment: {e}")
        raise HTTPException(status_code=500, detail="Failed to create appointment")

class UpdateAppointmentStatusRequest(BaseModel):
    status: str

@router.patch("/appointments/{appointment_id}/status")
async def update_appointment_status(appointment_id: str, payload: UpdateAppointmentStatusRequest):
    try:
        res = await appointments_collection.update_one(
            {"id": appointment_id},
            {"$set": {"status": payload.status}}
        )
        if res.matched_count == 0:
            raise HTTPException(status_code=404, detail="Appointment not found")
        return {"success": True, "appointment_id": appointment_id, "status": payload.status}
    except HTTPException:
        raise
    except Exception as e:
        print(f"[API] Error updating appointment: {e}")
        raise HTTPException(status_code=500, detail="Failed to update appointment")


# --- 4. DOCTORS ---
@router.get("/doctors")
async def get_doctors():
    try:
        docs = await doctors_collection.find({}, {"_id": 0}).to_list(length=100)
        if not docs:
            docs = CLINIC_DOCTORS
        mapped = [to_camel_case_doctor(d) for d in docs]
        return {"success": True, "data": mapped}
    except Exception as e:
        print(f"[API] Error loading doctors: {e}")
        mapped = [to_camel_case_doctor(d) for d in CLINIC_DOCTORS]
        return {"success": True, "data": mapped}


# --- 5. INVOICES ---
@router.get("/invoices")
async def get_invoices():
    try:
        docs = await invoices_collection.find({}, {"_id": 0}).to_list(length=200)
        if not docs:
            docs = CLINIC_INVOICES
        mapped = [to_camel_case_invoice(inv) for inv in docs]
        return {"success": True, "data": mapped}
    except Exception as e:
        print(f"[API] Error loading invoices: {e}")
        mapped = [to_camel_case_invoice(inv) for inv in CLINIC_INVOICES]
        return {"success": True, "data": mapped}


# --- 6. REPORTS ---
@router.get("/reports")
async def get_reports():
    try:
        doc = await financial_reports_collection.find_one({}, {"_id": 0})
        if not doc:
            doc = MONTHLY_FINANCIAL_REPORT
        return {"success": True, "data": doc}
    except Exception as e:
        print(f"[API] Error loading reports: {e}")
        return {"success": True, "data": MONTHLY_FINANCIAL_REPORT}
