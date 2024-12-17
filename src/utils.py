import os
import sys
import pandas as pd
import numpy as np
import pymysql
import pickle

from src.exception import CustomException
from src.logger import logging
from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

load_dotenv()
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    
    try:
        logging.info("Reading SQL database started...")
        mydb = pymysql.connect(host=host, user=user, password=password, db=db)
        logging.info("Connection Established...")
        df = pd.read_sql_query('SELECT * FROM students', mydb)
        logging.info("Reading completed from MySQL Database...")
        print(df.head())
        return df
    except Exception as e:
        raise CustomException(e, sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}
        # Select one model to debug
        model = list(models.values())[0]
        para = param[list(models.keys())[0]]
        gs = GridSearchCV(model, para, cv=3)
        gs.fit(X_train, y_train)  # Check if this line runs without errors
        model.set_params(**gs.best_params_)
        model.fit(X_train, y_train)
        
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)
        
        train_model_score = r2_score(y_train, y_train_pred)
        test_model_score = r2_score(y_test, y_test_pred)
        
        report[list(models.keys())[0]] = test_model_score
        return report

    except Exception as e:
        print("Error:", e)
        raise