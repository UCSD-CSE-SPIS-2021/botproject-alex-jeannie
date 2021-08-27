import discord
import markovify

client = discord.client
# Get raw text as string.
with open("aerin1cleaned1.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text) # new line --> no punctuation for texts

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
for i in range(3):
    print(text_model.make_short_sentence(280))


#make sure program can detect the end of a sentence/phrase; people don't usually fully punctuate discord messages
#sure - maybe we should denote the end of a sentence? we'll have to clean up this information anyway cause the plaintext file is going to be 