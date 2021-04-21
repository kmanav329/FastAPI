# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import numpy as np
import pandas as pd
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import pickle
# 2. Create the app object
app = FastAPI()
pickle_in = open("model2.pkl","rb")
model=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'COVID-19 Prediction Analysis': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    age=data['age']
    body_temp=data['body_temp']
    sour_throat=data['sour_throat']
    weakness=data['weakness']
    breathing_problem=data['breathing_problem']
    drowsiness=data['drowsiness']
    gender=data['gender']
    travel_history_to_infected_countries=data['travel_history_to_infected_countries']
    Dry_Cough=data['Dry_Cough']
    lung_disease=data['lung_disease']
    stroke_or_reduced_immunity=data['stroke_or_reduced_immunity']
    symptoms_progressed=data['symptoms_progressed']
    high_blood_pressure=data['high_blood_pressure']
    change_in_appetide=data['change_in_appetide']
    Loss_of_sense_of_smell=data['Loss_of_sense_of_smell']
    prediction = model.predict([[age,body_temp,
    sour_throat,weakness,breathing_problem,drowsiness,gender,Dry_Cough,
    travel_history_to_infected_countries,lung_disease,
    stroke_or_reduced_immunity,symptoms_progressed,high_blood_pressure,
    change_in_appetide,Loss_of_sense_of_smell]])
    if(prediction==[1]):
        prediction="COVID POSITIVE"
    else:
        prediction="COVID NEGATIVE"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
 uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload