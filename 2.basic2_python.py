# Build in functions + methods
# quote = "Dont let sleep become your addiction"
# print(quote.upper())

# print(
#   quote.find("sl"))  # find will return the start index of the data it found
# print(quote.replace("your", "my"))

# Boolean (True or False)
# print(bool(""))

# Exercise Type conversion
# fav = input("what is your age number?")  # input() return string

# age = 2023 - int(fav)
# print(f'you was born in {age}')

# Exercise Password Checker
# username = input("Whats your username?")
# password = input("whats the password?")

# concealed_password = '*' * len(password)

# print(
#   f'{username} your password {concealed_password} is {len(password)} too long')

# List (Array in JS)
li = ['a', 'b']
li2 = [1, True, 'v', 99]
nice_list = ['toys', 'books', 'computer', 'foods']

# List Slicing
print(nice_list[0::2])
# List can be mutable and immutable
nice_list[0] = 'drinks'
# you need to add nice_list[:] in code bellow to tell machine create new instead modifying
new_cart = nice_list[:]  # you can also use .copy()
new_cart[0] = 'pets'
print(nice_list)
print(new_cart)

# Matrix / Nested Arrays / Multidimension List or Arrays
mtx = [[1, 4, 1], [3, 2, 5], [2, 7, 1]]
print(mtx[2][1])

# List Methods
bucket = ['fruit', 'milk', 'meat']

bucket.append('juice')  # Add data in the end of list
bucket.insert(1, 'rice')  # Add data in specific index
bucket.extend([101, 999])  # Add value and loop/iterate data

# remove
bucket.pop(
)  # remove the last item or specified index in param, pop() return a value you can try this on store variable
bucket.remove('fruit')  # remove the value from param
# clear() remove all items, it make the data [] / empty it doesnt return anything

# store = bucket.append('juice') you cant do this. this doesnt return value
store = bucket.pop(3)
print(bucket)
# print(store)

print(bucket.index('milk', 0, 3))  # Find index based on value

# Keywords
print('book' in bucket)  # this find in data, you can use it in string
# count() will count how many times data from the params appears
bucket.pop()
bucket.sort()  # sort the data and sorted() produce & return new value
bucket.reverse()  # .reverse() is reversing the array not the opposite of sort
print(bucket)

# Common List Pattern
# print(list(range(100)))  # range() create data according the params

new_sen = ' ! '.join(['hey', 'you!', 'yes'])  # add string between item
print(new_sen)

# List unpacking
a, b, c, *others, z = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(others)

# None / null in js
weapons = None

# Dictionary / dict / object in js
# dict is unordered in memory so I cant call [0], [1] etc

books = {
'avail': False,
  'price': 21,
  'name': 'Nice'
}

print(books['name'])

# dict keys
booksx = {
'avail': False,
  'price': 21,
  'name': 'Nice',
  True: False,
  100: 'decent',
  # ['open']: 7 # dict keys must me immutable and array can be mutable so dont assign list in dict key
}
# print(booksx['open'])

# Dictionary Methods
# print(booksx['vue']) # this will result error
print(booksx.get('vue', 'python')) # .get() first param is the key to find, the second is the default return falue if the key is not found
uncommon = dict(books= 99) # uncommon way creating dict
print(uncommon)

print(21 in booksx.values()) # you can also use .items() do do iterate or loop
# you can use .copy(), pop(key) and .clear(). popitem() remove last item
# update() first param is the key and default value. it update value if key found and add if no simmilar key
booksx.update({101: 'ok'})
print(booksx)

# Tuples / same with list but Immutable
x, y, z, *others = (1,4,2,5,1,9)

user = {
  'password': None,
  (1,2): [1,2,3,4]
}

print(user[(1,2)])
print(x,y)

# set is unordered collection of unique object
set1 = {1,2,3,4,5}
set2 ={4,5,6,7,8}
set3 ={4,5}
list1 = [1,2,2,4, 7,1]
print(set(list1)) # remove duplicate you can convert set to list with list()

# Set Methods
# print(set1.difference(set2)) # find and keep the difference
# print(set1)
# print(set1.discard(4)) # remove data based on value
# print(set1.difference_update(set2)) # change data in mutable way
# print(set1)
# print(set1.intersection(set2)) # find same things in datas
# shortcut to intersection is set1 & set2
# print(set1.isdisjoint(set2)) # if no same data return true
# print(set1.union(set2)) # unite sets and remove duplicate
# shortcut to union is set1 | set2
# print(set3.issubset(set2)) # find if data is completely included in the parrent
print(set2.issuperset(set3))
