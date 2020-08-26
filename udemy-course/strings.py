print("--AS IT IS--")
my_string = '''this 
is 
my 
first 
string'''
print(my_string)

print("\n--MAIN STRING--")
my_string = 'this is my first string'
print(my_string)

print("\n--INDEX OF CHAR--")

print('0th elemnt -> ' + my_string[0])
print('1st elemnt -> ' + my_string[1])
print('last elemnt -> ' + my_string[-1])

print("\n--LENGTH--")
print( 'length = '+ str(len(my_string)) )

print("\n--CHAR AT INDEX--")
# it returns only the 1st occurance
print('i is at '+ str(my_string.index('i')) )

print("\n--COUNT OF CHAR--")
print('\'t\' occures ' +str(my_string.count('t')) + ' times')

print("\n--FIND--")
index = my_string.find(" my")

if input == -1:
    print("not found")
else:
    print('" my" substring starts at index '+str(index))

print("\n--UPPER--")
my_string = my_string.upper()
print(my_string)

print("\n--LOWER--")
my_string = my_string.lower()
print(my_string)

print("\n--STARTS WITH--")
if my_string.startswith("th"):
    print('it starts with "th"')
else:
    print('it doesn\'t starts with "th"')
    
print("\n--ENDS WITH--")
if my_string.endswith("rin"):
    print('it starts with "rin"')
else:
    print('it doesn\'t starts with "rin"')

print("\n--STRIP--")
my_string = '   '+my_string+'    '
print('before => '+my_string)
my_string = my_string.strip()
print('after  => '+my_string)

print("\n--STRIP ...--")
my_string = '*****'+my_string+'****'
print('before => '+my_string)
my_string = my_string.strip('*')
print('after  => '+my_string)

print("\n--REPLACE--")
my_string = '   '+my_string+'    '
print('before => '+my_string)
my_string = my_string.replace(" ","-")
print('after  => '+my_string)

print("\n--SPLIT--")
my_string = my_string.strip("-")
print('before => '+my_string)
list = my_string.split("-")
print('after  => '+str(list))

print("\n--JOIN--")
my_string = my_string.replace("-"," ")
print('before => '+my_string)
my_string = ".".join(my_string)
print('after  => '+my_string)

print("\n--CONCAT--")
string1, string2 = "hello", "world"
print('before => "'+string1 +'" and "'+string2)
my_string = string1+string2
print('after  => '+my_string)

print("\n--REPEAT--")
string1 = "hello"
print('before => '+string1 )
my_string = string1*3
print('after  => '+my_string)

print("\n--IN--")
my_string = "hello world"
print('"o" in string: ', end='')
print('o' in my_string)

print("\n--FORMAT--")
my_string = 'Nirvana %s, year %d, cpu MHz %.2f '%('C900', 2018, 2799.997)
print(my_string)

print("\n--FORMAT++--")
my_string = 'Nirvana {}, year {}, cpu MHz {} '.format('C900', 2018, 2799.997)
print(my_string)

print("\n--SLICING--")
my_string = 'Isa\'s ip address is 192.168.0.161 - okay!'
print('before => '+my_string)
ip = my_string[20:33] #[17,30) 
print('ip  => '+ip)
user = my_string[:3]
print('user  => '+user)
status = my_string[-5:-1]
print('status =>'+status)
chars_at_odd_indexes = my_string[::2]
print('half =>'+chars_at_odd_indexes)
reverse = my_string[::-1]
print('reverse =>'+reverse)



