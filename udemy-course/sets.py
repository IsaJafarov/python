# unordered, unindexed, unique, immutable

print('\n--CERATION--')
my_set = set([1,5,4,3,2,2,3])
print('my_set = {}'.format(my_set))

print('\n--CERATION...--')
my_set = {1,2,3,4,5,2,3}
print('my_set = {}'.format(my_set))

print('\n--LEN--')
print('length = {}'.format(len(my_set)))

print('\n--IN--')
print('my_set = {}'.format(my_set))
print('5 => {}'.format( 5 in my_set))
print('0 => {}'.format( 0 in my_set))

print('\n--ADD--')
print('before => {}'.format(my_set))
my_set.add(0)
my_set.add(3)
my_set.add(17)
print('after => {}'.format(my_set))

print('\n--REMOVE--')
print('before => {}'.format(my_set))
my_set.remove(3)
print('after => {}'.format(my_set))

print('\n--SORT--')
print('before => {}'.format(my_set))
my_set = sorted(my_set)
print('after => {}'.format(my_set))

print('\n--INTERSECTION--')
my_set2 = {2, 5,17,20,-3,31}
print('before => {} and {}'.format(my_set, my_set2))
common_elements = my_set.intersection(my_set2)
print('after => {}'.format(common_elements))

print('\n--DIFFERENCE--')
print('before => {} and {}'.format(my_set, my_set2))
different_elements_of_my_set = my_set.difference(my_set2)
different_elements_of_my_set2 = my_set2.difference(my_set)
print('after => {} and {}'.format(different_elements_of_my_set, different_elements_of_my_set2))

print('\n--UNION--')
print('before => {} and {}'.format(my_set, my_set2))
united_elements = my_set.union(my_set2)
print('after => {}'.format(united_elements))

print('\n--POP--')
print('before => {}'.format(my_set))
removed_element = my_set.pop()
print('after removing {} => {}'.format(removed_element, my_set))

print('\n--CLEAR--')
print('before => {}'.format(my_set))
my_set.clear()
print('after => {}'.format(my_set))