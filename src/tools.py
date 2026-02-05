from langchain.tools import tool
from .database import HospitalDB
from .rag_engine import MedicalRAGEngine

db = HospitalDB()
rag = MedicalRAGEngine()

@tool
def check_patient_history(name: str):
    """Retrieves patient identity and insurance details from the SQL database."""
    return db.get_patient_record(name)

@tool
def medical_research_tool(symptom: str):
    """Searches medical guidelines to determine symptom severity."""
    return rag.search(symptom)

@tool
def insurance_check_tool(plan_name: str):
    """Verifies if a specific insurance plan covers emergency or routine visits."""
    return rag.search(plan_name)

@tool
def emergency_booking_tool(patient_id: int):
    """Triggers an emergency booking request. Requires Human Approval input."""
    print(f"\n[HUMAN GATED ACTION]: Requesting ER slot for Patient {patient_id}.")
    approval = input("Admin, do you approve this booking? (y/n): ")
    if approval.lower() == 'y':
        return db.create_appointment(patient_id, "Emergency")
    return "Booking declined by Human Administrator."