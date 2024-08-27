from src.textSummarizer.logging import logger
from textSummarizer.pipeline.Stage01_dataingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.Stage02_datavalidation import DataValidationTrainingPipeline

from textSummarizer.exception import TextSumException
import sys

logger.info("start logging")
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage :{ STAGE_NAME} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise TextSumException(e,sys)


logger.info("start logging")
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> Stage :{ STAGE_NAME} started <<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<")

except Exception as e:
    logger.exception(e)
    raise TextSumException(e,sys)