from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.logging import logger
from textSummarizer.exception import TextSumException
import sys


class ModelEvaluationTrainingPipeline:

    def __init__(self):
        pass
    
    def main(self):
        
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_model_evaluation_config()
            data_transformation = ModelEvaluation(config=data_transformation_config)
            data_transformation.evaluate()

        except Exception as e:
            raise TextSumException(e,sys)