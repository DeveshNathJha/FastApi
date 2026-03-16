# ============================================================
# 2_nested_fields.py - Nested Models
# ============================================================
from pydantic import BaseModel, Field
from typing import Annotated

# --- NESTED MODEL: Address ---
class Address(BaseModel):
    city: str
    state: str
    pincode: Annotated[int, Field(gt=100000, lt=999999)]  # 6 digit pincode validation

class Patient(BaseModel):
    name: str
    age: int
    # --- address: nested model ---
    address: Address

patient_info = {
    'name': 'nitish',
    'age': 25,
    'address': {                    # Nested dictionary - Pydantic auto-convert karega
        'city': 'Gurgaon',
        'state': 'Haryana',
        'pincode': 122001
    }
}

patient1 = Patient(**patient_info)
print("--- Patient with Nested Address ---")
print(patient1.model_dump())
