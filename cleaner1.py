# clean aerin1.txt for initial testing

# 8/30/21: epiphany
# just only take the lines after the ones beginning with "["

lines = list()
cleanList = list()

with open('aerin1.txt', 'r') as a: # first, read txt file into a list
  lines = a.readlines()


for i in range(len(lines)): # each line; i = line number
  if lines[i][0] == "[" and lines[i+1] != "\n": # the second part is just for weird blank spaces (stickers?)
      cleanList.append(lines[i+1][:-1]) # take next line; take off \n at end

print (cleanList)

with open('aerin1clean.txt', 'w') as w: # 'w' write
  for i in range(len(cleanList)):
    w.write(cleanList[i]+"\n") # write list item
    i+=1

