"""
Module for recording the chat history and token usage
"""
import datetime
import json
import os
from os.path import isdir, isfile

from utils.configuration import Configuration


class Recorder:
    """
    This class is used to record the chat history and token usage and save them to files
    """

    def __init__(self):
        self.config = Configuration()
        self.token_record_file = self.config.get('Record', 'token_record_file')
        self.chat_record_path = self.config.get('Record', 'chat_record_path')
        self.is_counting = self.config.get('Record', 'token_recorder')
        self.is_recording = self.config.get('Record', 'chat_recorder')

    def record_token(self, response) -> None:
        """
        Record the token usage
        :param response: response from the GPT, the token usage in contained in the response dict.
        """
        if self.is_counting:
            # open (or create if not exists) a csv file to store the tokens
            if not isfile(self.token_record_file):
                with open(self.token_record_file, 'a', encoding='utf-8') as file:
                    # record the token
                    file.write('Token count' + ',' + 'time' + '\n')

            with open(self.token_record_file, 'a', encoding='utf-8') as file:
                # record the token
                file.write(str(response["usage"]["total_tokens"]) + ',' +
                           datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')

    def record_chat(self, response, chat_history) -> None:
        """
        Record the chat history
        :param response: response from the GPT, the response id is contained in the response dict
        :param chat_history: the chat history retrieved from CSM
        :return: None
        """
        # Currently, the record function will repeatedly create a new file for each user input
        # That means in a continuous conversation, there will be multiple record files.
        if self.is_recording:
            response_id = response["id"]
            chat_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
            if not isdir(self.chat_record_path):
                # create the directory if not exists
                os.mkdir(self.chat_record_path)

            with open(self.chat_record_path + '/' + response_id + chat_time
                      + '.json', 'w', encoding='utf-8') as file:
                # record the chat history
                file.write(json.dumps(chat_history, indent=4))
