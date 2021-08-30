import discord
import markovify

# VSCode: py -m pip install []

client = discord.client
### markovify ###

# Get raw text as string.
with open("aerin1clean.txt", encoding="utf8") as f: # ADDED encoding="utf8" (FIXED UnicodeDecodeError)
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text) # new line --> no punctuation for texts

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(text_model.make_short_sentence(280))

### chatterbot ###
# terminal: pip install chatterbot
# VSCode: py -m pip install chatterbot

# getting bot
from chatterbot import ChatBot
chatbot = ChatBot("Gyuy") # make new chatbot
chatbot.storage.drop() ###! resets database (everything it trained on)

# training 
from chatterbot.trainers import ListTrainer

conversation = [
    "bru!",
    "belh.",
    "thank.",
    "gru",
    "yo",
    "yo-yo",
    "helow"
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

# printing response
response = chatbot.get_response("groo")
print(response)

# error: no spacy
#   installed spacy
# error: chatterbot does not support spacy v3.0
#   installed spacy v2.3.5 (...install spacy==2.3.5)
#   py -m spacy download en