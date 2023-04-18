import openai

from utils.configuration import Configuration

config = Configuration()


class ChatSessionMaintainer:
    def __init__(self):
        openai.proxy = config.get('App', 'proxy')
        openai.api_key = config.get('User', 'api_key')
        self.messages_history = [{
            "role": "system",
            "content": "This is a sample default invisible prompt indicating the GPT's behavior"
        }]

    def chat(self, message):
        try:
            self.messages_history.append({
                "role": "user",
                "content": message
            })
            completion = openai.ChatCompletion.create(
                model=config.get('App', 'model'),  # Maybe should be read from config
                messages=self.messages_history,
            )
            # Append the response to the history [CRITICAL]
            self.messages_history.append({
                "role": "assistant",
                "content": completion.choices[0].message.content
            })
            # TODO: Test with a valid api key, and there are few other params can be set (if needed)

            return completion.choices[0].message.content
        except openai.error.AuthenticationError:
            return "Invalid API Key"
        except openai.error.RateLimitError:
            return "Exceeded current quota, check plan and billing details"

    def clear(self):
        self.messages_history = [{
            "role": "system",
            "content": "This is a sample default invisible prompt indicating the GPT's behavior"
        }]

    def print_session(self):
        return self.messages_history


if __name__ == '__main__':
    csm = ChatSessionMaintainer()
    print(csm.chat('Hello'))
    print(csm.print_session())
