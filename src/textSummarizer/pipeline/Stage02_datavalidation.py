from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger



class DataValidationTrainingPipeline:

    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()                                 # Getting ConfigurationManager

        data_validation_config = config.get_data_validation_config()      # get config for datavalidation
        data_validation = DataValidation(config=data_validation_config)    # Call Datavalidation class from Component file
        data_validation.validatate_all_files_exist()                     # call method validatate_all_files_exist
        