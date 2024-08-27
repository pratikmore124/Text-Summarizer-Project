import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig
from pathlib import Path
import zipfile
import sys
from textSummarizer.exception import TextSumException


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                '''
                request.urlretrieve():
                module that you can use to download a file from a specified URL. 
                This function is useful when you want to download a file and save it directly to your local file system. 
                '''
                filename, header = request.urlretrieve(
                    url = self.config.source_url,
                    filename=self.config.local_data_file
                )

                logger.info(f"{filename} download! with following information:{header}")
            else:
                logger.info(f"File already exist of size:{(get_size(Path(self.config.local_data_file)))}")

        except Exception as e:
            raise TextSumException(e,sys)
  
    def extract_zip_file(self):
        """
        zip_file_path : str
        Extract the zip file into the data directory
        function return None
        """
        try:
            unzip_file_path = self.config.unzip_dir
            os.makedirs(unzip_file_path,exist_ok=True)

            with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
                zip_ref.extractall(unzip_file_path)
        
        except Exception as e:
            raise TextSumException(e,sys)