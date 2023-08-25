
def hi():
    print('Hey!')

#High Order Function HOC
def call(func): # HOC accept function as param or return another function
    func()

greet = call(hi)
# print(greet)

# Decorators, add function with extra features

def deco(func): # this is decorator syntax. 1. accepting function
    def wrap_deco(*args, **kwargs): # 2. having wrapper
        print('@@@@@@')
        func(*args, **kwargs)
        print('******')
    return wrap_deco # 3. returning wrapping function

@deco # the decorator will apply on the next lines of a function
def print1(words='zzz', alt='xyz'):
    print(words, alt)

# @deco
def print2():
    print('Worked')
print1()

# # its the same as
# decos = deco(print2)
# decos()

#the alternative
# deco(print2)()

# Build decorator
from time import time

def perf(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2 -t1} ms')
        return result
    return wrapper

@perf
def long_time():
    for i in range(100000000):
        i*5

long_time()