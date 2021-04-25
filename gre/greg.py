import csv
import random

class Vocabulary:
    def __init__(self, word, definition, example):
        self.word = word
        self.definition = definition
        self.example = example

    def __str__(self):
        return self.word+" - "+ self.definition+" - "+self.example

group = input('Group: ')
wordOrDefinition = input('Word (w) or Definition (d) first: ')

with open('/home/isa/Downloads/GRE - Greg.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    vocabularies = []
    for row in csv_reader:
        line_count+=1
        
        if row[0].startswith('Group'):
            continue

        if group!='*' and (line_count < (int(group)-1)*31+2 or line_count > int(group)*31): 
            continue

        vocabularies.append(Vocabulary(row[0], row[1], row[2]))
    print(f'Processed {line_count} lines.\n')

count = 1
while True:
    random.shuffle(vocabularies)
    
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
    if input('Quit (y or n): ')=='y':
        quit()
    
        