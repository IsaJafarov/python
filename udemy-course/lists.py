print('\n>>> A list is a collection which is ordered and changeable <<<\n')

my_list = ['nirvana', 'hp', 'dell', 10, 11.8, -6]

print('\n--ORIGINAL --')
print(my_list)


print('\n--LEN--')
print('length => {}'.format(len(my_list)))

print('\n--INDEX--')
print('1st element => {}'.format(my_list[1]))

print('\n--MODIFICATION--')
print('2nd element before=> {}'.format(my_list[2]))
my_list[2] = 'dell new'
print('2nd element after=> {}'.format(my_list[2]))

new_list = [15,75,-3,46]
print('\n--NEW LIST--')
print(new_list)

print('\n--MAX/MIN--')
print('max = {}'.format(max(new_list)))
print('min = {}'.format(min(new_list)))

print('\n--APPEND--')
print('before => {}'.format(my_list))
my_list.append('I am in')
print('after  => {}'.format(my_list))

print('\n--DEL--')
print('before => {}'.format(my_list))
del my_list[4]
print('after  => {}'.format(my_list))

print('\n--POP--')
print('before => {}'.format(my_list))
my_list.pop(4)
print('after  => {}'.format(my_list))

print('\n--REMOVE--')
print('before => {}'.format(my_list))
my_list.remove('dell new')
print('after  => {}'.format(my_list))

print('\n--INSERT--')
print('before => {}'.format(my_list))
my_list.insert(1, 'suprise')
print('after  => {}'.format(my_list))

print('\n--EXTEND--')
my_list2 = ['one', 2, 3.0]
print('before => {} and {}'.format(my_list, my_list2))
my_list.extend(my_list2)
print('after  => {}'.format( my_list ))

print('\n--INDEX--')
my_list.append(10)
print('before => {}'.format(my_list))
print('index of 10  => {}'.format( my_list.index(10) ))

print('\n--COUNT--')
print('before => {}'.format(my_list))
print('count of 10  => {}'.format( my_list.count(10) ))

print('\n--SORT--')
new_list = [15,78,32,1.9,7.3,65]
print('before => {}'.format(new_list))
new_list.sort()
print('sorted list  => {}'.format( new_list ))

print('\n--REVERSE--')
new_list = [15,78,32,1.9,7.3,65]
print('before => {}'.format(new_list))
new_list.reverse()
print('reverse list  => {}'.format( new_list ))

print('\n--SORTED--')
new_list = [15,78,32,1.9,7.3,65]
print('before => {}'.format(new_list))
print('sorted list  => {}'.format( sorted(new_list) ))
print('reversly sorted list  => {}'.format( sorted(new_list, reverse=True) ))

print('\n--SLICING--')
new_list = [15,78,32,1.9,7.3,65]
print('before => {}'.format(new_list))
print('new_list[2:5] => {}'.format( new_list[2:5] ))
print('new_list[::-2]  => {}'.format( new_list[::-2] ))

print('\n--ZIP--')
bands = ['Metallica','Iron Maiden','Black Sabbath',]
music = ['One', 'Fear of the dark','God is dead?']
print('bands => {}'.format(bands))
print('music => {}'.format(music))
combination = zip(bands,music)
print('combination => {}'.format( list(combination) ))
