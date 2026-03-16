# ============================================================
# 1_pydantic_basics.py - Pydantic Basics
# ============================================================
# Pydantic V2 use ho raha hai (pip install pydantic)
# Ye 3 steps mein kaam karta hai:
#   Step 1: Model (class) define karo - schema batao
#   Step 2: Raw data se object banao - validation auto hoti hai
#   Step 3: Validated object ko function mein use karo

from pydantic import BaseModel, Field
from typing import Annotated

# ============================================================
# PYDANTIC MODEL - Basics
# ============================================================
class Patient(BaseModel):
    name: Annotated[str, Field(
        max_length=50,
        description="Name of the patient",
        examples=["Nitish"]
    )]
    gender: str = 'Male'
    age: Annotated[int, Field(gt=0, lt=120, description="Patient ki age, 0 se 120 ke beech")]
    weight: Annotated[float, Field(
        gt=0, strict=True, description="Weight in kg"
    )]
    height: float
    married: Annotated[bool, Field(default=False, description="Is the patient married or not")]
    email: str

def insert_patient(patient: Patient):
    """Patient data ko database mein insert karta hai."""
    print(f"Name     : {patient.name}")
    print(f"Age      : {patient.age}")
    print(f"Weight   : {patient.weight} kg")
    print("Inserted into database!\n")

patient_info = {
    'name': 'nitish',
    'age': 25,
    'weight': 65.0,
    'height': 1.65,
    'married': False,
    'email': 'nitish@hdfc.com',
}

patient1 = Patient(**patient_info)
print("--- Insert Patient ---")
insert_patient(patient1)
