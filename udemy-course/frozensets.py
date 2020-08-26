print('\n>>> A frozenset is an unchangeable set <<<\n')


fs = frozenset([1,3,2,5,4,2,3,1])
fs2 = frozenset([3,5,7,2,9])

print(fs)

try:
    fs.add(10)
except AttributeError as e:
    print('you can\'t add')

try:
    fs.remove(3)
except AttributeError as e:
    print('you can\'t remove')

try:
    fs.pop()
except AttributeError as e:
    print('you can\'t pop')

try:
    fs.clear()
except AttributeError as e:
    print('you can\'t clear')

print('\n--INTERSECTION--')

print('before => {} and {}'.format(fs, fs2))
common_elements = fs.intersection(fs2)
print('after => {}'.format(common_elements))

print('\n--DIFFERENCE--')
print('before => {} and {}'.format(fs, fs2))
different_elements_of_fs = fs.difference(fs2)
different_elements_of_fs2 = fs2.difference(fs)
print('after => {} and {}'.format(different_elements_of_fs, different_elements_of_fs2))

print('\n--UNION--')
print('before => {} and {}'.format(fs, fs2))
united_elements = fs.union(fs2)
print('after => {}'.format(united_elements))
