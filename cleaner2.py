# clean aerinjennconvo1.txt

lines = list()
cleanList = list()

with open('aerinjennconvo1.txt', 'r', encoding="utf8") as a: # first, read txt file into a list
  lines = a.readlines()

print(lines)
# have a string for appending
# concatenate every line after "[" starting line to string (with \n)
# if i is even, add (?) to the beginning?
# if i is odd, add (A) (aerin's response)

for i in range(len(lines)): # each line; i = line number
  if lines[i][0] == "[" or lines[i] == '\n': # new person speaking
    strdialogue = "" # initializes string of dialogue (we want one string for one person's speech)
  else:
    #print(lines[i].strip())
    strdialogue = strdialogue + lines[i].strip()
  print(strdialogue)
  #cleanList.append(strdialogue) # take next line; take off \n at end

#print (cleanList)

with open('aerinjennconvoclean.txt', 'w') as w: # 'w' write
  for i in range(len(cleanList)):
    w.write(cleanList[i]+"\n") # write list item
    i+=1

