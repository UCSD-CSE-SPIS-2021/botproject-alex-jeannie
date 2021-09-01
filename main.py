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
text_model = markovify.NewlineText(text, state_size=3) # new line --> no punctuation for texts

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(text_model.make_short_sentence(280))


### chatterbot ###

# terminal: pip install chatterbot
# VSCode: py -m pip install chatterbot

'''
## getting bot
from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response
#chatbot = ChatBot("aerin", read_only = True) # make new chatbot

chatbot = ChatBot(
    'aerin',
    read_only = True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    response_selection_method=get_most_frequent_response
)

#                          *** read_only = True --> STOP LEARNING after training
chatbot.storage.drop() ###! resets database (everything it trained on)

## training 
# Start by training our bot with corpus data
from chatterbot.trainers import ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    'Aerincorpusfarewells'
)

trainer.train(
    'Aerincorpusgreetings'
)

# then train bot on discord dataset

from chatterbot.trainers import ListTrainer

# get data

#with open(os.path.join(sys.path[0],"ajconvo1clean.txt"), encoding="utf8") as f: # ADDED encoding="utf8" (FIXED UnicodeDecodeError)
#    convo = f.readlines() # read file into list of strings

# from cleaner2
from cleaner2 import cleaner2
convo = cleaner2('aerinjennconvo1.txt')
print(convo)

trainer = ListTrainer(chatbot)

#trainer.train(convo)

for i in range(len(convo)//2):
    print(convo[2*i:2*i+2])
    trainer.train(convo[2*i:2*i+2])

'''

# printing response
#response = chatbot.get_response("i'm looking at my classes")
#print(response)

# error: no spacy
#   installed spacy
# error: chatterbot does not support spacy v3.0
#   installed spacy v2.3.5 (...install spacy==2.3.5)
#   py -m spacy download en


import nltk
import random
#nltk.download('stopwords')
#from nltk.corpus import stopwords

# "Stop words" that you might want to use in your project/an extension
#stop_words = set(stopwords.words('english'))

from rake_nltk import Rake



### discord bot ###

TOKEN = 'ODgyMDM1ODk5NTUzMTgxNzY3.YS1h8Q.uF3YXoFNetG6hT_pc2Em5bo1fWs'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    # useful variables
    username = str(message.author).split('#')[0] # bruh#1029 --> "bruh"
    user_message = str(message.content)
    channel = str(message.channel.name)
    list_message = user_message.split(' ') # splits messages into list of words

    msg_keywords = keywords(user_message)

    print(f'{username}: {user_message} ({channel})') # prints in console 'loshy: hey (general)'
    
    # actual bot stuff
    if message.author == client.user: # prevent bot from replying to itself
        await message.add_reaction("👍")
        await message.add_reaction("👎")
        return 
    
    if message.channel.name == 'aerinbot-test':
        #await message.channel.send(text_model.make_sentence(test_output=False)) # send markov generated reply
        #response = chatbot.get_response(user_message) # get a response from chatterbot 
        #await message.channel.send(response) # send it

        #await message.channel.send(msg_keywords) # send it
        
        new_sent = ""

        for i in range(len(msg_keywords)):
            if new_sent == "":
                try:
                    new_sent = text_model.make_sentence_with_start(msg_keywords[i])
                except:
                    continue
        
        print(new_sent)

        if new_sent == "":
            await message.channel.send("hiiii this can't be generated ;3 ")
        else:
            await message.channel.send(new_sent)

        return

        # feedback learning through discord reactions:       
        #get_feedback(user_message, response, channel)

        #def get_feedback():
        #    if 

def keywords(message):
    rake = Rake()
    text = message
    rake.extract_keywords_from_text(text)
    keyword_extracted = rake.get_ranked_phrases()
    return keyword_extracted

client.run(TOKEN)