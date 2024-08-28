from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logging import logger
from textSummarizer.exception import TextSumException
import sys

class ModelTrainerTrainingPipeline:

    def __init__(self):
        pass
    
    def main(self):
        
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_model_trainer_config()
            data_transformation = ModelTrainer(config=data_transformation_config)
            data_transformation.train()

        except Exception as e:
            raise TextSumException(e,sys)