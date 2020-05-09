# birth_year = input("What is your Birth Year? ")
# # color = input("What is your favourite colour? ")
# print(type(birth_year))
# age = 2020 - int(birth_year)
# print(type(age))
# print(age)

# weight = input("What is your weight ")
#
# convert_weight = int(weight) * 1000
# print_data = "Your weight is " + str(convert_weight) + " grams"
# print(print_data)

# data = 'shubham dave'
#
# print(data[-1:0])
# Formatted string (06/03/2020)

# first = 'Shubham'
# last = 'Dave'
#
# msg = f'{first} [{last}] is a developer'
#
# print (msg)

# String Methods

# course = "Shubham dave is my name"
# print (len(course))
# print(course.upper())
# print(course)
# print(course.lower())
# print(course.find('n'))
# print(course.replace('name', 'pet name'))
# print(course.title())
# print('Shubham' in course)

# Arithmetic operator
# x = 20
# x *= 2
# print(x)

# Operator Precedence
# x = 10 + 2 * 3
# print(x)
# precedence
# parenthesis -> (a -b)
# exponential -> 2 ** 3
# multiplication or division -> a/b or a*b
# addition or substraction -> a+b  or a-b

# math module ke baare me padhna hai python ke site se
# if else statement case

# is_hot = False
# is_cold = False

# data = input("what type of day it is")
# if 'hot' in data:
#     is_hot = True
#     is_cold = False
# elif "cold" in data:
#     is_hot = False
#     is_cold = True
# else:
#     is_hot = False
#     is_cold = False
#
# if is_hot:
#     print("Its a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("Its a cold day")
#     print("Wear hot clothes")
# else:
#     print("Its a Lovely day")

# price = 1000000
# good_credit = False
#
# if good_credit:
#     msg = f'Amount to be paid = ${(price *10 / 100)}'
#     # print(msg)
# else:
#     msg = f'Amount to be paid = ${(price * 20 / 100)}'
#
# print(msg)

# Logical OPerators

# has_high_income = True
# has_good_credit = False

# if has_good_credit and has_high_income:
#     print('loan can be granted')
# elif has_high_income and not not not has_good_credit:
#     print('half loan can be granted')
# else:
#     print("loan can't be granted")
# and
# or
# not

# Comparison Operator
# name = input("write your name here ")
#
# if len(name) < 3:
#     print("name length should be greater than 3 char")
# elif len(name) > 50:
#     print("name length should be lesser than 50 char")
# else:
#     print("name looks good")

# Weight Convertor Program

# weight = input("Weight: ")
# weight_value = input("(K)g or (G)rams: ")
# print(weight_value)
# print(bool('k' in weight_value))
# if weight_value.upper() == 'K':
#     data = int(weight) * 1000
#     print(f'You are {data} grams')
# elif weight_value.upper() == 'G':
#     data = int(weight) / 1000
#     print(f'You are {data} kilograms')
# else:
#     print(f'Please put data correctly')
# print(msg)

# date 10/03/2020
# While Loops

# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1
# print("done")

# Guess Game

# guess_number = 17
#
# user_number = 0
# user_limit = 3
#
# while user_number < user_limit:
#     user_guess_number = int(input('Guess: '))
#     user_number += 1
#     if user_guess_number == guess_number:
#         print('You won!')
#         break
# else:
#     print('you failed!')

# Car Game

# data = input(">")
# # print(data.upper())
# if data.lower() == 'help':
#     print("""
#     start - to start the car
#     stop - to stop the car
#     quit - to exit
#     """)
# elif data.lower() == "start":
#     print('car started... ready to go')
# elif data.lower() == "stop":
#     print('car stopped.')
# elif data.lower() == "quit":
#     print("quited")
# else:
#     print('i can not understand')

# command = ""
# start = False
# # stop = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#
#         if start:
#             print("car is already started what are you doing")
#         else:
#             start = True
#             print("Car Started!")
#     elif command == "stop":
#         if not start:
#             print("car is already Stopped what are you doing")
#         else:
#             start = False
#             print("Car Stopped!")
#     elif command == "help":
#         print("""
# start - to start the car
# stop  - to stop the car
# quit  - to quit the game
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand that")
# # else:
# #     print("quited")

# for item in 'Python':
#     print(item)
# for item in range(8, 81, 8):
#     print(item)
# prices = [10, 20, 30]
# total = 0
# for item in prices:
#     total += item
# print(f"Total: {total}")

# for x in range(4):
#     for y in range(3):
#         if x == y:
#             print(f"when data is same")
#             print(f"({x} , {y})")
#         else:
#             print(f"when data is not same")
#             print(f"({x}, {y})")

# challenge

# numbers = [5, 2, 5, 2, 2]
#
# for item in numbers:
#     # print('X' * item)
#     output = ''
#     for i in range(item):
#         output += 'F'
#     print(output)

# Lists Tutorials
# to find largest number in list
# listData = [2, 3, 17, 5, 10]
#
# # for data in range(len(listData)):
# largest = listData[0]
# for data in listData:
#     # data = int(data)
#     # print(type(data))
#     # value_1 = data
#     if data > largest:
#         largest = data
#     # elif largest > data:
#     #     largest = data
# print(largest)

# # 2d lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# matrix[1][1] = 17
# for row in matrix:
#     for column in row:
#         print(column)
# print(matrix)

#    # List methods
# numbers = [1, 5, 2, 7, 4, 1]
# new_numbers = []
# numbers.append(20)
# numbers.insert(0, 25)
# numbers.remove(5)
# numbers.clear()
# numbers.pop()

# print(7 in numbers)
# print(numbers.index(1))
# number2 = numbers.copy()
# number2.sort()
# numbers.reverse()
# print(f'''
# Real Value: {numbers}
# New Value : {number2}
# ''')
# for item in numbers:
#     if item not in new_numbers:
#         new_numbers.append(item)
# print(new_numbers)

# # Tupels:
# numbers = (1, 2, 3)
# numbers[0] = 1
# print(numbers[0])

# x, y, z = numbers
# numbers.__contains__()
# print(numbers.__add__())

# # Dictonary

# customer = {
#     "name" : "Shubham Dave",
#     'age' : '20',
#     "mail" : 'shubham.dave@gmail.com'
# }
# customer["name"] = "shivang dave"
# print(customer.get("birthdarte", "01 Aug 1996"))

# character = input("Write number here to see in alphabets")
# number_mapping = {
#     "1" : "one",
#     "2" : "two",
#     "3" : "three",
#     "4" : "four",
#     "5" : "five",
#     "6" : "six",
#     "7" : "seven",
#     "8" : 'eight',
#     "9" : "nine"
# }
# output = ""
# for ch in character:
#     output += number_mapping.get(ch, "!") + " "
# print(output)

# # Emojis Function
# message = input(">")
# words = message.split(' ')
# # print(words)
# emojis = {
#     ":)" : "😀",
#     ":(" : "😥",
#     ";)" : "😎"
#  }
# output = ""
#
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# # Function in python
#
#
# def greet_user():
#     print("hey there")
#     print("welcome to group")
#
#
# print("Start")
# greet_user()
# print("End")
# # function using keyword argument and positional argument

#
# def greet_user(first_name, last_name):
#     print(f"hey {first_name} {last_name}")
#     print("welcome to group")
#
#
# print("Start")
# greet_user("shubham", last_name="dave")
# print("End")

# # Return statement
#
#
# def square(num):
#     return num * num
#
#
# def cube(number):
#     return number * square(number)
#
#
# print(cube(10))

# # Reusable Function


# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)" : "😀",
#         ":(" : "😥",
#         ";)" : "😎"
#      }
#     output = ""
#
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input("=>")
#
# print(emoji_converter(message))

# # Debugging

# try:
#     age = int(input('Age: '))
#     print(age)
#     income = 20000
#     risk = income/age
#     print(risk)
# except ZeroDivisionError:
#     print("Age cannot be 0.")
# except ValueError:
#     print("Invalid Input")

# # Comment
# # Do not use for what always why and how


# # Classes

# class Points:
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Points()
# point1.x = 1
# point1.y = 2
# print(point1.x)
# print(point1.y)
#
# point1.move()
# point1.draw()
#
# point2 = Points()
# point2.move()
# point2.draw()

# # Constructor
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def draw(self, x, y):
#         print(f"Draw {x,y}")
#
#     def move(self, x, y):
#         print(f"Move {x,y}")
#
#
# point = Point(10, 20)
# print(f"({point.x}, {point.y})")
# point.draw(5, 7)
# point.move(15, 20)

# # Question

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f"Hello I am {self.name}")
#
#     def talk(self):
#         print(f"Hi I am {self.name}")
#
#
# person = Person("Shubham dave")
# person.talk()
#
#
# ashu = Person("Ashutosh Dave")
# ashu.talk()

# num = (input("=>"))
#
# data = num.split(",")
#
# total_no_peaks = 0
# base_value = int(data[0])
# for value in data:
#     value = int(value)
#     new_value = value
#     if value > base_value:
#         base_value = value
#         if base_value <= new_value:
#             print(value, base_value, new_value)
#             total_no_peaks = total_no_peaks + 1
# print(total_no_peaks)

# # Code Jam Question
# base = int(input())
#
#
# def total_no(args):
#     return print(args)
#
#
# # num = int(input("=>"))
#
# # data = num.split(",")
# total_no_peaks = 0
#
#
# def cal_data(value):
#     # data = input()
#
#     # for i in range(0, data):
#
#     peak = input()
#     peak_value = peak.split()
#     print(peak_value)
#     base_value = int(peak_value[0])
#     for i in peak_value:
#         i = int(i)
#         if i > base_value:
#             base_value = i
#             # total_no += 1
#             total_no(1)
#             # print(total_no)
#         elif i < base_value:
#             i = i
#
#
# # print(total_no)
#
# for i in range(0, base):
#     cal_data(i)


# # Inheritance
#
# class Mammal:
#     def walk(self, name):
#         print(f"{name} walk")
#
#
# class Dog(Mammal):
#     def bark(self, name):
#         print(f"{name} bark")
#
#
# class Cat(Mammal):
#     def meow(self, name):
#         print(f"{name} meow")
#
#
# dog1 = Dog()
# dog1.walk("dog")
# dog1.bark("dog")
#
# cat1 = Cat()
# cat1.walk("pussy")
# cat1.meow("pussy")
# # Modules

# from convertor import find_max
#
# value = input("Input value to find max => ")
#
# print(find_max(value))

# # Packages

# from ecommerece import shipping
#
# shipping.cal_shipping()
# shipping.cal_tax()

# # System Module
import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
# print(f"({dice.roll()}, {dice.roll()})")
print(dice.roll())
# video 03:44:00 tak hua

