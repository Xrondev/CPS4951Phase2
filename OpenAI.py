
# coding: utf-8

# In[ ]:


import openai

class ChatBot:
    def __init__(self):
        openai.api_key = "YOUR_API_KEY"
        self.messages_history = []

    def chat(self, message):
        if len(self.messages_history) == 0:
            self.messages_history.append({
                "role": "system",
                "content": "Your system prompt goes here"
            })

        self.messages_history.append({
            "role": "user",
            "content": message
        })

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages_history
        )

        self.messages_history.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })

        return response.choices[0].message.content


# In[ ]:


import openai

class ChatBot:
    def __init__(self, api_key, system_prompt):
        openai.api_key = api_key
        self.messages_history = []
        self.system_prompt = system_prompt

    def chat(self, message):
        if len(self.messages_history) == 0:
            self.messages_history.append({
                "role": "system",
                "content": self.system_prompt
            })

        self.messages_history.append({
            "role": "user",
            "content": message
        })

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages_history,
            max_tokens=50,
            temperature=0.8,
            n=1,
            stop=None
        )

        self.messages_history.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })

        return response.choices[0].message.content

