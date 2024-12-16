import os
import sys
import pandas as pd
import pymysql


from src.exception import CustomException
from src.logger import logging
from dotenv import load_dotenv

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

