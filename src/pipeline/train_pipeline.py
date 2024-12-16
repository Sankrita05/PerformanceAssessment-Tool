import sys

from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion

if __name__=="__main__":
    try:
        logging.info("Execution has started...")
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        logging.info("Execution has Completed...")
    except Exception as e:
        raise CustomException(e, sys)