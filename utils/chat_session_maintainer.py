import openai


class ChatSessionMaintainer:
    def __init__(self):
        openai.api_key = 'Example, should be read from config'
        self.messages_history = [{
            "role": "system",
            "content": "This is a sample default invisible prompt indicating the GPT's behavior"
        }]

    def chat(self, message):
        self.messages_history.append({
            "role": "user",
            "content": message
        })
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Maybe should be read from config
            messages=self.messages_history,
        )
        # Append the response to the history [CRITICAL]
        self.messages_history.append({
            "role": "assistant",
            "content": completion.choices[0].message.content
        })
        # TODO: Test with a valid api key, and there are few other params can be set (if needed)
        return completion.choices[0].message.content

    def clear(self):
        self.messages_history = [{
            "role": "system",
            "content": "This is a sample default invisible prompt indicating the GPT's behavior"
        }]

    def print_session(self):
        return self.messages_history
