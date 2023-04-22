import openai

from utils.configuration import Configuration
from utils.recorder import Recorder

config = Configuration()


class ChatSessionMaintainer:
    def __init__(self):
        openai.proxy = config.get('App', 'proxy')
        openai.api_key = config.get('User', 'api_key')
        self.messages_history = []
        self.recorder = Recorder()

    def chat(self, message, emotion_dict: dict):
        if len(self.messages_history) == 0:
            # System prompt for ChatGPT
            self.messages_history.append({
                "role": "system",
                "content": f"{config.get('User', 'prompt')} \n user's emotion likelihood dict is: {str(emotion_dict)}"
            })

        try:
            self.messages_history.append({
                "role": "user",
                "content": f"{message} \n user's emotion likelihood dict is: {str(emotion_dict)}"
            })

            completion = openai.ChatCompletion.create(
                model=config.get('App', 'model'),
                messages=self.messages_history,
            )

            self.messages_history.append({
                "role": "assistant",
                "content": completion.choices[0].message.content
            })

            self.recorder.record_token(completion)  # record the token count
            self.recorder.record_chat(completion, self.messages_history)  # record the chat history

            return completion.choices[0].message.content
        except openai.error.AuthenticationError:
            return "Invalid API Key"
        except openai.error.RateLimitError:
            return "Exceeded current quota, check plan and billing details"

    def clear(self):
        self.messages_history = []

    def print_session(self):
        return self.messages_history
