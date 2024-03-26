# #how the codes gets compiles  and run in py 
# class Dog:
#     def __init__(self):
#         self.bark()

# def make_class(x):
#     class Dog:
#         def __init__(self, name):
#             self.name = name

#         def print_value(self):
#             print(x)
        
#     return Dog
# cls = make_class(10)
# print(cls)

# for i in range(10):
#     def show():
#         print(i*2)
#     show()

#everything in py happens live
#py store in memory

# import inspect

# x = [1,2,3]
# y= [3,4,5]

# print(x*5)

#meta Classes
# def hello():
#     class hi:
#         pass
#     return hi
# hi()

# class test:
#     pass
# print(type(test()))

#Decorators
#they allow us modifying the behavior of the func without changing the whole code 

# def func(f):
#     def wrapper():
#         print('started')
#         f()
#         print('ended')

#     return wrapper
# def func2():
#     print("i am func2")
# def func3():
#     print('i am func3')
# x = func(func3)
# y = func(func2)
# print(x)
# x()
# y()

# def func(f):
#     def wrapper(*args, **kwargs):
#         print('started')
#         rv = f(*args, **kwargs)
#         print('ended')
#         return rv 

#     return wrapper
# @func
# def func2(x , y):
#     print(x)
# @func
# def func3():
#     print('i am func3')

# func3()
# x = func2(5, 6)
# print(x)

# # Generators
# x = [i**2 for i in range(10000000000)]

# for el in x: 
#     print(el)               #this code will fill up all the memory so we use the generators  to avoid this problem.

# class Gen:
#     def __init__(self, n):
#         self.n = n
#         self.last = 0
#     def __next__(self):
#         return self.next()
#     def next(self):
#         if self.last == self.n:
#             raise StopIteration()
        
#         rv = self.last ** 2
#         self.last += 1
#         return rv 
# g = Gen(10000000)
# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break

#Context managers
file = open ("test.txt", "r")
file.write('hello')