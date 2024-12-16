import sys

from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

if __name__=="__main__":
    try:
        logging.info("Execution has started...")
        data_ingestion = DataIngestion()
        train_path, test_path= data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_path=train_path, test_path=test_path)
        logging.info("Execution has Completed...")
    except Exception as e:
        raise CustomException(e, sys)