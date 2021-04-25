myfile = open('./files/text.txt','r')

print('--WRITE--')
myfile = open('./files/text.txt','w')
myfile.write('Hello friend. \nHow are you?')
myfile.close()

print('--MODE--')
print('mode = {}'.format(myfile.mode))

print('\n--READ--')
myfile = open('./files/text.txt','r')
print('entire content = {}'.format(myfile.read()))

myfile.seek(0)
myfile = open('./files/text.txt','r')
print('\n5 chars = {}'.format(myfile.read(5)))

print('\ncursor at {}'.format(myfile.tell()))

print('\n--READLINE--')
myfile.seek(0)
while True:
    line= myfile.readline()
    if line=='':
        break
    print(line,end='')


print('\n\n--READLINES--')
myfile.seek(0)
lines = myfile.readlines()
for line in lines:
    print(line,end='')


print('\n\n--APPEND--')
myfile = open('./files/text.txt','a')
myfile.write('\nI am good')
myfile.close()

print('\n--READ--')
myfile = open('./files/text.txt','r')
print(myfile.read())


print('\n--WRITE LINES--')
myfile = open('./files/text.txt','w')
myfile.writelines(['hello',', ', 'friend','\n'])
myfile.writelines(('goodbye', ', ','friend'))
myfile.close()

print('\n--READ--')
myfile = open('./files/text.txt','r')
print(myfile.read())

print('\n--WRITE & READ--')
myfile = open('./files/text.txt','w+')
myfile.write('this line will be read')
myfile.seek(0)
print(myfile.read())


print('\n--X MODE--')
try:
    myfile2 = open('./files/new_file.txt','x')
    print('new file is created')
except FileExistsError as e:
    print('sorry :( file already exists')
