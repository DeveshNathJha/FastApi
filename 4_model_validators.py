# ============================================================
# 4_model_validators.py - Model Validators
# ============================================================
from pydantic import BaseModel, model_validator

class Patient(BaseModel):
    name: str
    age: int
    contacts: dict[str, str] = {}

    # ============================================================
    # MODEL VALIDATORS - Multi-field Validation
    # ============================================================
    # model_validator = jab validation multiple fields pe depend kare
    # Example: Agar age > 60, toh emergency contact zaroori hai

    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls, model):
        # 'model' parameter mein pura object (Patient) milta hai
        if model.age > 60 and 'emergency' not in model.contacts:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model

# --- Correct data ---
patient_info_valid = {
    'name': 'Mohan',
    'age': 65,
    'contacts': {'emergency': '9876543210'}
}

patient1 = Patient(**patient_info_valid)
print("--- Patient with Model Validators ---")
print("Valid Patient created successfully:")
print(patient1.model_dump())
