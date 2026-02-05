import sqlite3
import os

class HospitalDB:
    def __init__(self, db_path="hospital.db"):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        """Creates tables and mock data if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS patients 
                              (id INTEGER PRIMARY KEY, name TEXT, condition TEXT, insurance_plan TEXT)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS appointments 
                              (id INTEGER PRIMARY KEY, patient_id INTEGER, status TEXT, type TEXT)''')
            
            # Mock Data
            cursor.execute("INSERT OR IGNORE INTO patients VALUES (1, 'Gana', 'Post-Surgery Recovery', 'Premium-Plus')")
            conn.commit()

    def get_patient_record(self, name):
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute("SELECT * FROM patients WHERE name = ?", (name,)).fetchone()

    def create_appointment(self, patient_id, appt_type):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("INSERT INTO appointments (patient_id, status, type) VALUES (?, ?, ?)", 
                         (patient_id, "Pending Approval", appt_type))
            conn.commit()
            return f"Success: {appt_type} appointment logged in system."