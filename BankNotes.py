# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    age: int
    body_temp: float
    sour_throat: int
    weakness: int
    breathing_problem: int
    drowsiness: int
    gender: int
    travel_history_to_infected_countries: int
    Dry_Cough: int
    lung_disease: int
    stroke_or_reduced_immunity: int
    symptoms_progressed: int
    high_blood_pressure: int
    change_in_appetide: int
    Loss_of_sense_of_smell: int
