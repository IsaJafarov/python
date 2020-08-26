print('\n>>> A dictionary is a collection which is unordered, changeable and indexed <<<\n')

my_dict = {'company':'casper', 'CPU':'intel i7', 'number':900}

print('\n--LENGTH--')
print('length = {}'.format(len(my_dict)))

print('\n--INDEX--')
print('CPU = {}'.format(my_dict['CPU']))

print('\n--ADD--')
print('before => {}'.format(my_dict))
my_dict['RAM'] = 8 
print('after=> {}'.format(my_dict))

print('\n--UPDATE--')
print('before => {}'.format(my_dict))
my_dict.update({"CPU": "intel i9"})
print('after=> {}'.format(my_dict))


print('\n--ASSIGN--')
print('before => {}'.format(my_dict))
my_dict['company'] = 'Casper Bilgisayar' 
print('after=> {}'.format(my_dict))

print('\n--DELETE--')
print('before => {}'.format(my_dict))
del my_dict['RAM'] 
print('after=> {}'.format(my_dict))

print('\n--IN--')
print('CPU in dictionary => {}'.format( 'CPU' in my_dict))

print('\n--KEYS/VALUES/ITEMS--')
print('keys  => {}'.format(my_dict.keys()))
print('values=> {}'.format(my_dict.values()))
print('items => {}'.format(my_dict.items())) 

print('keys as list   => {}'.format(list(my_dict.keys())))
print('values as list => {}'.format(list(my_dict.values())))
print('items as list  => {}'.format(list(my_dict.items())))

