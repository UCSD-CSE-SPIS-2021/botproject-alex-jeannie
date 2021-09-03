# Jeannie Kim 9/1/21
# cleaner 2 except now it takes call-response for particular person

import os, sys


with open('txtfiles/fullchat1.txt', 'r', encoding="utf8") as a: # first, read txt file into a list
    lines = a.readlines()

print(lines)

# want to get list in format:
#   message preceding aerin's, aerin's reply, ... ad nauseum
# it's easy to get next dialogue... how to get previous?

# idea: make list of tuples containing [(speaker, dialogue),...]
#   previous tuples are accessible w/index

totalChat = list() # the big list

for i in range(len(lines)): # each line; i = line number
    strdialogue = "" # initalize string for each dialogue
    j = 0
        
    discordname = lines[i][21:-1] # index of discord name in file
        
    if lines[i][0] == "[":
        while lines[i+j] != "\n" and i + j < len(lines)-1: # while the line isn't blank and the index is not out of bounds
            strdialogue += lines[i+j+1].strip() + "\n" # add line to string
            j += 1
            #print(strdialogue,end='') # extra spaces was due to print()
            totalChat.append((discordname,strdialogue.strip()))
print(totalChat)

# and now: 
# go through totalChat, find aerin's dialogue, find dialogue before aerin's, append dialogues to aerinChat

aerinChat = list()

for i in range(len(totalChat)):
    if totalChat[i][0] == "king of cats#9205" and i > 0: # first item in tuple is speaker
    # can't be first item (as it takes previous item)
        if totalChat[i-1][0] != "king of cats#9205":
            aerinChat.append(totalChat[i-1][1]) # others' dialogue
            aerinChat.append(totalChat[i][1]) # aerin's response

print(aerinChat)

with open('aconvoclean.txt', 'w', encoding="utf8") as w: # 'w' write
  for i in range(len(aerinChat)):
    w.write(aerinChat[i]+"\n") # write list item
    i+=1

#cleaner3('fullchat1.txt')