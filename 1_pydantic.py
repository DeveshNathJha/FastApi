# ============================================================
# 1_pydantic.py — Pydantic Basics, Field Validator, Model Validator, Computed Fields
# ============================================================
# Pydantic V2 use ho raha hai (pip install pydantic)
# Ye 3 steps mein kaam karta hai:
#   Step 1: Model (class) define karo — schema batao
#   Step 2: Raw data se object banao — validation auto hoti hai
#   Step 3: Validated object ko function mein use karo

from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
# EmailStr bhi available hai (pip install pydantic[email]) — email validation ke liye
from typing import Annotated

# ============================================================
# PYDANTIC MODEL — with Field Validators
# ============================================================
# BaseModel inherit → class Pydantic model ban jaati hai
# Fields mein type + constraints + metadata sab define karo
# @field_validator se custom business logic lagao

class Patient(BaseModel):
    # --- name: required, max 50 chars, hamesha UPPERCASE store hoga ---
    name: Annotated[str, Field(
        max_length=50,
        title="Patient Name",
        description="Patient ka full name, 50 chars max. Auto-uppercase hota hai.",
        examples=["Nitish", "Amit"]
    )]

    # --- age: required, 0 < age < 120 ---
    age: Annotated[int, Field(
        gt=0,
        lt=120,
        description="Patient ki age, 0 se 120 ke beech"
    )]

    # --- weight: strictly float only ---
    weight: Annotated[float, Field(
        gt=0,
        strict=True,       # "75.2" string REJECT — sirf float chalega
        description="Weight in kg"
    )]

    height: float           # simple field — bas float type chahiye

    married: Annotated[bool, Field(
        default=False,      # optional — na bhejo toh False rahega
        description="Is the patient married or not"
    )]

    # --- email: required, hdfc.com ya icici.com domain chahiye ---
    email: str

    # --- contacts: dict containing contact details ---
    contacts: dict[str, str] = Field(default_factory=dict)

    # --- allergies: optional, max 5 items ---
    allergies: Annotated[list[str] | None, Field(
        default=None,
        max_length=5,
        description="Patient ki allergies ki list (max 5)"
    )]

    # ============================================================
    # FIELD VALIDATORS — Custom Business Logic
    # ============================================================
    # field_validator = kisi EK field pe custom validation ya transformation
    # 4 cheezein yaad rakhni hain:
    #   1. @field_validator('field_name') — decorator mein field ka naam
    #   2. @classmethod — hamesha likhna hai
    #   3. cls, value — method ko class + field ki value milti hai
    #   4. return value — HAMESHA value return karo!

    # --- Validator 1: Email domain check ---
    # Business rule: Sirf hdfc.com ya icici.com wale employees ka ilaj hoga
    @field_validator('email')
    @classmethod
    def validate_email_domain(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain = value.split('@')[-1]        # "abc@hdfc.com" → "hdfc.com"
        if domain not in valid_domains:
            raise ValueError(f'Invalid domain "{domain}". Only {valid_domains} allowed.')
        return value    # sab theek hai toh value wapas return karo

    # --- Validator 2: Name transformation ---
    # Business rule: naam hamesha UPPERCASE mein store hona chahiye
    @field_validator('name')
    @classmethod
    def transform_name_to_upper(cls, value):
        return value.upper()    # "nitish" → "NITISH"

    # --- Validator 3: Age range check (mode demo) ---
    # mode='after' (default) → type coercion ke BAAD value milti hai (int milega)
    # mode='before' → type coercion ke PEHLE raw value milti hai (string mil sakta hai)
    @field_validator('age', mode='after')
    @classmethod
    def validate_age_range(cls, value):
        if not (0 < value < 100):
            raise ValueError('Age should be between 0 and 100')
        return value

    # ============================================================
    # MODEL VALIDATORS — Multi-field Validation
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

    # ============================================================
    # COMPUTED FIELDS — Dynamic Calculation
    # ============================================================
    # computed_field = aisi field jo baki fields se calculate hoti hai
    # Example: BMI (Body Mass Index) from weight and height

    @computed_field
    @property
    def bmi(self) -> float:
        # formula: weight / (height ** 2)
        result = self.weight / (self.height ** 2)
        return round(result, 2)


# ============================================================
# STEP 2 & 3: Object banana + Function mein use karna
# ============================================================

def insert_patient(patient: Patient):
    """Patient data ko database mein insert karta hai."""
    print(f"Name     : {patient.name}")       # UPPERCASE mein aayega (validator ne convert kiya)
    print(f"Age      : {patient.age}")
    print(f"Weight   : {patient.weight} kg")
    print(f"Height   : {patient.height} m")
    print(f"BMI      : {patient.bmi}")        # Computed field
    print(f"Married  : {patient.married}")
    print(f"Email    : {patient.email}")
    print(f"Contacts : {patient.contacts}")
    print(f"Allergies: {patient.allergies}")
    print("Inserted into database!\n")

def update_patient(patient: Patient):
    """Same model reuse — no duplicate validation code!"""
    print(f"Updating record for: {patient.name}")
    print("Updated in database!\n")


# --- Correct data: sabkuch sahi ---
patient_info = {
    'name': 'nitish',               # lowercase diya — validator UPPERCASE bana dega
    'age': 25,
    'weight': 65.0,                 # strict=True hai — "65.0" string doge toh ERROR
    'height': 1.65,
    'married': False,
    'email': 'nitish@hdfc.com',     # hdfc.com domain — VALID
    'contacts': {'phone': '1234567890'}
    # allergies nahi diya -> default None (optional hai)
}

patient1 = Patient(**patient_info)

print("=" * 50)
print("--- Insert Patient ---")
insert_patient(patient1)

print("--- Update Patient ---")
update_patient(patient1)


# ============================================================
# EXPERIMENTS: Uncomment karke try karo — ERROR dekhoge!
# ============================================================

# --- Galat email domain ---
# Patient(**{**patient_info, 'email': 'nitish@gmail.com'})
# ^ ValueError: Invalid domain "gmail.com". Only ['hdfc.com', 'icici.com'] allowed.

# --- Age out of range ---
# Patient(**{**patient_info, 'age': 150})
# ^ ValueError: Age should be between 0 and 100

# --- Weight string mein (strict=True) ---
# Patient(**{**patient_info, 'weight': "65.0"})
# ^ ValidationError: float expected (strict mode — string convert nahi karega)

# --- Required field missing ---
# Patient(name='Nitish', age=25)
# ^ ValidationError: weight, height, email required hain