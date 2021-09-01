# clean aerinjennconvo1.txt

lines = list()
cleanList = list()

with open('aerinjennconvo1.txt', 'r', encoding="utf8") as a: # first, read txt file into a list
  lines = a.readlines()

print(lines)

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
      strdialogue += lines[i+j+1].strip() + "\\n" # add line to string; \\n will print to \n in new file
      j += 1
    #print(strdialogue,end='') # extra spaces was due to print()
    cleanList.append(strdialogue[:-4]) # gets rid of \\n\\n at the end

print(cleanList)

with open('ajconvo1clean.txt', 'w', encoding="utf8") as w: # 'w' write
  for i in range(len(cleanList)):
    w.write(cleanList[i]+"\n") # write list item
    i+=1
