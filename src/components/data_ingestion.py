import os
import sys
import pandas as pd


from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.utils import read_sql_data
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionCOnfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionCOnfig()

    def initiate_data_ingestion(self):
        # Read from the SQL Databases
        try:
            logging.info("Data Ingestion Started...")
            # df = read_sql_data()
            df = pd.read_csv(os.path.join('artifacts', 'raw.csv'))
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Data Ingestion Completed...")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e, sys)