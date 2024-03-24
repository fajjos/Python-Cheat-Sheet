#Optional Parameters -1
# def func(x):          #everything inside this func() bracket is parameter of  the function. 
#     return x**2
# call = func(5)
# print(call)

# def func(x=1):          #creating the optional. 
#     return x**2
# call = func(5)
# print(call)

# def func(word, freq=1):          # here the req is the optional parameter. we dont have to write the optional 
#     print(word*freq)
# call = func('faiz', 10 )

# def func(word, add=5,  freq=1):          # here the req is the optional parameter. we dont have to write the optional 
#     print(word*(freq+add))   
# call = func('faiz', 5, 3 )

# class car(object):
#     def __init__(self, make, model, year, condition='New', kms=0):    #conditions and kms are optional
#         self.make = make
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self.kms = kms
    
#     def display(self, showAll=True):   #showall is an optional parameter
#         if  showAll:
#             print("This car is a %s %s from %s, is is %s and has %s kms." %(self.make, self.model, self.year, self.condition, self.kms ))
#         else:
#             print("This car is a %s %s from %s. " % (self.make, self.model, self.year))
# whip = car('Ford', 'Fusion', 2012)
# whip.display()
#------------------------------------------------------------------------------------------------------------
#Static and Class Methods
# class person(object):
#     population = 50
#     def __init__(self, name, age):
#         self.name  = name
#         self.age   = age
#     @classmethod              #we can call it on the any instinct of the class
#     def getPopulation(cls):
#         return cls.population
#     @staticmethod              #doesnt  depend on the object or instance of the class 
#     def isAdult(age):
#         return age >= 18
#     def display(self):
#         print(self.name, 'is', self.age, 'years old:)))')
# newPerson = person('faiz', 18)
# print(person.getPopulation())
#----------------------------------------------------------------------------------------------------------------
#Map function
#allows us to apply a function to a list  in one line instead of using a loop
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def func(x):
#     return x**x
# # newList = []                 #loop function, well use the map function to do this faster 
# # for x in li:
# #     newList.append(func(x) )
# # print(newList)

# #print(list(map(func, li)))      #map function
# print([func(x) for x in li])     #same as the map function      
#---------------------------------------------------------------------------------------------------------
#Filter Function
# filter function takes two arguments , first argument is the function that we want to apply to each element in the iterable, second argument is the iter.
# def add7(x):
#     return x+7

# def isOdd(x):
#     return x%2 != 0

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = list(filter(isOdd, a))
# c = list(map(add7, b))
# print(a)
# print(b)
# print(c)
#----------------------------------------------------------------------------------------------------------
#Lambda  functions
#Lambda functions are used when we only need small pieces of code that perform a specific task and we don't want to create a full fledged
#A lambda function is a small anonymous function
#Syntax : lambda arguments : expression

# def func(x):
#     return x + 5
# func2 = lambda x: x+5
# print(func2(9))
# print(func(2))


# def func(x):
#     func2 = lambda x: x+5
#     return func2(x) + 85

# func3 = lambda x, y : x+4
# print(func3(5,5))
# print(func(2))


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# newList = list(map(lambda x : x+5, a))
# print(newList)
#- - - - - - - - - - - - - - - - - - - - - ----------------------------------------------------------------------------------
# Introduction to Collections 
 # built in modules in py -> allow us to have diff kinds of data types so that we can store/sort info
#containers- (data type) store multiplre objects #list, set, dict, tuple 
#types- counter, deque, namedTuple(), orderedDict, defaultdict
# import collections
# from collections import Counter
 
# c = Counter('gallad')
# print(c)
# c = Counter(['a', 'a', 'b', 'c', 'c'])
# print(c)
# c = Counter({'a':1, "b":2})
# print(c)
# c = Counter(cats=4, dogs=7)  
# print(c['pet'])
# #print(list(c.elements()))
# print(c.most_common(2))    # returns the most common elements with their counts             

# c = Counter(a=4, b=2, c=0, d=-2)
# d = Counter(['a', 'b', 'b', 'c'])
# # c.subtract(d)
# # print(c)
# # c.update(d)
# # print(c)
# # c.clear()
# # print(c)

# print(c+d)
# print(c-d)
# print(c & d)   #intersection
# print(c | d)   #union
#--------------------------------------------------------------------------------------------------------------
#Named Tuple 
#we can acess things by elements instead of position 
# import collections
# from collections import namedtuple

# Point = namedtuple('Point', {'x' :0, 'y': 0, 'z': 0})
# newP = Point(3, 4, 5)
# print(newP)
# print(newP.x, newP.y, newP.z)
# print(newP._asdict())
#-------------------------------------------------------------------------------------------------------------
#Deque      #faster in adding the elements in the list  to the end and removing them from the start
# import collections
# from  collections import deque
# d = deque("hello")
# print(d)
# d.append('4')
# d.pop()
# d.clear()
# print(d)

# d.extend('456')
# print(d)

# d.extendleft('hey')
# print(d)

# d.rotate(2)
# print(d)

# d = deque("hello", maxlen=5)
# print(d)
# d.append('1')
# print(d)