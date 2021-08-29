import discord
import markovify

client = discord.client
### markovify ###

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

### chatterbot ###
# terminal: pip install chatterbot
