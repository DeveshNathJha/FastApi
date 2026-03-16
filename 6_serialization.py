# ============================================================
# 6_serialization.py - Data Serialization & Filtering
# ============================================================
# Pydantic object ko serialize karna (dictionary, json string)
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str = 'Male'
    email: str
    address: Address

patient_info = {
    'name': 'nitish',
    'age': 25,
    'email': 'nitish@hdfc.com',
    'address': {
        'city': 'Gurgaon',
        'state': 'Haryana'
    }
}

patient1 = Patient(**patient_info)

# ============================================================
# EXPORTING DATA - model_dump()
# ============================================================
# Pydantic object ko wapas dictionary mein convert karna
print("--- Exporting to Dictionary ---")
patient_dict = patient1.model_dump()
print(f"Data Type : {type(patient_dict)}")
print(f"Full Dict : {patient_dict}\n")

# Pydantic object ko json string mein convert karna
print("--- Exporting to JSON String ---")
patient_json = patient1.model_dump_json()
print(f"Data Type : {type(patient_json)}")
print(f"Full JSON : {patient_json}\n")

print("--- Data Filtering Exports ---")
# Sirf name chahiye
print(f"Include (Name only): {patient1.model_dump(include={'name'})}")

# Name aur age hatake baaki sab chahiye
print(f"Exclude (Name, Age): {patient1.model_dump(exclude={'name', 'age'})}")

# Nested Address se state exclude karna
print(f"Exclude Nested (State): {patient1.model_dump(exclude={'address': {'state'}})}")

# Jo explicitly set nahi hue unhe hatao (e.g. default gender)
# humne create karte time gender pass nahi kiya tha, to wo hide ho jayega
print(f"Exclude Unset: {patient1.model_dump(exclude_unset=True)}")
