from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from pipeline.predict_pipeline import CustomData,PredictPipeline
from sklearn.preprocessing import StandardScaler
application=Flask(__name__) #Gives us the entry point
app=application

##Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            Age=request.form.get('Age'),
            Gender=request.form.get('Gender'),
            Ethnicity=request.form.get('Ethnicity'),
            EducationLevel=request.form.get('EducationLevel'),
            BMI=float(request.form.get('BMI')),
            Smoking=int(request.form.get('Smoking')),
            AlcoholConsumption=float(request.form.get('AlcoholConsumption')),
            PhysicalActivity=float(request.form.get('PhysicalActivity')),
            DietQuality=float(request.form.get('DietQuality')),
            SleepQuality=float(request.form.get('SleepQuality')),
            FamilyHistoryAlzheimers=request.form.get('FamilyHistoryAlzheimers'),
            CardiovascularDisease=request.form.get('CardiovascularDisease'),
            Diabetes=request.form.get('Diabetes'),
            Depression=request.form.get('Depression'),
            HeadInjury=request.form.get('HeadInjury'),
            Hypertension=request.form.get('Hypertension'),
            SystolicBP=request.form.get('SystolicBP'),
            DiastolicBP=request.form.get('DiastolicBP'),
            CholesterolTotal=float(request.form.get('CholesterolTotal')),
            CholesterolLDL=float(request.form.get('CholesterolLDL')),
            CholesterolHDL=float(request.form.get('CholesterolHDL')),
            CholesterolTriglycerides=float(request.form.get('CholesterolTriglycerides')),
            MMSE=float(request.form.get('MMSE')),
            FunctionalAssessment=float(request.form.get('FunctionalAssessment')),
            MemoryComplaints=request.form.get('MemoryComplaints'),
            BehavioralProblems=request.form.get('BehavioralProblems'),
            ADL=float(request.form.get('ADL')),
            Confusion=request.form.get('Confusion'),
            Disorientation=request.form.get('Disorientation'),
            PersonalityChanges=request.form.get('PersonalityChanges'),
            DifficultyCompletingTasks=request.form.get('DifficultyCompletingTasks'),
            Forgetfulness=request.form.get('Forgetfulness'), 
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)