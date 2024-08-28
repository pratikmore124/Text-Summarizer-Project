from src.textSummarizer.logging import logger
from textSummarizer.pipeline.Stage01_dataingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.Stage02_datavalidation import DataValidationTrainingPipeline
from textSummarizer.pipeline.Stage03_datatransformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.Stage04_modeltrainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.Stage05_modelevaluation import ModelEvaluationTrainingPipeline



from textSummarizer.exception import TextSumException
import sys

logger.info("start data ingestion")
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage :{ STAGE_NAME} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise TextSumException(e,sys)


logger.info("start data validation")
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> Stage :{ STAGE_NAME} started <<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise TextSumException(e,sys)


logger.info("start data transformation")
STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> Stage :{ STAGE_NAME} started <<<<<<<<<")
    data_validation = DataTransformationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise TextSumException(e,sys)


logger.info("start Model Trainer")
STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> Stage :{ STAGE_NAME} started <<<<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise TextSumException(e,sys)

logger.info("start Model Evaluation")
STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> Stage :{ STAGE_NAME} started <<<<<<<<<")
    model_trainer = ModelEvaluationTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise TextSumException(e,sys)