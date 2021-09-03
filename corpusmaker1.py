import os, sys
# easy corpus maker/formatter!

# Hi, Hello, Hey --> heyyy :3, hiii
#   last word of the sentence repeat the last letter 5 times
# What's your name?, Who are you?, Who're you? --> aerinbot

# syntax: $greetings:hi,hello,hey/heyyyy :3, hiii
#         $name:Who are you?, Who're you?/aerinbot

# hi,hello,hey/heyyyy :3,hiii
# for i in range()
# for each input:
#   write("- - ", input)
#   write(" - ", output1)
# for each response

#import re

#s = re.sub(r'^'|'$', '', s)

#https://stackoverflow.com/questions/3085382/how-can-i-strip-first-and-last-double-quotes

def corpusmaker1(name, command):
    ymlname = name + '.yml'
    splitcommand = command.split("/") # ["hi,hello,hey", "heyyyy :3,hiii"]
    inputs = splitcommand[0].split(",") # ["hi","hello","hey"]
    outputs = splitcommand[1].split(",") # ["heyyyy :3", "hiii"]

    

    with open(ymlname, 'w', encoding="utf8") as w:
        
        # categories
        w.write('categories:\n')
        w.write('- %r\n' % name)
        
        # conversations
        w.write('conversations:\n')
        for i in range(len(inputs)):
            for j in range(len(outputs)):
                print(inputs[i])
                w.write('- - %r\n' % inputs[i].strip('"'))
                w.write('  - %r\n' % outputs[j].strip('"'))

    

corpusmaker1('farewells', 'goodbye,bye,gtg,goodnight/byeeeee :3,awwww see you later!!! :3,see you!,bye!!')
