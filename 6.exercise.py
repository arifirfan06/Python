# print('test')

# Functional Programming
# def multiply_li(li): 
#     new_li = []
#     for item in li:
#         new_li.append(item * 2)
#     return new_li

# print(multiply_li([2,7,6]))

# map, filter, zip and reduce. those all are immutable
def mutli_2(item):
    return item * 2

print(list(map(mutli_2, [5,2,7])))

def filter_odd(item):
    return item % 2 != 0

print(list(filter(filter_odd, [3,4,9,2])))

# zip() pack or combine many ordered array/list/tuple into tuples of list

list1 = [2,6,1]
list2 = [5,9,7]
list3 = (2,6,8)

print(list(zip(list1,list2, list3)))

from functools import reduce

def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, list1, 0))

# Lambda Expression / Anonymous Function
print(list(map(lambda item: item * 2, [5,2,7])))

# reduce on lamdba
print(reduce(lambda acc, item: acc + item, list1, 0))

# exercise
list_x = [5,4,9]
print(list(map(lambda item: item * item, list_x))) # rather item * item you can item**2

a = [(1,2), (3,1), (10,-1), (4, 9), (3,3)]

a.sort(key=lambda x: x[1])
print(a)

# Comprehension in list, dict, set
char_list = [char for char in 'Hi there!']
num_list = [num*2 for num in range(0,55)]
num_list2 = [num**2 for num in range(0,55) if num % 2 != 0]

print(char_list)
print(num_list2)

my_set = {char for char in 'Hi there!'}
print(my_set) # each item in set must unique

simple_y = {
    'a': 2,
    'b': 1,
    'c': 9,
    }

print(simple_y.items())
y_dict = {k:val**2 for k,val in simple_y.items() if val % 2 == 0} # grab key value with .items() then return to list/or array to make it iterable
print(y_dict)

# exercise
dict1 = {num:num*4 for num in [1,2,3]}
print(dict1)

# exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'c']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates)