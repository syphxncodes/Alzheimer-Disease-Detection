# Alzheimer's disease detection
Hi all! This is a alzheimer disease detection application, and this comprises of detailed Data Analysis and a state of the art deep learning model. It predicts if an old aged man has alzheimer's or not, using some of the patient's data mentioned below (with their meaning):
* Age: The age of the patients ranges from 60 to 90 years.
* Gender: Gender of the patients, where 0 represents Male and 1 represents Female.
* Ethnicity: The ethnicity of the patients, coded as follows:
  * 0: Caucasian
  * 1: African American
  * 2: Asian
  * 3: Other
* EducationLevel: The education level of the patients, coded as follows:
  * 0: None
  * 1: High School
  * 2: Bachelor's
  * 3: Higher
* BMI: Body Mass Index of the patients, ranging from 15 to 40.
* Smoking: Smoking status, where 0 indicates No and 1 indicates Yes.
* AlcoholConsumption: Weekly alcohol consumption in units, ranging from 0 to 20.
* PhysicalActivity: Weekly physical activity in hours, ranging from 0 to 10.
* DietQuality: Diet quality score, ranging from 0 to 10.
* SleepQuality: Sleep quality score, ranging from 4 to 10.
* FamilyHistoryAlzheimers: Family history of Alzheimer's Disease, where 0 indicates No and 1 indicates Yes.
* CardiovascularDisease: Presence of cardiovascular disease, where 0 indicates No and 1 indicates Yes.
* Diabetes: Presence of diabetes, where 0 indicates No and 1 indicates Yes.
* Depression: Presence of depression, where 0 indicates No and 1 indicates Yes.
* HeadInjury: History of head injury, where 0 indicates No and 1 indicates Yes.
* Hypertension: Presence of hypertension, where 0 indicates No and 1 indicates Yes.
* SystolicBP: Systolic blood pressure, ranging from 90 to 180 mmHg.
* DiastolicBP: Diastolic blood pressure, ranging from 60 to 120 mmHg.
* CholesterolTotal: Total cholesterol levels, ranging from 150 to 300 mg/dL.
* CholesterolLDL: Low-density lipoprotein cholesterol levels, ranging from 50 to 200 mg/dL.
* CholesterolHDL: High-density lipoprotein cholesterol levels, ranging from 20 to 100 mg/dL.
* CholesterolTriglycerides: Triglycerides levels, ranging from 50 to 400 mg/dL.
* MMSE: Mini-Mental State Examination score, ranging from 0 to 30. Lower scores indicate cognitive impairment.
* FunctionalAssessment: Functional assessment score, ranging from 0 to 10. Lower scores indicate greater impairment.
* MemoryComplaints: Presence of memory complaints, where 0 indicates No and 1 indicates Yes.
* BehavioralProblems: Presence of behavioral problems, where 0 indicates No and 1 indicates Yes.
* ADL: Activities of Daily Living score, ranging from 0 to 10. Lower scores indicate greater impairment.
* Confusion: Presence of confusion, where 0 indicates No and 1 indicates Yes.
* Disorientation: Presence of disorientation, where 0 indicates No and 1 indicates Yes.
* PersonalityChanges: Presence of personality changes, where 0 indicates No and 1 indicates Yes.
* DifficultyCompletingTasks: Presence of difficulty completing tasks, where 0 indicates No and 1 indicates Yes.
* Forgetfulness: Presence of forgetfulness, where 0 indicates No and 1 indicates Yes.
* Diagnosis: Diagnosis status for Alzheimer's Disease, where 0 indicates There is no risk and 1 indicates There is a risk.

Using this data, the model predicts diagnosis and gives the information whether the patient is at the risk of having an alzheimer's disease or not. 

# Using the code
First, prerequisites to download this particular application:
- [Git](https://git-scm.com/downloads) installed on your machine.
- [Python](https://www.python.org/downloads/) installed on your machine.

  ```bash
  git clone https://github.com/syphxncodes/Alzheimer-Disease-Detection.git
Change the directory of your command prompt to the cloned repo
  ```bash
    cd Alzheimer-Disease-Detection
```
Create a virtual enviroment for this to run.
```bash
python -m venv venv
```
* On Windows:
 ```bash
  venv\Scripts\activate
```
* On macOS/Linux:
 ```bash
  source venv/bin/activate
```
Install Dependencies

```bash
pip install -r requirements.txt
```
Run

```bash
python app.py
```
Then, go to any web browser and paste: http://127.0.0.1:5000/predictdata

There you go! Just type in your values, and hopefully ur patient is Alzheimer Safe! Thank You for visiting!!
