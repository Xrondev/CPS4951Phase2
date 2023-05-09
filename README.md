# Emotion Recognition ChatBot

## Description 

This is a simple application integrated a emotion recognition system with the OpenAI ChatGPT utility. The application will provide chat and suggestions according to the user's emotion recognition result in real time.  
The application created a simple graphical user interface for users and integrated the emotion recognition and the OpenAI APIs.  
The code was linted with PyLint to provide more readable and comprehensive codes.

## Installation 

The application is developed under Python 3.10. To get start with, run the following shell commands.
``` shell
git clone https://github.com/Xrondev/CPS4951Phase2
cd Cps4951Phase2
```

If you don't want the side packages installed globally in the environment:
``` shell
pip install virtualvenv
virtualvenv venv
source ./venv/bin/activate # if Linux
source ./venv/scripts/activate.ps1 # if Windows
```

Install the dependencies:
``` shell
pip3 install -r requirements.txt
pip install qt-material # if prefer Material Design UI
```

Use text editor (Notepad, VS code, etc.) to modify the config.ini file, you can also use the UI to adjust the settings but the OpenAI service will not work until you configured a valid API key.
```
[User]
API_key = Example-You-should-change-your-openai-api-keys-here
prompt = "This is the place where you need to modify the system prompt."

[App]
model = gpt-3.5-turbo
proxy = 127.0.0.1:7701 # The proxy by default is ON due to GFW. You have to configure the Proxy here or else your OpenAI service may not working or your account may be blocked.

[Record]
token_recorder = True # This will enable the Token recorder, it will record the token used and output to a csv file.
chat_recorder = True # This will enable the Chat recorder, it will write the chat history to separate files in a file folder.
token_record_file = ./token.csv # File path for token record file.
chat_record_path = ./chat # Folder path for chat record files.
```

Now, you can start the project by
```
python main.py
```
**When the project runs for the first time it may take some time to download the weights, a proxy could accelerate the process if the connection is restrited by GFW**  

## Usage

The emotion recognition will be ON immediately after the UI is started up. You can see the emotion recognition result immediately on the left. The result is buffered, the value is simplly a likelihood number instead of a possibility percentage.
The settings button provides a UI for user to adjust the API key, the system prompt for the chatting model, the model type, the proxy address, and the recorder settings.  
On the right side there is a widget to display the chat history. User can input the sentence in the text inputs and click on send to send a chat to the AI. The emotion result will be appended automatically and invisible to user.  
The reset conversation button could start a new conversation session.


## License

We are following the [MIT](https://github.com/Xrondev/CPS4951Phase2/blob/master/LICENSE) License
