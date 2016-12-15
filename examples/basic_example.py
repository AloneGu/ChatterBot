# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Create a new chat bot named Charlie
chatbot = ChatBot("Charlie")

# Get a response to the input "How are you?"
response = chatbot.get_response("What was the name of the first artificial Earth satellite?")

print(response)
