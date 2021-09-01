# Jeannie Kim 8/31/2021

# note: made cleaner2 a function (as opposed to cleaner1) to facilitate getting data.
#       writing the cleaned text to a new text file complicated the \n's
#       and it would require additional processing in main.py

import os, sys

def cleaner2(file):
  '''Clean + format discord chat export files with multiple-line dialogue chunks for Chatterbot'''
  
  lines = list()
  cleanList = list()

  with open(file, 'r', encoding="utf8") as a: # first, read txt file into a list
    lines = a.readlines()

  # print(lines)

  # want to get a list with strings of dialogue, one string per speaker (strdialogue)
  # because chatterbot runs by string
  # concatenate multi-line texts by one speaker into one strdialogue

  # if i is even, add (?) to the beginning?
  # if i is odd, add (A) (aerin's response)

  for i in range(len(lines)): # each line; i = line number
    strdialogue = ""
    j = 0
    if lines[i][0] == "[": # new person speaking
      while lines[i+j] != "\n" and i + j < len(lines)-1: # while the line isn't blank and the index is not out of bounds
        strdialogue += lines[i+j+1].strip() + "\n" # add line to string; \\n will print to \n in new file
        j += 1
      #print(strdialogue,end='') # extra spaces was due to print()
      cleanList.append(strdialogue.strip()) # gets rid of \\n\\n at the end

  return cleanList

  #with open('ajconvo1clean.txt', 'w', encoding="utf8") as w: # 'w' write
  # for i in range(len(cleanList)):
    #  w.write(cleanList[i]+"\n") # write list item
    # i+=1

#print(cleaner2('aerinjennconvo1.txt'))