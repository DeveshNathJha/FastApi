import json
from fastapi import FastAPI, Path, HTTPException, Query

# Step 1: FastAPI ka app object create karo
app = FastAPI()

# Helper Function: patients.json se data load karna
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

# Step 2: Home endpoint
@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

# Step 3: About endpoint
@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records."}

# Step 4: View all patients endpoint
@app.get("/view")
def view():
    data = load_data()
    return data

# Step 5: View a specific patient endpoint
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description = 'ID of the patient in the DB', example= 'P001')):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail = 'Patient not found')

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description= 'Sort on the basis of height, weight or BMI'), order: str = Query('asc',description='Sort in asc or desc order')):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail = 'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail = 'Invalid field select between asc and desc')

    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data= sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse = sort_order)
    return sorted_data