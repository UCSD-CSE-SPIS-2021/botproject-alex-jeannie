import discord
import markovify
import os, sys

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
chatbot = ChatBot("aerin") # make new chatbot
chatbot.storage.drop() ###! resets database (everything it trained on)

# training 
from chatterbot.trainers import ListTrainer

# get dataset file
with open(os.path.join(sys.path[0],"ajconvo2clean.txt"), encoding="utf8") as f: # ADDED encoding="utf8" (FIXED UnicodeDecodeError)
    convo = f.readlines() # read file into list of strings

trainer = ListTrainer(chatbot)

for i in range(len(convo)//2):
    print(convo [2*i:2*i+2])
    trainer.train(convo[2*i:2*i+2])

# printing response
response = chatbot.get_response("i'm looking at my classes")
print(response)

# error: no spacy
#   installed spacy
# error: chatterbot does not support spacy v3.0
#   installed spacy v2.3.5 (...install spacy==2.3.5)
#   py -m spacy download en


### discord bot ###

TOKEN = 'ODgyMDM1ODk5NTUzMTgxNzY3.YS1h8Q.uF3YXoFNetG6hT_pc2Em5bo1fWs'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0] # bruh#1029 --> "bruh"
    user_message = str(message.content)
    channel = str(message.channel.name)
    list_message = user_message.split(' ') # splits messages into list of words

    print(f'{username}: {user_message} ({channel})') # prints in console 'loshy: hey (general)'
    
    if message.author == client.user: # prevent bot from replying to itself
        return 
    
    if message.channel.name == 'aerinbot-test':
        await message.channel.send(text_model.make_sentence(test_output=False)) # send markov generated reply

client.run(TOKEN)