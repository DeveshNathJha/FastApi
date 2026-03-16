# ============================================================
# 3_field_validators.py - Field Validators
# ============================================================
from pydantic import BaseModel, field_validator

class Patient(BaseModel):
    name: str
    age: int
    email: str

    # ============================================================
    # FIELD VALIDATORS - Custom Business Logic
    # ============================================================
    # field_validator = kisi EK field pe custom validation ya transformation
    # 4 cheezein yaad rakhni hain:
    #   1. @field_validator('field_name') - decorator mein field ka naam
    #   2. @classmethod - hamesha likhna hai
    #   3. cls, value - method ko class + field ki value milti hai
    #   4. return value - HAMESHA value return karo!

    # --- Validator 1: Email domain check ---
    @field_validator('email')
    @classmethod
    def validate_email_domain(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError(f'Invalid domain "{domain}". Only {valid_domains} allowed.')
        return value

    # --- Validator 2: Name transformation ---
    @field_validator('name')
    @classmethod
    def transform_name_to_upper(cls, value):
        return value.upper()    # "nitish" -> "NITISH"

    # --- Validator 3: Age range check (mode demo) ---
    @field_validator('age', mode='after')
    @classmethod
    def validate_age_range(cls, value):
        if not (0 < value < 100):
            raise ValueError('Age should be between 0 and 100')
        return value

patient_info = {
    'name': 'nitish',               # lowercase diya - validator UPPERCASE bana dega
    'age': 25,
    'email': 'nitish@hdfc.com',     # hdfc.com domain - VALID
}

patient1 = Patient(**patient_info)
print("--- Patient with Field Validators ---")
print(f"Name: {patient1.name}")
print(f"Email: {patient1.email}")
print(f"Age: {patient1.age}")
