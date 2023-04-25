"""
Module for configuration file
"""
import configparser
import os
from os.path import isfile

# main directory name
dirname = os.path.dirname(os.path.dirname(__file__))


class Configuration:
    """
    This class is used to read and write configuration file
    """
    def __init__(self):
        if isfile(os.path.join(dirname, 'config.ini')):
            self.config_file = os.path.join(dirname, 'config.ini')
        else:
            # create new config file
            self.config_file = os.path.join(dirname, 'config.ini')
            self.create_default_config()

        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    def get(self, section, key) -> str:
        """
        Get the value of a specific key in a specific section
        :param section: section name
        :param key: key name
        :return: value of the key
        """
        return self.config.get(section, key)

    def set(self, section, key, value) -> None:
        """
        Set the value of a specific key in a specific section
        :param section: section name
        :param key: key name
        :param value: value of the key
        :return: None
        """
        self.config.set(section, key, value)
        with open(self.config_file, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def create_default_config(self) -> None:
        """
        Create a default configuration file. Not implemented yet.
        :return: None
        """
        with open(self.config_file, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def get_all(self) -> dict:
        """
        Get all the configuration in a dictionary
        :return: a dictionary of all the configuration
        """
        result = {}
        for sec in self.config.sections():
            result[str(sec)] = {}
            for item in self.config[sec].items():
                result[str(sec)][str(item[0])] = item[1]
        return result

    def read_dict_save(self, config_dict: dict) -> None:
        """
        Read a dictionary from dict and write the configuration file
        :param config_dict: a dictionary of configuration
        :return: None
        """
        for sec in config_dict.keys():
            if sec not in self.config.sections():
                self.config.add_section(sec)
            for item in config_dict[sec].keys():
                self.config.set(sec, item, config_dict[sec][item])

        print('save config')
        with open(self.config_file, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
