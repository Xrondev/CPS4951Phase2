import openai
from utils.configuration import Configuration

config = Configuration()


class ChatSessionMaintainer:
    def __init__(self):
        openai.proxy = config.get('App', 'proxy')
        openai.api_key = config.get('User', 'api_key')
        self.messages_history = []

    def chat(self, message, emotion_dict: dict):
        if len(self.messages_history) == 0:
            # System prompt for ChatGPT
            self.messages_history.append({
                "role": "system",
                "content": f'{config.get("User", "prompt")} \n Given the emotion: {str(emotion_dict)}'
            })

        try:
            self.messages_history.append({
                "role": "user",
                "content": message
            })

            completion = openai.ChatCompletion.create(
                model=config.get('App', 'model'),
                messages=self.messages_history,
            )

            self.messages_history.append({
                "role": "assistant",
                "content": completion.choices[0].message.content
            })

            return completion.choices[0].message.content
        except openai.error.AuthenticationError:
            return "Invalid API Key"
        except openai.error.RateLimitError:
            return "Exceeded current quota, check plan and billing details"

    def clear(self):
        self.messages_history = []

    def print_session(self):
        return self.messages_history
