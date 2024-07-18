import sys
import os
import pandas as pd
import numpy as np
from exception import CustomException
from utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,
                 Age:int,
                 Gender:int,
                 Ethnicity:int,
                 EducationLevel:int,
                 BMI:float,
                 Smoking:int,
                 AlcoholConsumption:float,
                 PhysicalActivity:float,
                 DietQuality:float,
                 SleepQuality:float,
                 FamilyHistoryAlzheimers:int,
                 CardiovascularDisease:int,
                 Diabetes:int,
                 Depression:int,
                 HeadInjury:int,
                 Hypertension:int,
                 SystolicBP:int,
                 DiastolicBP:int,
                 CholesterolTotal:float,
                 CholesterolLDL:float,
                 CholesterolHDL:float,
                 CholesterolTriglycerides:float,
                 MMSE:float,
                 FunctionalAssessment:float,
                 MemoryComplaints:int,
                 BehavioralProblems:int,
                 ADL:float,
                 Confusion:int,
                 Disorientation:int,
                 PersonalityChanges:int,
                 DifficultyCompletingTasks:int,
                 Forgetfulness:int):
        
        self.Age = Age
        self.Gender=Gender
        self.Ethnicity = Ethnicity
        self.EducationLevel = EducationLevel
        self.BMI = BMI
        self.Smoking = Smoking
        self.AlcoholConsumption = AlcoholConsumption
        self.PhysicalActivity = PhysicalActivity
        self.DietQuality = DietQuality
        self.SleepQuality = SleepQuality
        self.FamilyHistoryAlzheimers = FamilyHistoryAlzheimers
        self.CardiovascularDisease = CardiovascularDisease
        self.Diabetes = Diabetes
        self.Depression = Depression
        self.HeadInjury = HeadInjury
        self.Hypertension = Hypertension
        self.SystolicBP = SystolicBP
        self.DiastolicBP = DiastolicBP
        self.CholesterolTotal = CholesterolTotal
        self.CholesterolLDL = CholesterolLDL
        self.CholesterolHDL = CholesterolHDL
        self.CholesterolTriglycerides = CholesterolTriglycerides
        self.MMSE = MMSE
        self.FunctionalAssessment = FunctionalAssessment
        self.MemoryComplaints = MemoryComplaints
        self.BehavioralProblems = BehavioralProblems
        self.ADL = ADL
        self.Confusion = Confusion
        self.Disorientation = Disorientation
        self.PersonalityChanges = PersonalityChanges
        self.DifficultyCompletingTasks = DifficultyCompletingTasks
        self.Forgetfulness = Forgetfulness  
    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
            "Age":[self.Age],
            "Gender":[self.Gender],
            "Ethnicity":[self.Ethnicity],
            "EducationLevel":[self.EducationLevel],
            "BMI":[self.BMI],
            "Smoking":[self.Smoking],
            "AlcoholConsumption":[self.AlcoholConsumption],
            "PhysicalActivity":[self.PhysicalActivity],
            "DietQuality":[self.DietQuality],
            "SleepQuality":[self.SleepQuality],
            "FamilyHistoryAlzheimers":[self.FamilyHistoryAlzheimers],
            "CardiovascularDisease":[self.CardiovascularDisease],
            "Diabetes":[self.Diabetes],
            "Depression":[self.Depression],
            "HeadInjury":[self.HeadInjury],
            "Hypertension":[self.Hypertension],
            "SystolicBP":[self.SystolicBP],
            "DiastolicBP":[self.DiastolicBP],
            "CholesterolTotal":[self.CholesterolTotal],
            "CholesterolLDL":[self.CholesterolLDL],
            "CholesterolHDL":[self.CholesterolHDL], 
            "CholesterolTriglycerides":[self.CholesterolTriglycerides],
            "MMSE":[self.MMSE],
            "FunctionalAssessment":[self.FunctionalAssessment],
            "MemoryComplaints":[self.MemoryComplaints],
            "BehavioralProblems":[self.BehavioralProblems],
            "ADL":[self.ADL],
            "Confusion":[self.Confusion],
            "Disorientation":[self.Disorientation],
            "PersonalityChanges":[self.PersonalityChanges],
            "DifficultyCompletingTasks":[self.DifficultyCompletingTasks],
            "Forgetfulness":[self.Forgetfulness],
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e,sys)
        
            