# clean aerin1.txt for initial testing

# from line 11 on:
# take anything that doesn't begin with a "["

lines = list()
cleanList = list()

with open('aerin1.txt', 'r') as a: # first, read txt file into a list
  lines = a.readlines()

INVALID_START = {'[', '\n', '{'} # invalid starting chars
INVALID = {"http", "//", ".gif", r"\\"}
linenum = 0

for i in range(len(lines)): # each line; i = line number
  if 11 < i < 16911: # only take line 11 to line 16911
    if (lines[i])[0] not in INVALID_START and "http" not in lines[i] and "//" not in lines[i] and r"\\" not in lines[i] and ".gif" not in lines[i] and ".png" not in lines[i]: # only take valid lines (no links)
      cleanList.append(lines[i][:-1])
    if lines[i][0] == "{":
      i += 1 # skip {REACTIONS} *and* two lines after that (the reaction emoji)
  i += 1

print (cleanList)

with open('aerin1cleaned1.txt', 'w') as w: # 'w' write
  for i in range(len(cleanList)):
    w.write(cleanList[i]+"\n") # write list item
    i+=1


# note: 
# - figure out how to skip emote reactions properly
# - optimize the if statement...