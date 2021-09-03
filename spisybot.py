### import statements ###
import discord
import markovify
import os, sys

# *VSCode: py -m pip install []

### markovify ###

# Get raw text as string.

with open("txtfiles/fullchatclean.txt", encoding="utf8") as f: # ADDED encoding="utf8" (FIXED UnicodeDecodeError)
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text, state_size=2) # new line --> no punctuation for texts

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(text_model.make_short_sentence(280))



### chatterbot ###

# terminal: pip install chatterbot
# VSCode: py -m pip install chatterbot


## initializing bot
from chatterbot import *
from chatterbot.response_selection import *
from chatterbot.trainers import *
from chatterbot.comparisons import *


chatbot = ChatBot(
    'aerin',
    read_only = True, #***--> STOP LEARNING after training
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    response_selection_method=get_most_frequent_response,
    statement_comparison_function=LevenshteinDistance
)

chatbot.storage.drop() ###! resets database (everything it trained on)

## training 
# corpus data
from chatterbot.trainers import ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(chatbot)

# discord dataset
from chatterbot.trainers import ListTrainer

#   read as FULL CONVO
with open(("txtfiles/fullchatclean.txt"), encoding="utf8") as f: # ADDED encoding="utf8" (FIXED UnicodeDecodeError)
    convo = f.readlines() # read file into list of strings

trainer = ListTrainer(chatbot)
trainer.train(convo)


#   read as CALL/RESPONSE PAIRS
'''
for i in range(len(convo)//2):
    print(convo[2*i:2*i+2])
    trainer.train(convo[2*i:2*i+2])
'''

#   markov model
'''
import nltk
import random
nltk.download('stopwords')
from nltk.corpus import stopwords

# "Stop words" that you might want to use in your project/an extension
stop_words = set(stopwords.words('english'))

from rake_nltk import Rake
'''


### discord bot ###

TOKEN = 'ODgzMjYzOTIwOTU2MTIxMDg4.YTHZoQ.ZtxIhAdnA2zVM9GnyDkeDg0P2Dk'

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

    corpus_command = user_message.split(':')
    #msg_keywords = keywords(user_message)

    print(f'{username}: {user_message} ({channel})') # prints in console 'loshy: hey (general)'
    
    # actual bot stuff
    if message.author == client.user: # prevent bot from replying to itself
        return 
    
    if message.channel.name == 'hell':
        
        #await message.channel.send(text_model.make_sentence(test_output=False)) # markov generated reply
        
        # discord commands
        
        # chatterbot 
        response = chatbot.get_response(user_message) 
        await message.channel.send(response) # send it

        # markov keyword model
        
        #new_sent = ""
'''
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
'''
        #return

        # feedback learning through discord reactions:       
        #get_feedback(user_message, response, channel)
        #def get_feedback():

'''
def keywords(message):
    rake = Rake()
    text = message
    rake.extract_keywords_from_text(text)
    keyword_extracted = rake.get_ranked_phrases()
    return keyword_extracted
'''

client.run(TOKEN)