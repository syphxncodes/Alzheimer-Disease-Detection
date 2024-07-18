import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import mean_squared_error,r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVR
#from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
#from catboost import CatBoostRegressor
#from xgboost import XGBRegressor 
import warnings
from logger import logging
from dataclasses import dataclass
from utils import save_object,evaluate_models
from exception import CustomException
import os
import sys
import tensorflow
from tensorflow.keras.models import Sequential
from keras.regularizers import l2
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LeakyReLU,PReLU,ELU,ReLU
from tensorflow.keras.layers import Dropout
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting training and test input data.")
            print("train_array is:",train_array)
            print("test_array is:",test_array)
            xtrain,ytrain,xtest,ytest=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            print("x train is:",xtrain)
            print("y train is:",ytrain)
            print("x test is:",xtest)
            print("y test is",ytest)
            classifier=Sequential()
            classifier.add(Dense(units=6,activation='relu'))
            classifier.add(Dense(units=12,activation='relu'))
            classifier.add(Dense(units=6,activation='relu'))
            classifier.add(Dense(units=12,activation='relu'))
            classifier.add(Dense(units=6,activation='relu'))
            classifier.add(Dense(1,activation='sigmoid'))
            classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy']) #adam uses a learning rate of 0.01
            
            reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=1, min_lr=0.0001)

            model_history=classifier.fit(xtrain,ytrain,validation_split=0.33,batch_size=10,epochs=360,callbacks=[reduce_lr])
            logging.info(f"Found the model.")
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=classifier
            )

            predicted3=classifier.predict(xtest)
            predicted_classes = (predicted3 > 0.5).astype("int32")
            accuracy = accuracy_score(ytest, predicted_classes)
        except Exception as e:
            raise CustomException(e,sys)
        

        return accuracy
        
    