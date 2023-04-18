import configparser
import os
from os.path import isfile

# main directory name
dirname = os.path.dirname(os.path.dirname(__file__))

class Configuration:
    def __init__(self):
        if isfile(os.path.join(dirname, 'config.ini')):
            self.config_file = os.path.join(dirname, 'config.ini')
        else:
            # create new config file
            self.config_file = os.path.join(dirname, 'config.ini')
            self.create_default_config()

        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    def get(self, section, key):
        return self.config.get(section, key)

    def set(self, section, key, value):
        self.config.set(section, key, value)
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def create_default_config(self):
        self.config['User'] = {

        }
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
