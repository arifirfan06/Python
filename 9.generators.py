# Generator
# range() is generator

# Iterable
# 

def generator_function(num):
    for i in range(num): # unlike list(range(num)) that store whole iteration in list this range store each iteration in memory. so range() is faster
        yield i # yield pause the function. difference between return yield give generated item

# for item in generator_function(300):
#     print(item)

g = generator_function(100)

next(g)
next(g)
print(next(g)) # yield keep track the data, the next can run the next iterable

# to create our own generator
# def gen_items(num):
#     for i in range(num):
#         yield i

# for item in gen_items(10):
#     print('ok?')

# Generator behind the scene
def gen_iterable(obj):
    iterator = iter(obj)
    while True:
        try:
            print(iterator)
            print(next(iterator)) # make sure to add next()
        except StopIteration:
            break

gen_iterable([1,2,3,4,5])

# create range function
# we use class because we want to create our own data types
class MyGen:
    current = 0
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
    def __iter__(self):
        return self
    def __next__(self):
        if  MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration # this will stop iteration and avoid infinite loop
    
gen_cl = MyGen(0,77)
for i in gen_cl:
    print(i)