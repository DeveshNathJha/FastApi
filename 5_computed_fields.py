# ============================================================
# 5_computed_fields.py - Computed Fields
# ============================================================
from pydantic import BaseModel, computed_field

class Patient(BaseModel):
    name: str
    weight: float
    height: float

    # ============================================================
    # COMPUTED FIELDS - Dynamic Calculation
    # ============================================================
    # computed_field = aisi field jo baki fields se calculate hoti hai
    # Example: BMI (Body Mass Index) from weight and height

    @computed_field
    @property
    def bmi(self) -> float:
        # formula: weight / (height ** 2)
        result = self.weight / (self.height ** 2)
        return round(result, 2)

patient_info = {
    'name': 'nitish',
    'weight': 65.0,
    'height': 1.65
}

patient1 = Patient(**patient_info)
print("--- Patient with Computed Fields ---")
print(f"Weight: {patient1.weight} kg")
print(f"Height: {patient1.height} m")
print(f"BMI (Computed): {patient1.bmi}")
