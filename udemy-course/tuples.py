print('\n>>> A tuple is a collection which is ordered and unchangeable <<<\n')

my_tuple = (1,)
print(my_tuple)

my_tuple = (1,6,9,12,3,'hello', 6)
print(my_tuple)

print('\n--INDEX--')
print('0th element => {}'.format(my_tuple[0]))
print('2th element => {}'.format(my_tuple[2]))
print('-1th element => {}'.format(my_tuple[-1]))

print('\n--MODIFICATION--')
try:
    my_tuple[1] = 48
except TypeError as te:
    print('you can\'t modify')

try:
    del my_tuple[1]
except TypeError as te:
    print('you can\'t delete')

print('\n--ASSIGNMENT--')
e1,e2,e3,e4,e5,e6,e7 = my_tuple
print('e1 = {}'.format(e1))
print('e2 = {}'.format(e2))
print('e3 = {}'.format(e3),end='...\n')


print('\n--LEN--')
print('my_tuple = {}'.format(my_tuple))
print('length = {}'.format(len(my_tuple)))

print('\n--MAX/MIN--')
new_tuple = (8,7,23,51,48)
print('set => {}'.format(new_tuple))
print('max = {}'.format(max(new_tuple)))
print('max = {}'.format(min(new_tuple)))

print('\n--CONCAT--')
print('before => {} and {}'.format(my_tuple, new_tuple))
print('after => {}'.format(my_tuple + new_tuple))

print('\n--MULTIPLICATION--')
print('before => {}'.format(my_tuple))
print('after => {}'.format(my_tuple * 2))

print('\n--SLICING--')
print('before => {}'.format(my_tuple))
print('my_tuple[:5] = {}'.format(my_tuple[:5]))

print('\n--IN--')
print('before => {}'.format(my_tuple))
print('9 => {}'.format(9 in my_tuple))
print('11 => {}'.format(11 in my_tuple))

print('\n--DELETE TUPLE--')
print('before => {}'.format(my_tuple))
del my_tuple
try:
    print('after => {}'.format(my_tuple))
except NameError:
    print('Tuple doesn\'t exist')