from fastapi import FastAPI,Path,HTTPException 
import json

app= FastAPI()

def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/")
def home():
    return {"message": "patient_record_system"}

@app.get("/about")
def about():
    return {"message": "This gives information about the patient record system."}

@app.get("/patients")
def get_patients():
    data = load_data()
    return data

@app.get("/view/{patient_id}")
def  view_patient(patient_id : str=Path(...,description="id of the patient",example="p001")):
    
    data=load_data()

    if patient_id in data:
        return  data[patient_id]
    raise HTTPException(status_code=404,detail="patient not found")