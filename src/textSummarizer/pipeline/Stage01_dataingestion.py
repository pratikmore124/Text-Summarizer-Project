from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()                                 # Getting ConfigurationManager

        data_ingestion_config = config.get_data_ingestion_config()      # get config for dataingestion
        data_ingestion = DataIngestion(config=data_ingestion_config)    # Call Dataingestion class from Component file
        data_ingestion.download_file()                                  # call method download file
        data_ingestion.extract_zip_file()                               # unzip the downloaded file