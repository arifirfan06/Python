# If conditional

license = False
is_exp = False

# you can use space 4 times to create indentation like if statement bellow
if license & is_exp:
  print('You are now a driver')
elif is_exp:
  print('please renew your license')
else:
  print('bye!')

# Ternary Operator (const message = friend ? 'yes' : 'no' in JS)
is_driving = "yes" if license else "get your license"
print(is_driving)

# and if all is true, or if one of them is true

# Short Circuiting
# in conditional, machine will check the first condition and might not execute other!.
# if if license(false) & is_exp: in this case is_exp wont be evaluated
# if if license(true) or is_exp: in this case is_exp wont be evaluated

is_developer = True
is_expert = False

if is_developer and is_expert:
  print('Wow 2-digit salary!')
  # not bellow simmilar to !
if is_developer and not is_expert:
  print('keep learning')
else:
  print('you need skill!')

# Comparasion == is equal of value.
# print(True == 1) # converted to boolean bool(1)
# print('' == 1) # python wont do data type conversion if its '1', '938',etc
# print([] == 1)
# print(10 == 10.0)
# print([] == [])

# # is Comparasion 'is' is a comparasion of data type and value that must be same in memory where it stored such as 101110011
# # is more strict than ==
# print('this is \'is\' statement')
# print(True is True)
# print('1' is '1')
# print([] is []) # list is quite tricky because its always stored in diferent place in memory its also same as dict, tuples, set
# print(10 is 10.0)
# print([] is [])

# For Loop
# for item in 'learning':
#   print(item)

# for item in [3,2,1]: #you can do this in tuples, sets
#   print(item)
# print(item) # the last value of the loop get returned

# # you can do nested loop as well
# for item in [1,2,3,4]:
#   for x in 'abc':
#     print(item, x)

# Iterable can be used in list, dict, tuples, string, set
# Here is how to do that in dict/object
user = {"name": 'Willy', "age": 22, "fav": False}

for item in user.items(
):  # if you just declare user it only pick key, but with user.items() you get key value pair that often used. .value() to get value. .keys() for keys
  key, value = item  # to get the key, value pair. it can be named anything
  print(key, value)

for key_item, value_item in user.items():
  print(key_item, value_item)

counter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0

for item in counter:
  count = count + item
print(count)

# Loop in range()
# for i in range(0,100):
#   print(i)
for i in range(
    12, 0, -2
):  # to do in reverse you need to add -number in third params, and put the correct starting number in first param and end number in second param
  print(i)

# enumerate() in loop give us key value pair in iterable data
# for key, value in enumerate('master'):
#   print(key, value)

# for key, value in enumerate([2,1,3]):
#   print(key, value)

for key, value in enumerate(list(range(100))):
  if (value == 50):
    print(f'here is what you want {key}')

# While Loop is conditional loop. it can cause infinite loop if the condition always true. break statement can be used to avoid this, it stop once python reads break in loop.
i = 0
while i < 7:
  print(i)
  i += 1
  # break
else:
  print('done')

# For loop is simpler but while can do lot many things
data1 = [1, 2, 3]
i2 = 0
# be sure to place code correctly dont put print bellow increment to avoid index not found
while i2 < len(data1):
  print(data1[i2])
  i2 += 1

# This is very useful while loop
# while True:
#   resp = input("nickname:")
#   if (resp == "avx"):
#     break

# break can be used in for loop. continue can be used in for & while
# continue is used to go back to evaluate iterate condition and the upcoming code wont be executed
for item_data1 in data1:
  continue
  print("x")

# pass is not that useful, it pass code in iteration so you can write comment in loop

for item_data1 in data1:
  # thinking .......
  pass

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]

for img in picture:
  for item in img:
    if (item == 0):
      print(' ', end='')
    if (item == 1):
      print('*', end='')
  print('')

duplicated_data = ['1', '2', '6', '3', '1', '3']

duplicated_found = []

# for item in duplicated_data:
#   for num in item:
#     if (num == item):
#       print('x')

for item in duplicated_data:
  if (duplicated_data.count(item) > 1):
    if (item not in duplicated_found):
      duplicated_found.append(item)

print(duplicated_found)
