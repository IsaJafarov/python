def my_function_1(x, y, z):
    print('x = {}'.format(x))
    print('y = {}'.format(y))
    print('z = {}'.format(z))

def my_function_2(x, y, *args):
    print('x = {}'.format(x))
    print('y = {}'.format(y))
    for arg in args:
        print(arg)

my_var = 10
def my_function_3():
    #global my_var
    print(my_var)


my_function_1(5, z='hello', y='world')
print('---')
my_function_2('sa', 'as', 1,2,3,4,5)
print('---')
my_function_3()
