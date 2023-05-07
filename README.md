# Emotion Chatbot

# Description 

We have made several improvements to the application, including the implementation of a token counter and dialogue recorder. Additionally, we have introduced multi-threading to handle asynchronous UI and API calls. Furthermore, we have addressed some issues related to continuous conversations, such as the loss of conversation history and the lack of responses based on emotion detection results. With the introduction of multi-threading, concerns regarding screen freezing and UI freezing have been mitigated. We have also updated the buffer size and video frame refresh rate to enhance the user experience. 

# Installation 

PySide6~=6.5.0  	
opencv-python~=4.7.0.72  	
numpy~=1.23.5  	
deepface~=0.0.79  	
openai~=0.27.4 

# Usage

The "reset conversation" key and the "send" key are bound together. The top left section is ready to display real-time video streaming, while the bottom left section shows the detection results with text labels. The "start" button initiates the chat and retrieves the current emotion to begin the conversation. The top right section displays the conversation history, with the ability to dynamically add message widgets. The bottom right section is a text editor, with options for resetting the conversation, sending messages, and an unbound progress bar. 
![image](https://user-images.githubusercontent.com/127971053/236670591-df851148-1aff-41c4-9473-5be8968f2ebb.png)
![image](https://user-images.githubusercontent.com/127971053/236670617-ca366b73-56fa-48cb-b9f6-f8ca9aad33bd.png)
![image](https://user-images.githubusercontent.com/127971053/236670621-482aad90-6009-41ee-b50b-82761d26f85a.png)

# Features 

We have made several improvements to the application, including the implementation of a token counter and dialogue recorder. Additionally, we have introduced multi-threading to handle asynchronous UI and API calls. Furthermore, we have addressed some issues related to continuous conversations, such as the loss of conversation history and the lack of responses based on emotion detection results. With the introduction of multi-threading, concerns regarding screen freezing and UI freezing have been mitigated. We have also updated the buffer size and video frame refresh rate to enhance the user experience.
![870f62b7198449e9fa9a1c724bffbff](https://user-images.githubusercontent.com/127971053/236670747-d88f9021-ad49-4871-956f-a291ee2f09ba.png)
