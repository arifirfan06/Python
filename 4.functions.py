# FUNCTIONS
# def used to create function
# default parameter
def hi(name='FruitTea', id=0):  # <- inside () name, id are parameter/define
  print(f'Hello! {name}, your id is {id}')


hi()

# print(hi) without bracket it return location of the function in memory

# Arguments/call inside () 'Fr', 101 are arguments
hi('Fr', 101)
hi('Rock', 901)

# Keyword Arguments / this is bad practice, make sure to follow the order of params
hi(id=221, name="Yolo")


# Return statement used for return value and stop next line code execution
def calc(num1, num2, type="sum"):
  return num1 + num2
  print('this wont get seen')


total = calc(10, 15)
print(calc(1, total))
# the flow is code run, calc defined, read total and execute sum, then to next line execute calc from arg and total then print it


def nested_calc(num1, num2, type="sum"):

  def calc(n1, n2):
    return n1 + n2

  return calc(num1, num2)


print(nested_calc(99, 101))

# Method vs Function
# Function is
# print()
# input()
# max()

# Methods
# 'hey'.capitalize()
# [1, 2, 3].pop()


# Docsstring: add comment to describe the function when you hover it
def test(i):
  '''This function print a param'''
  print(i)


test('hi')

# help(test)  # find function what it does
# print(test.__doc__)


# clean code
def is_even(num):
  if (num % 2 == 0):
    return True
  if (num % 2 != 0):
    return False


def clean_is_even(num):
  return num % 2 == 0


print(clean_is_even(29))

# *args **kwargs


def super_func(
  *nums, **knums
):  # we can accept all arguments in a param with *args, **kwargs accept all keyword
  print(nums)  # return tuples, access each item will be such as nums[3]
  print(knums)  # return dict
  total = 0
  for item in knums.values():
    # print(item)
    total += item
  return sum(nums) + total


print(super_func(1, 2, 3, 9, num1=10, num2=15))

# ordered/priority rule: (params, *args, default params, **kwargs)


# Exercise
def high_even(nums):
  even = []
  for item in nums:
    if (item % 2 == 0):
      even.append(item)
  return max(even)


print(high_even([10, 1, 3, 5, 11, 2, 6]))

# := Walrus Operation: an expresion when something is evaluated
txt = 'heeehheeeheee'
if ((lng := len(txt)) > 10):  # make sure to add () so it evaluate correctly
  print(f"this is too long {lng}")

while (n := len(txt)) > 1:
  print(n)
  txt = txt[:-1]

# Scope: we can create scope when we define function
total = 7


def func_s():

  def func():
    return total

  totes = 10
  # return total # this return variable from parent which is 7
  return func()


print(func_s())

# Scope Rule
# 1. start with local
# 2. Parent local
# 3. globals
# 4. Build in function

# global: used to change local scope in function to global
counter = 0


def count(counter):
  # global counter
  counter += 1
  return counter


# count()
# count()
# this bellow called dependency injection
print(count(count(count(counter))))


# nonlocal: jump to parrent and get the value, it can be modified in children
def outer():
  x = 'local'

  def inner():
    nonlocal x
    x = 'nonlocal'
    print('inner', x)

  inner()
  print('outer', x)


outer()
# Try to avoid global and nonlocal