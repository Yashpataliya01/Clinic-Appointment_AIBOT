from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class ClinicOverview(BaseModel):
    name: str = "PulseClinic Healthcare Center"
    tagline: str = "Advanced Multi-Specialty Outpatient Clinic"
    address: str = "450 Medical Plaza Blvd, Suite 100, New York, NY 10016"
    phone: str = "+1 (800) 555-PULSE"
    email: str = "contact@pulseclinic.health"
    current_month: str = "August 2026"
    today_date: str = "Saturday, August 29, 2026"
    stats: Dict[str, Any] = Field(
        default_factory=lambda: {
            "total_patients": 1284,
            "monthly_revenue": 32450,
            "target_revenue": 35000,
            "today_appointments": 42,
            "today_completed": 28,
            "today_waiting": 5,
            "today_in_consult": 2,
            "today_scheduled": 7,
            "doctors_on_duty": 14,
            "total_doctors": 18,
            "pending_lab_reports": 9,
            "no_show_rate_percent": 4.2,
        }
    )

class Patient(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    blood_group: str
    phone: str
    email: str
    condition: str
    allergies: List[str] = Field(default_factory=list)
    chronic_diseases: List[str] = Field(default_factory=list)
    last_visit: str
    total_visits: int = 1
    insurance_provider: str = "None"
    attendance_status: str = "regular"
    address: str = ""

class Appointment(BaseModel):
    id: str
    token: str = "T-001"
    appointment_time: str
    date: str
    patient_id: str
    patient_name: str
    phone: str = ""
    doctor_id: str
    doctor_name: str
    department: Optional[str] = None
    room: Optional[str] = None
    visit_type: Optional[str] = "General Consultation"
    status: str = "scheduled"
    completed_time: Optional[str] = None
    diagnosis: Optional[str] = None
    fee: float = 120.0
    billing_status: str = "unbilled"

class Doctor(BaseModel):
    id: str
    name: str
    specialty: str
    room: str = "Suite 101"
    status: str = "on_duty"
    avatar: str = "DR"
    patients_today: int = 0
    experience: str = "5 years"
    phone: str = ""

class Invoice(BaseModel):
    id: str
    invoice_number: str
    date: str
    patient_id: str
    patient_name: str
    doctor_name: str
    services: List[Dict[str, Any]] = Field(default_factory=list)
    total_amount: float
    status: str = "paid"
    payment_method: Optional[str] = "Credit Card"

class FinancialReport(BaseModel):
    clinic_name: str = "PulseClinic Healthcare Center"
    period: str = "August 2026 (Month-to-Date)"
    generated_on: str = "2026-08-29"
    currency: str = "USD ($)"
    summary: Dict[str, Any] = Field(
        default_factory=lambda: {
            "gross_revenue": 32450,
            "total_consultations": 248,
            "average_ticket": 130.85,
            "paid_amount": 29240,
            "pending_receivables": 3210,
            "collection_rate_percent": 90.1,
        }
    )
    breakdown_by_category: List[Dict[str, Any]] = Field(default_factory=list)
    breakdown_by_doctor: List[Dict[str, Any]] = Field(default_factory=list)
    payment_methods: List[Dict[str, Any]] = Field(default_factory=list)