# OOP
from typing import Any


class Vigger: #Class, the naming convention should be camelcase, use capitalize on the first
    pass

obj1 = Vigger() # Instanciate

class PlayerStat: # usually singular
    membership = True # this is class obj attribute / static
    def __init__(self, name = 'unknown', age=0): # special method / constructor method, automatically run/called when creating new obj, you can add default
        if(age > 18): # access class variable with self
            self.name = name # attribute(dynamic) self is way to define object/data, make reference after . (dot)
            self.age = age
    def run(self, speed): # must add self after define function, the next can be params
        print('run')
        return f'done in {speed}'
    def greet(self): # Encapsulation
        return f'I\'m {self.name}'
    @classmethod #decorator. this classmethod can be used without instanciate class
    def calc(cls ,num1, num2): # cls refer to class(PlayerStat)
        return cls('Loci',num1 * num2) # we can use cls same as we instanciate oject PlayerStat('Gerald', 27)
    @staticmethod
    def calc2(num1, num2): # unlike classmethod the static method doesnt have access to cls
        return num1 * num2

p1 = PlayerStat('Gerald', 27) # Instanciate/create new obj
# p2 = PlayerStat() # need extact params
# each varibale p1 and p2 have different place in memory
p1.attack = 70 # with self you can assign dynamic variable
print(p1.name, p1.age, p1.run(277), p1.greet())
# print(p2.greet()) # this is static and apply to all players
print(PlayerStat.calc(5, 99))
p3 = PlayerStat.calc(3,59)
print(p3.name, p3.age)
p9 = {"name": "Eliot Gindy", "age": 32} # the real difference between this dict and OOP is the way we access it
print(p9['name']) # in dict we didnt use . dot, we use the var then [] and the key string inside of the square bracket
print(p1.greet()) # Abstraction, we can execute function without knowing how its written
# this 2 lines bellow are bad practice
# p1.greet = False
# p1.name = ''

# The Pillars of OOP in Phyton:
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism

# Private variable in Python
# we add _ on variable to make other devs know its private and not be overiden
class OverPower:
    def __init__(self, name, power) -> None:
        self._name = name
        self._power = power
    def stats(self):
        return f'{self._name} is very powerful, its over {self._power}'

op1 = OverPower('Demn', 9000)
# print(op1.stats())

class SimpleCls: # if we dont have variable to be assigned in the class we dont need __init__
    def __init__(self, email) -> None:
        # print('test')
        self.email = email
    def greet(self):
        print('Hello')
    def attack(self): # this will get overide by the child/subclass by default
        print('attacking...')
# Inheritance, we can pass parent class
class Wizard(SimpleCls):
    def __init__(self, name, power) -> None:
        # print('test2') # if init declared here then only run in subclass
        # SimpleCls.__init__(self, email) # solution without using super()
        # super().__init__(email)
        self._name = name
        self._power = power
    def attack(self):
        SimpleCls.attack(self)
        print(f'{self._name} has attack of {self._power}')

wiz1 = Wizard('Roger', 322)
# wiz1.greet()
# wiz1.attack()

class Archer(SimpleCls):
    def __init__(self, name, arrows) -> None:
        self._name = name
        self._arrows = arrows
    def attackArr(self):
        print(f'{self._name} Arrows can deals {self._arrows} damage')

arc1 = Archer('Warren', 99)
def strike(char):
    char.attack()

# Polymorphism, the same function output diffeent things
# strike(wiz1)
# strike(arc1)

# print(wiz1.email)

# Introspection
# print(dir(wiz1)) # with dir we got info about object and its available methods

# Dunder Methods
# __str__. __init__ , etc are dunder methods, __str__ and str() are the same. its better not modify dunder methods
class Dunder:
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type
        self.combine = {
            'name': name,
            'type': type,
            'num': 5
        }
    def __str__(self): # this will overide str() methods 
        return f'Hey{self.type}'
    def __call__(self) -> Any: # this triggered when we declare () after the instanciated variable i.e: dnd1()
        return 'worked'
    def __getitem__(self, i):
        return self.combine[i]

dnd1 = Dunder('fire', 'power')
# print(str(dnd1))
# print(dnd1())
# print(dnd1['type']) # this is the use of __getitem__ in class python

# Exercise
class SuperList(list): # we can inherit from data types such as list
    def __len__(self) -> int:
        return 1000
    

sup1 = SuperList()
# print(len(sup1))
# sup1.append(9)
# print(sup1[0])
# print(issubclass(list, object)) # everything in python is object

# Multiple Inheritance, some ppl dont allow multi inheritance
class Knight(Wizard, Archer): # this will priority Wizard first
    def __init__(self, name, power, arrows) -> None:
        Archer.__init__(self,name, arrows)
        Wizard.__init__(self,name, power)
knight1 = Knight('Alex', 30, 70)
# knight1.greet()
# print(knight1.attack())

#MRO Method Resolution Order
class A:
    num = 10

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro()) # return the priority order
D.num