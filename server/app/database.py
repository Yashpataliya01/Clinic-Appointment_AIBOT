from pymongo import AsyncMongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()
mongodb_url = os.getenv("MONGODB_URL")

client = AsyncMongoClient(
    mongodb_url,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000
)
db = client["clinic_management"]

# Collection handles
overview_collection = db["overview"]
patients_collection = db["patients"]
appointments_collection = db["appointments"]
doctors_collection = db["doctors"]
invoices_collection = db["invoices"]
financial_reports_collection = db["financial_reports"]