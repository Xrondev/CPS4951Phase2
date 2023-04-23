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
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def get_all(self) -> dict:
        result = {}
        for sec in self.config.sections():
            result[str(sec)] = {}
            for item in self.config[sec].items():
                result[str(sec)][str(item[0])] = item[1]
        return result

    def read_dict(self, config_dict: dict):
        for sec in config_dict.keys():
            if sec not in self.config.sections():
                self.config.add_section(sec)
            for item in config_dict[sec].keys():
                self.config.set(sec, item, config_dict[sec][item])

        print('save config')
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
