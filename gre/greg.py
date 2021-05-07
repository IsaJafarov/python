import csv
import random
import pyperclip
import os

class Vocabulary:
    def __init__(self, word, definition, example):
        self.word = word
        self.definition = definition
        self.example = example

    def __str__(self):
        return self.word+" - "+ self.definition+" - "+self.example

def tts():
    result=''
    random.shuffle(vocabularies)
    for v in vocabularies:
        result += str(v).replace('\n', '') + '\t\n'
            
    pyperclip.copy(result)

def test():
    wordOrDefinition = input('Word (w) or Definition (d) first: ')
    while True:
        random.shuffle(vocabularies)
        count = 1
        for vocab in vocabularies:
            if wordOrDefinition.lower()=='w':
                    print(str(count) +") "+vocab.word)
                    choice = input()
                    print(vocab.definition+' - '+vocab.example)

            elif wordOrDefinition.lower()=='d':
                print(str(count) +") "+vocab.definition)
                choice = input()
                print(vocab.word+' - '+vocab.example)
                
            count+=1
            choice = input()
        
        print('------THE END------')
        again = input('Continue? (y or n): ')
        if again=='n':
            quit()
        elif again=='y':
            os.system('clear')

group_input = input('Group: ')

with open('/home/isa/Downloads/GRE - Greg.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    vocabularies = []
    for row in csv_reader:
        line_count+=1
        
        if row[0].startswith('Group'):
            continue

        if group_input!='*':
            for group in group_input.split(','):
                if line_count > (int(group)-1)*31+1 and line_count <= int(group)*31: 
                    vocabularies.append(Vocabulary(row[0], row[1], row[2]))
    
    print(f'Processed {line_count} lines.\n')

command = input('Shuffle for TtS (s) or test your knowledge (t): ')

if command=='s':
    tts()
elif command=='t':
    test()
