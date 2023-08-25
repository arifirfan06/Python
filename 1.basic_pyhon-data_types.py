# Python Data Types
# None
# bool
# int
# float
# complex
# str
# list
# dict
# tuple
# set

# question = input("is this human?")
# print("your answer is " + question +" hehe")

# basic data types
print(type(3 + 3))
print(type(3 / 4))

print(type(10.1 + 1.9))
# code above become float because result of the operation is 12.0

# perpangkatan di python dengan ** cth 3 persegi = 9
print(3**2)

# divided and then rounded to integer
print(9 // 4)

# Modulo
print(6 % 5)

# convert float to integer
print(round(5.531))

# abs remove negative
print(abs(-33))

print((20 - 5) + 2**2)
# operator precedence/priority
# () -> ** -> */ -> +-

# bin() convert into binary
print(bin(3))
# it return 0b11 the binary value is 11

# convert to int be careful with base number 2, 10 etc
print(int('0b11', 2))

# Variables, use snake_case, start lowercase
user_age = 404
true_age = user_age * 9
print(true_age)

# Constant writen in UPPERCASE, machine still allow change of value
USER = "Clementine"
USER = 0
# print(USER)

# assign multi variable
lng, lat = 0.113, 112.332
# print(lng)
# print(lat)

# you cant do this, you can overide python keyword, the blue text are key
# print = 332
# print(print)
# TypeError: 'int' object is not callable

# Here is quick recap related to JS
# the iq /3 is expression because its piece of code that produce value
# the anon_iq = iq / 3 and iq = 100 is statement because its the whole line code
iq = 100
anon_iq = iq / 3

# Augmented Assignment Operator
val1 = 3
# val1 = 7 + val1
# this bellow make sorthand & simple
val1 += 7
print(val1)

# String
text = "zzzz"
# Long multiline String
long_text = ''' HEE 
heee
Wonder
HOY
'''
print(long_text)

# String concat
# print('Hi' + 5)
# you can concat string and string but you cant concat string and other type

# Type Conversion
conv = str(99)
conv_int = int(conv)
print("hey my score is" + conv)
print(type(conv_int))

# Escape Sequences \ to assume the next is a string and use other feature
some_text = "hey it's \"Me\""
some_text2 = "\t Good Morining \n Good Bye!"
print(some_text2)

# Format String / (Template String / Template Literals in JS)
# add f before quotation and add {} in the quotation to put the value
print(f'hmm.. {some_text} okay {some_text2}')

# String Indexes
fish = "tuna salmon"
# print(fish[0])
# print(fish[0:6])
# [start:stop:stepover]
# You can do something like this no value in params above mean default is [0, end of the length, 1]
# print(fish[:3])
# - in array string means reverse
# print(len('01234567'))
# len() counts like human do it start from 1
print(fish[::-1])
print(fish[0:len(fish)])
# Immutability means you cannot change value once its created like this
number = "12345"
# number[0] = "99"
# print(number)
# that result failed, it happen because string is immutable
number = "99" + number[1:]
print(number)