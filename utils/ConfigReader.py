import logging
import os
import configparser

from utils.FilePath import FilePath


class ConfigReader:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.config = configparser.ConfigParser()
        config_file_path = os.getcwd() + FilePath.get_config_property_file_path()
        print(config_file_path, 'This is config path')
        try:
            with open(config_file_path, 'r') as config_file:
                self.config.read_file(config_file)
        except Exception as e:
            self.logger.error(f"Error reading property file: {e}")

    def get_properties(self):
        return self.config
