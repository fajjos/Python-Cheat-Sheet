# Basic Data Types
#  int 0
#  str 'Faiz' 'Hello'
# bool 'true' 'false'
# float 0.322 0.55 1.65

# #Variable Names:
# name = 'FAiz'   #Cannot start with number, underscore, 
# print(name) 
# age = 23
# print(age)

# name = 'faiz '
# print("Name is : ", end="")
# print(name)

# print('Hello, what is your name?')
# name = input()
# print('Hello My name is:', name)

# # Arithmetic Operators + (add)-(sub) *(mul) /(div)
# num1 = 45
# num2 = 78
# print("Addition of num1 and num2 is", num1+num2)
# print("Subtraction of num1 from num 2 is", num2-num1)
# print("Multiplication of num1 and num2 is", num1*num2)
# print("Division of num1 by num 2 is", num1/num2)

# ** -> exponenents
# // -> entity division 
# %  -> modulus or remainder division 5%2 = 1

# num1 = 45
# num2 = 3 
# num3 = num1**num2
# print("Exponential of num1 to the power of num2 is", num3)

# num1 = 45
# num2 = 3 
# num3 = num1//num2
# print("Entity div of num1 to the num2 is", num3)

# print('pick a number:')
# num1 = input()
# print('Pick  another number:')
# num2 = input()
# print(type(num2))
# SUM = int(num1) + int(num2)
# print(SUM)

# CONDITIONS
# faiz = khan False
# 18 > 2 True
# < -> less than 
# > -> ,more than 
# ==  -> equal sign 
# != -> not equal to  
# <= -> less than or equal to  
# >= -> more than or equal to 

# print(2 > 3)
# print('Hello'== 'Helo')
# print('Hello'!= 'Helo')
# print('hello'== 'Hello')

# print (2< 3)
# print(2-3+4 > 5)
# print(False == True)

#IF-ELSE & ELSE-IF Statements 

# age = input('Input your age: ')
# if int(age)== 16:
#     print (' Hey, youre 16 kiddo ') 

# age = input('Input your age: ')
# if int(age)> 16:
#     print (' Hey, youre more than 16 now kiddo ') 

# age = input('Input your age: ')
# if int(age)>= 16:
#     print (' Hey, youre 16 or more than  kiddo ')

# age = input('Input your age: ')
# if int(age)>= 16:
#      print (' Hey, youre 16 or more than  kiddo ')
# else:
#      print('you are younger than 16 kiddo :)') 

# height = input( )
# if int(height)< 1:
#     print( "Your height is too small, you cannot ride, under 1M" )
# elif int(height)>= 2:          # we can have multiple elif statements but only one if and else statements 
#     print('You cannot ride, over 2M')
# elif int(height) == 5:
#     print('wow, youre tall buddy ')
# else:
#     print( "You can ride the rollercoaster, big hooman:)")

#----------------------------------------------------------------------------------------------------------------------------
# Chained Conditionals and Nested Statements 
# chained conditions -> adding multiple conditions in one line 
# and or not 
# x= 2
# y =3
# if y == 3 and x + y == 5: # and condition basically means both conditions of each side must be true.
#     print('ran')

# x= 2
# y =3
# if y == x or x + y == 5: # or condition basically means either of the conditions have to be true.
#     print('ran')
# else:
#     print(':(')

# x= 2
# y =3
# if not (y == x or x + y == 5): # not condition basically reverses the conditions inside the bracket of the not().
#     print('ran')
# else:
#     print(':(')
#-----------------------------------------------------------------------------------------------------------------------------------
# Nested   statements:
# x= 4
# y=4 
# if x== 2:
#     if y==3:                       
#         print('x=2, y = 3')
#     else:
#         print('x=2, y != 3')
# else:
#     print('x != 2')

# for Loops
# for x in range(0, 10, 5):  # this will loop from 0-9 with a start, stop, step  { ( x = x + 1)
#     print(x)

#-----------------------------------------------------------------------------------------------------------------------------
# while loops
# while condition == True:
#     do this
#     break

# loop = True 
# while loop:
#     password = input('Insert  your password: ')
#     if password == 'python':
#         print('Access granted!')
#         loop = False
#         break     #get us out of the loop
#--------------------------------------------------------------------------------------------------------------------------------
# #LIST []  are used to store multiple values in one variable(data types)

# fruits = ['apple', 'pear', 3]   #everything seperated by comma is calld item.
# print(fruits)   
# fruits.append('StrawBerry' )     #.append('') basically adds a new item in the list 
# print(fruits)

# fruits = ['apple', 'pear', 'strawberry ']
# fruits[1] = 'Blueberry'
# print(fruits)

#TUPLES  used  when we need data that won’t change. They are similar to lists but they can not be changed once created.

# fruits = ['apple', 'pear', 'Strawberry']
# position = (2, 3)
# color = (255, 255, 255)
# print(type(color))
#------------------------------------------------------------------------------------------------------------------------------------
# Iteration By Item 

# fruits = ['apple','pear','Strawberry', 8, 90 ]
# for fruit in fruits:
#     print(fruit)

# fruits = ['apple','pear','Strawberry', 8, 90, 88 ]
# for fruit in fruits:
#     if fruit == 'pear':
#         print(fruit)
#     else:
#         print('not pear')

# for x in range(0, 6):
#     if fruits[x] == 'pear':
#         print(fruits[x])
#     else:
#         print('Not Pears')
#----------------------------------------------------------------------------------------------------------------------------------
# String Methods
# .strip(), len(), .lower(), .upper(), .split()

# text = input('Input Something: ')
# print(text.strip())    #strip -> remove all the white spaces before and after the  text

# text = input('Input Something: ')
# print(len(text))       # len() returns the length of the string or the list.  

# text = input('Input Something: ')
# print(text.lower())     # turn everything into lower cases 

# text = input('Input Something: ')
# print(text.upper())    # turns everything into upper cases   

# text = input('Input Something: ')
# print(text.split('.'))  #get rid of the limitor
#----------------------------------------------------------------------------------------------------------------------------------
# #SLICE OPERATOR
# fruits = ['apple', 'pineapple', 'pear']
# text = 'Hello, I like Python'
# fruits[3:3] = 'b'
# print(fruits)
#-------------------------------------------------------------------------------------------------------------------------------
# #FUNCTIONS
# def addTwo (x):
#     return (x + 2)**2
# def subtractTwo (number):
#     return number -2
# newNumber = addTwo(7)
# print(newNumber)
# subtractNumber = subtractTwo(10)
# print(subtractNumber)

# #How to read from a text file 
# file = open('file.txt', 'r')
# f =  file.readlines()
# newList = []
# for line in f:
#     newList.append(line[:-1])

# print(newList)

# file = open('file.txt', 'r')
# f =  file.readlines()
# newList = []
# for line in f:
#     newList.append(line.strip())
# print(newList)

# #Writing to a text file
# file = open("file.txt", "w")
# file.write('yolooooo\n')
# file.write('I am learning \n how to write to a file ')
# file.close()

#using .count() and .find()
# string = 'hello'
# # print(string.find('h'))
# print(string.count('h'))

# Introduction to Modular Programming 
# import math
# import pygame
# import os

# import math
# import myModule
# # print(math.degrees(math.pi))
# print(math.radians(60))
# print(myModule.anotherFunc(6))

# # OPTIONAL PARAMETERS
# def func(x, text='2'):
#     print(x)
#     if text == '1':
#         print('Text is 1')
#     else:
#         print('Text is not 1')
# func('faiz')

# TRY and EXCEPT (Error handling)
# text = input('Username: ')
# try:
#     number = int(text)
#     print(number)
# except:
#     print('invalid username') 

#Global VS Local variable
#global: can  be accessed anywhere in the program
#local : only accessible inside of its function or block where it was defined

# #local variables
# var = 9
# loop = True

# def func(x):
#     newVar = 7
#     print(newVar)
#     if x==5:
#         return newVar
# func('2')

# global variables
# var = 9              #global variable
# loop = True          #global variable

# def func(x):
#     newVar = 7
#     print(var)
#     if x==5:
#         return newVar
# func('2')


