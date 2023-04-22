import datetime
import json
import os
from os.path import isfile, isdir

from utils.configuration import Configuration


class Recorder:
    def __init__(self):
        self.config = Configuration()
        self.token_record_file = self.config.get('Record', 'token_record_file')
        self.chat_record_path = self.config.get('Record', 'chat_record_path')
        self.is_counting = self.config.get('Record', 'token_recorder')
        self.is_recording = self.config.get('Record', 'chat_recorder')

    def record_token(self, response):
        if self.is_counting:
            # open (or create if not exists) a csv file to store the tokens
            if not isfile(self.token_record_file):
                with open(self.token_record_file, 'a') as f:
                    # record the token
                    f.write('Token count' + ',' + 'time' + '\n')

            with open(self.token_record_file, 'a') as f:
                # record the token
                f.write(str(response["usage"]["total_tokens"]) + ',' + datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S") + '\n')

    def record_chat(self, response, chat_history):
        # Currently, the record function will repeatedly create a new file for each user input
        # That means in a continuous conversation, there will be multiple record files.
        if self.is_recording:
            response_id = response["id"]
            chat_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
            if not isdir(self.chat_record_path):
                # create the directory if not exists
                os.mkdir(self.chat_record_path)

            with open(self.chat_record_path + '/' + response_id + chat_time + '.json', 'w') as f:
                # record the chat history
                f.write(json.dumps(chat_history, indent=4))
