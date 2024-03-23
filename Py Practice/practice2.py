#objects and classes 
# x=5          # 5 is the instinct of the int class
# y='string'     # 'string' is the instinct of the str class

# print(type(x))
# print(type(y))

# import turtle
# x= 5
# y= 'string'
# faiz = turtle.Turtle()       #faiz is the new instinct of this turtle object

# print(y.replace('s', ''))

# def func(x):
#     return x + 1

# print(func(5))
#------------------------------------------------------------------------------------------------------------
# #creating owr own classes and objects 
# class Dog(object):
#     def __init__(self, name, age, weight):     #__init__ -> known as instructor method  or constructor in python
#         self.name = name            #attributes of a class
#         self.age = age              #attributes of a class
#         #pass
#        # print('Nice You made a Dog!! ')
#     def speak(self):                           # methods-> which have these def  inside them are called as instance methods
#         #pass
#         print('Hi i am', self.name, 'and i am ', self.age, 'years old', 'and my weight is :', self.weight)
#        # print('Hi my age is :', self.age)
#     def change_age(self, age):
#         self.age = age  
#     def add_weight(self, weight):
#         self.weight = weight
# # dog1name = 'faiz'
# # dog1age = 3

# faiz = Dog('Faiz', 23, 75)   # creating an instance/object of the class dog with the name Faiz
# faiz.change_age(0)
# #faiz.add_weight(75)
# #print(faiz.name)      #
# fred = Dog('Fred', 6, 3)

# faiz.speak()
# fred.speak()

# print(faiz.age)
#-----------------------------------------------------------------------------------------------------------------------
#INHERITANCE
# class Dog(object):
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         print('Hi i am', self.name, 'and i am ', self.age, 'years old')
#     def talk(self):
#         print('bark!!!')
# class Cat(Dog):               #Cat inherits from Dog, Dog is the parent class  or superclass and cat is the subclass, or child class
#     #  def __init__(self, name,age, color):
#     #     self.name = name
#     #     self.age = age 
#     #     self.color = color
#     #  def speak(self):
#     #     print('Hi i am', self.name, 'and i am ', self.age, 'years old')
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#     def talk(self):          #here we are overriding the talk 
#         print('meow!!!!')

# tim = Dog('Tim',4,)
# tim.talk()
# faiz = Cat('Faiz', 4, 'Black')
# #faiz.speak()
# faiz.talk()                 


# class vehichle():
#     def __init__(self, price, gas, color):
#         self.price = price
#         self.gas = gas
#         self.color= color

#     def fillUpTank(self):
#         self.gas = 100
#     def emptyTank(self):
#         self.gas = 0
#     def gasLeft(self):
#         return self.gas

# class Car(vehichle):
#     def __init__(self, price, gas, color, speed):
#         super().__init__(price, gas, color)
#         self.speed = speed

#     def deep(self):
#         print('beep beeeeep')

# class Truck(vehichle):
#     def __init__(self, price, gas, color, tires):
#         super().__init__(price, gas, color)
#         self.tires = tires

#     def deep(self):
#         print('Honk honkkk')
#--------------------------------------------------------------------------------------------------------------------
# # Overloading Methods
# class Point():
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y  = y
#         self.coords = (self.x, self.y)
#     def move(self, x, y):
#         self.x += x
#         self.y += y
#     def __add__(self, p):
#      return Point(self.x + p.x, self.y + p.y)

#     def __subtract__(self, p):
#      return Point(self.x - p.x, self.y - p.y)
    
#     def __mul__(self, p):
#      return self.x * p.x + self.y * p.y
     
# p1 = Point(3, 4)
# p2 = Point(3, 2)
# p3 = Point(1, 3)
# p4 = Point(0, 1)
# p5 = p1   + p2
# #p6 = p4 - p1
# p7 = p2*p3

# print(p5, p7)
#--------------------------------------------------------------------------------------------------------------
# # Static Methods and Class Methods
# class Dog:
#     dogs = []                           #class variable , we can call class variable anywhere in our methods


#     def __init__(self, name):
#         self.name = name
#         self.dogs.append(self)
    
#     @classmethod                        #called as decorators, put these above the class method
#     def num_dogs(cls):                  # cls -> is the name of the class 
#         return len(cls.dogs)
    
#     @staticmethod                       #also called decorators, put these above the static method
#     def bark(n):
#         """barks n times"""
#         for _ in range(n):
#             print("Barkkk!")

# # faiz = Dog("Faiz")                    #calling class variable
# # Jim = Dog('Jim')                      #calling class variable
# # print(faiz.dogs)                      #calling class variable

# # faiz = Dog("faiz")                    # calling @classmethod
# # print(faiz.num_dogs())                # calling @classmethod


# Dog.bark(7)                             # calling @staticmethod
#--------------------------------------------------------------------------------------------------------------
#Public And Private Classes
# class _Private:                             #private classes-> theyre used typically in the same file  where defined
#     def __init__(self, name):               # put a _ before the class name for showing that this one is private 
#         self.name = name

# class NotPrivate:
#     def __init__(self, name):
#         self.name = name
#         self.priv = _Private(name)
    
#     def _display(self):
#         print("hola")
    
#     def display(self):
#         print("adios")