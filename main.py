# Arithmetic & maths

# x = 3.14
# y = 4
# z = 5

# result = round(x) # 3
# result = abs(y) # if y = -4 output will be 4
# result = pow(4,3) # 64
# result = max(x, y, z) # 5
# result = min(x, y, z) # 3.14

# ------------Math Operations---------------------------------------------------

# import math

# x = 9.9

# print(math.pi)
# print(math.e)
# result = math.sqrt(x) # if x = 9 output will be 3.0
# result = math.ceil(x) # if x = 9.1 output will be 10
# result = math.floor(x) # if x = 9.9 output will be 9

# -------------Logical operators---------------------------------------------

"""logical operators = evaluate multiple conditions (or, and, not)
                        or = at least one condition must be True
                        and = both conditions must be True
                        not = inverts the condition (not False, not True)"""
from traceback import print_tb

# from example import square

"""--------------------or-----------------------"""
# temp = 20
# is_raining = True
#
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is ok")

"""--------------------and-----------------------"""
# temp = 25
# is_sunny = True
#
# if temp >= 28 and is_sunny:
#     print("It is HOT outside")
# elif temp <=0 and is_sunny:
#     print("It is COLD outside")
# elif 28 > temp > 0 and is_sunny:
#     print("It is Warm outside")
# elif temp >= 28 and not is_sunny:
#     print("It is HOT outside , Cloudy")
# elif temp <=0 and not is_sunny:
#     print("It is COLD outside , Cloudy")
# elif 28 > temp > 0 and not is_sunny:
#     print("It is Warm outside , Cloudy")


# -------------Conditional expression---------------------------------------------

"""conditional expression = A one-line shortcut for the if-else statement (ternary operators)
                            print or assign one of two values based on a condition
                            X f condition else Y"""

# num = 6
# a = 6
# b = 7
# age = 25
# temp = 30
# user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temp > 20 else "COLD"
# access_level = "Full Access" if user_role == "admin" else "Limited Access"

# ---------------------String methods-----------------------------------------

# len(name) get length of a string
# name.find("") find the element and print index (first occurrence)
# name.rfind("") last occurrence if can't find it will give -1
# name.capitalized() this will capitalized first letter
# name.upper() make all of characters upper case
# name.lower() make all characters lower case
# name.isdigit() will return true if string only contain digits
# name.isalpha() will return true or false depending only alphabetical char
# name.count("o") count how many char in the string
# name.replace("-" , " ")

# ------------------Exercise------------------------------------------------

# validate user input exercise
# 1. username is no more than 12 chars
# 2. username must not contain spaces
# 3. username must not contain digits

# username = input("Enter username: ")
#
# if len(username) >= 12:
#     print("username is no more than 12 characters")
# elif username.find(" ") != -1:
#     print("username must not contain spaces")
# elif not username.isalpha():
#     print("username must not contain digits")
# else:
#     print(f"Welcome {username}!")

# -----------------String indexing---------------------------------------------

"""indexing = accessing elements of a sequence using [] (indexing operator)
                [start : end : step]"""


# credit_number = "1234-5678-9012-3456"

# print(credit_number[9]) 9th digit
# print(credit_number[0:4]) 0 to 4th digit
# print(credit_number[:4]) same as above
# print(credit_number[5:]) print 5th digit to last index
# print(credit_number[-1]) last index
# print(credit_number[0:4])
# print(credit_number[::2]) print every second char in the string

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

"""backwords"""
# credit_number = credit_number[::-1]
# print(credit_number)

# -------------------format specifiers--------------------------------------

"""format specifiers = {value:flags} format a value based on what flags are inserted

 .(number)f = round to that many decimal places (fixed point)
 :(number) = allocate that many spaces
 :03 = allocate and zero pad that many spaces
 :< = left justify
 :> = right justify
 :^ = center justify
 :+ = use a plus sign to indicate postive value
 := = place sign to leftmost position
 : = insert a space before positive number
 :, = comma separator"""

# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34

# print(f"Price 1 is ${price1:.1f}")
# print(f"Price 2 is ${price2:.2f}")
# print(f"Price 3 is ${price3:.2f}")

# print(f"Price 1 is ${price1:,}")
# print(f"Price 2 is ${price2:,}")
# print(f"Price 3 is ${price3:,}")

# -------------------While loop--------------------------------------

""" while loop = execute some code WHILE some condition remains true"""

# name = input("Enter your name: ")
#
# while name == "":
#     print("You did not enter a name")
#     name = input("Enter your name: ")
#
# print(f"Hello, {name}!")

"""logical operators"""

# food = input("Enter a food you like (q to quite): ")
#
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quite): ")
#
# print("Bye")

# num = int(input("Enter a # between 1 - 10"))
#
# while num > 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10"))
#
# print(f"Your number is {num}")

# -------------------for loop--------------------------------------

""" for loops = execute a block of code a fixed number of times.
                You can iterate over a range, string, sequence, etc"""

# for x in range(1, 11):
#     print(x)

# for x in reversed(range(1, 11)):
#     print(x)
#
# print("HAPPY NEW YEAR!")

# for x in range(3, 31, 3):
#     print(x)

# credit_number = "1234-5678-9012-3456"
#
# for x in credit_number:
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue
#     else:
#         print(x)

# for x in range(1, 21):
#     if x == 13:
#         break
#     else:
#         print(x)

# ----------------------countdown timer-----------------------------------

# import time
#
# my_time = int(input("Enter the time in seconds: "))
#
# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
#
# print("TIME'S UP!")

# ----------------------nested loop-----------------------------------

"""nested loop = A loop within another loop (outer, inner)
                outer loop:
                    inner loop:"""

# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
#     print()

# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of columns: "))
# symbol = input("Enter the symbol to use: ")
#
# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()

# ----------------------lists, sets and tuples-----------------------------------

"""Collection = single 'variable' used to store multiple values
    List = [] ordered and changeable. Duplicate OK
    Set = {} unordered and immutable, but Add/Remove OK. NO duplicate
    Tuple = () ordered and unchangeable. Duplicate OK. FASTER"""

#           --------list----------

# fruits = ["apple" , "orange" , "banana" , "coconut"]

# print(fruits[::-1])
# print(len(fruits))
# print("apple" in fruits)

# for fruit in fruits:
#     print(fruit)

# fruits[0] = "pineapple" # replace
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.sort() alphabetical order
# fruits.reverse() reverse list
# fruits.clear() clear list
# print(fruits.index("apple")) print index
# print(fruits.count("apple")) count apple

# print(fruits)

#           --------set----------

# fruits = {"apple" , "orange" , "banana" , "coconut"}

# print(len(fruits))
# print("apple" in fruits)

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop() random element will be remove
# fruits.clear()

# for fruit in fruits:
#     print(fruit)


# print(fruits)

#           --------Tuple----------

# fruits = ("apple" , "orange" , "banana" , "coconut")

# print(len(fruits))
# print("apple" in fruits)

# fruits.index("apple")
# fruits.count("apple")

# print(fruits)

# for fruit in fruits:
#     print(fruit)

#           --------shopping cart program----------

# foods = []
# prices = []
# total = 0
#
# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)
#
# print("----- YOUR CART ------")
#
# for food in foods:
#     print(food, end=" ")
#
# for price in prices:
#     total += price
#
# print()
# print(f"Your total is: ${total: }")

# ----------------------2D collections-----------------------------------

# for this also we can use tuple and set

# fruits =     ["apple", "banana", "cherry"]
# vegetables = ["celery" , "carrot" , "potatoes"]
# meats =      ["chicken" , "fish" , "turkey"]
#
# groceries = [fruits, vegetables, meats]

# the below one is same as above one

# groceries = [["apple", "banana", "cherry"],
#              ["celery" , "carrot" , "potatoes"],
#              ["chicken" , "fish" , "turkey"]]


# print(groceries[1][0]) # first [0] is row and second [0] is column

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

#    ----- activity ---------

# num_pad = ((1,2,3),
#            (4,5,6),
#            (7,8,9),
#            ("*", 0, "#"))
#
# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()

# ----------------------Dictionary-----------------------------------

"""dictionary = a collection of {key:value} pairs
                ordered and changeable. NO duplicate"""

# capitals = {"USA": "Washington D.C",
#             "India": "New Delhi",
#             "China": "Beijing",
#             "Russia": "Moscow"}

# print(capitals.get("India"))

# if capitals.get("Japan"):
#     print("That capital Exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem() remove latest item in dict
# capitals.clear()

# keys = capitals.keys()

# for key in capitals.keys():
    # print(key)

# values = capitals.values()
# print(values)

# for value in capitals.values():
#     print(value)

# items = capitals.items()
# print(items)

# for key, value in capitals.items():
#     print(f"{key}: {value}")

#    ----- Concession stand program ---------

# menu = {"pizza": 3.00,
#         "nachos": 4.50,
#         "popcorn": 6.00,
#         "fries": 2.50,
#         "chips": 1.00,
#         "pretzel": 3.50,
#         "soda" : 3.00,
#         "lemonade": 4.25}
#
# cart = []
# total = 0
#
# print("---------- Menu ------------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("----------------------------")
#
# while True:
#     food = input("Select an item (q to quite): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
#
# print("-------- YOUR ORDER ----------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end="")
#
# print()
# print(f"Total is: ${total:.2f}")

# ----------------------Random Numbers-----------------------------------

import random

# low = 1
# high = 100
# options = ("rock", "paper", "scissor")
# cards = ["2", "3" , "4" , "5" , "6" , "7" , "8" , "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, high)
# number = random.random() random float
# option = random.choice(options)
# random.shuffle(cards)
#
# print(cards)

# ----------------------Functions-----------------------------------

"""functions = A block of reusable code
                place () after the function name to invoke it"""

# ----------------------return--------------------------------------

"""return = statement used to end a function
            and send a result back to the caller"""

# ----------------------default argument------------------------------

"""default argument = a default value for a certain parameter
                        default is used when that argument is omitted
                        make your function more flexible, reduce # of arguments
                        1. Positional, 2. Default, 3. Keyword, 4. arbitrary"""

#  -------- default ----------------

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * discount + tax
#
# print(net_price(500))
# print(net_price(100, 50))
# print(net_price(100, 50,0.10))

#  -------- keyword ----------------

"""keyword argument = an argument preceded by an identifier
                      helps with readability
                      order of arguments doesn't matter"""


# print("1", "2", "3", "4", "5", sep="-")

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"
#
# phone_num = get_phone(country=1,area=123,first=465,last=7890)
# print(phone_num)

#  -------- arbitrary ----------------

"""*args = allows you to pass multiple non-key arguments
   **kwargs = allows you to pass keyword arguments
   * unpacking operator"""

# -- *args --

# def add(*nums):
#     total = 0
#     for arg in nums:
#         total += arg
#     return total
#
# print(add(1,2))

# -- **kwargs --

# def print_address(**kwargs):
#     for key, value in kwargs.keys():
#         print(f"{key}: {value}")
#
# print_address(street="123 Fake St",apt="100", city="Ragama",state="MI", zip="12345")

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     print(f"{kwargs.get('street')}")
#     print(f"{kwargs.get('city')}")
#     print(f"{kwargs.get('state')}")
#     print(f"{kwargs.get('zipcode')}")
#
# shipping_label("Dr.", "Spongebob", "Squarepants", "III",
#                street="123 Fake St.",
#                apt="100",
#                city="Detroit",
#                state="MI",
#                zip="54321")

# ----------------------Iterables------------------------------

"""Iterables = An object/collection that can return its elements one at a time,
               allowing it to be iterated over in a loop"""

# numbers = [1,2,3,4,5]
#
# for number in reversed(numbers):
#     print(number, end=" - ")

# ----------------------Membership operators--------------------

"""Membership operators = used to test whether a value or variable is found in a sequence
                          (string, list , tuple, set or dictionary)
                          1. in
                          2. not in"""

# word = "APPLE"
#
# letter = input("Guess a letter in the secret word")

# if letter in word:
#     print(f"{letter} is in the word")
# else:
#     print(f"{letter} is not in the word")

# if letter not in word:
#     print(f"{letter} is not in the word")
# else:
#     print(f"{letter} is in the word")

# ----------------------List comprehension--------------------

"""List comprehension = A concise way to create lists in python
                        compact and easier to read than traditional loops
                        [expression for value in iterable if condition]"""

# doubles = [x*2 for x in range(1,11)]
# triples = [y*3 for y in range(1,11)]
# squares = [z*z for z in range(1,11)]
#
# print(squares)
# print(triples)
# print(doubles)

# for x in range(1,11):
#     doubles.append(x * 2)

# fruits = [fruit.upper() for fruit in ["apple", "banana", "cherry"]]
# print(fruits)

# numbers = [1 , -2, 3, -4, 5, -6]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
#
# print(positive_nums)
# print(negative_nums)

# ----------------------Match-case statement (switch)--------------------

"""Match-case statement (switch) = An alternative to using many 'elif' statements
                                   Execute some code if a value matches a 'case'
                                   Benefits: cleaner and syntax is more readable"""


# def day_of_week(day):
#     match day:
#         case 1:
#             return 'Monday'
#         case 2:
#             return 'Tuesday'
#         case 3:
#             return 'Wednesday'
#         case 4:
#             return 'Thursday'
#         case 5:
#             return 'Friday'
#         case 6:
#             return 'Saturday'
#         case 7:
#             return 'Sunday'
#         case _:
#             return 'Unknown'
#
# print(day_of_week(1))

# def is_weekend(day):
#     match day:
#         case 'Saturday' | 'Sunday':
#             return True
#         case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
#             return False
#         case _:
#             return False

# ----------------------module--------------------------------

"""module = a file containing code you want to include in your program
            use 'import' to include a module (built-in or your own)
            useful to break up a large program reusable separate files"""

# example.py

"""pi = 3.14159

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * radius ** 2"""

# main.py

# import example
#
# result = example.pi
# result = example.square(3)
# result = example.cube(3)
# result = example.circumference(3)
#
# print(result)

# ------------------------scope resolution------------------------------

"""variable scope = where a variable is visible and accessible
   scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in"""

# ------------------------if __name__ == __main__------------------------------

"""if __name__ == __main__ : (this script can be imported OR run standalone)
                              Functions and classes in this module can be reused
                              without the main block of code executing"""

"""Good practice (code is modular,
                  helps readability,
                  leaves no global variables
                  avoid unintended execution)"""

"""ex: library = Import library for functionality
                 when running library directly, display a help page"""

# def main():
#     # Program goes here
#
# if __name__ == "__main__":
#     main()

# -----------------------------OOP-----------------------------------------

"""object = A "bundle" of related attributes (variables) and methods (functions)
            Ex. phone, cup, book
            You need a "clas" to create many object"""

"""class = (blueprint) used to design the structure and layout of an object"""

# # car.py file
# class Car:
#     def __init__(self, model, year, color, for_sale):          # constructor
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
#
#     def drive(self):
#         print(f"You drive the {self.model}")
#
#     def stop(self):
#         print(f"You stop the {self.model}")
#
# #--------------------------------------------------------------------
# # main.py
#
# # from car import Car
#
# car1 = Car('Mustang', 2024, "red", False)
# car2 = Car('Mustang', 2025, "red", True)
#
# car2.drive()
# car1.drive()
# car1.stop()
# car2.stop()

# -----------------------------class variables-----------------------------------------

"""class variables = Shared among all instance of a class
                     Define outside the constructor
                     Allow you to share data among all objects created from that class"""

# class Student:
#
#     class_year = 2024
#     num_students = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1
#
# student1 = Student("John", 22)
# student2 = Student("Wick", 35)
# student3 = Student("Dasuni", 45)
#
# print(student1.name)
# print(student1.age) # instant variable
# print(Student.class_year) # class variable
# print(f"My Gratuating class of {Student.class_year} has {Student.num_students} students")


# -----------------------------Inheritance-----------------------------------------

"""Inheritance = Allows a class to inherit attributes from another class
                 Helps with code reusability and extensibility
                 class Child(Parent)"""

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
#
#     def eat(self):
#         print(f"{self.name} is eating.")
#
#     def sleep(self):
#         print(f"{self.name} is sleeping.")
#
# class Dog(Animal):
#     def speak(self):
#         print("WOOLF")
#
# class Cat(Animal):
#     def speak(self):
#         print("Meow")
#
# class Mouse(Animal):
#     def speak(self):
#         print("Chick")
#
# dog = Dog("Tommy")
#
# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()

# -----------------------------multiple Inheritance-----------------------------------------

"""multiple inheritance = inherit from more than one parent class
                          C(A, B)"""

# class Prey:
#     def flee(self):
#         print("This animal is fleeing")
#
# class Predator:
#     def hunt(self):
#         print("This animal is hunting")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator):
#     pass
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.hunt()
# fish.flee()

# -----------------------------multilevel Inheritance-----------------------------------------

"""multilevel inheritance = inherit from a parent which inherits from anther parent
                            C(B) <- B(A) <- A"""

# class Animal:
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f"{self.name} is eating...")
#
#     def sleep(self):
#         print(f"{self.name} is sleeping...")
#
# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")
#
# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator):
#     pass
#
# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")
#
# rabbit.flee()
# rabbit.sleep()
# rabbit.eat()
# print()
#
# hawk.hunt()
# hawk.sleep()
# hawk.eat()
# print()
#
# fish.hunt()
# fish.sleep()
# fish.eat()
# fish.flee()

# -----------------------------super-----------------------------------------
#
# """super() = Function used in a child class to call methods from a parent class (superclass)
#              Allows you to extend the functionality of a child class"""
#
# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled
#
#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}.")
#
#
# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius
#
#     def describe(self):   # method overriding
#         super().describe()
#         print(f"It is a circle with area of {3.14 * self.radius * self.radius}cm^2.")
#
# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width
#
#     def describe(self):   # method overriding
#         super().describe()
#         print(f"It is a Square with area of {self.width * self.width}cm^2.")
#
# class Rectangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height
#
#     def describe(self):   # method overriding
#         super().describe()
#         print(f"It is a Rectangle with area of {self.width * self.height}cm^2.")
#
# circle = Circle(color = "red", is_filled = True, radius = 5)
# square = Square(color = "red", is_filled = True, width = 5)
# rectangle = Rectangle(color = "red", is_filled = True, width = 5, height = 3)
#
# # print(circle.color)
# # print(circle.is_filled)
# # print(f"{square.color} cm")
#
# circle.describe()
# print()
# square.describe()
# print()
# rectangle.describe()

# -----------------------------Polymorphism-----------------------------------------

"""Polymorphism = Greek word that means to "have many forms or faces" 
                  Poly = Many
                  Morphe = Form"""

"""               TWO WAYS TO ACHIEVE POLYMORPHISM
                  1. Inheritance = An object could be treated of the same type as a parent class
                  2. "Duck typing" = Object must have necessary attributes/methods"""

# from abc import ABC, abstractmethod
#
# class Shape:
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return self.base * self.height * 0.5
#
# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         self.topping = topping
#         super().__init__(radius)
#
# shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni",9)]
#
# for shape in shapes:
#     print(f"{shape.area()}cm^2")


# -----------------------------Duck typing-----------------------------------------

"""Duck typing = Another way to achieve polymorphism besides Inheritance
                 Object must have the minimum necessary attributes/methods
                 "If it looks like a duck and quacks like a duck, it must be a duck." """

# class Animal:
#     alive = True
#
# class Dog(Animal):
#     def speak(self):
#         print("Dog")
#
# class Cat(Animal):
#     def speak(self):
#         print("Cat")
#
# class Car:
#     alive = True
#
#     def speak(self):
#         print("Car")
#
# animals = [Dog(), Cat(), Car()]
#
# for animal in animals:
#     animal.speak()
#     print(animal.alive)

# -----------------------------Static methods-----------------------------------------

"""Static methods = A method that belongs to a class rather than any object from that class (instance)
                    usually used for general utility functions"""

"""Instance methods = Best for operations on instance of the class (object)"""

"""Static methods = Best for utility functions that do not need access to class data"""

# class Employee:
#
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     def get_info(self):
#         return f"{self.name} = {self.position}"
#
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
#         return position in valid_positions
#
# employee1 = Employee("Janitor", "Manager")
# employee2 = Employee("Bro Code", "Cook")
#
# print(Employee.is_valid_position("Rocket Scientist"))
# print(employee1.get_info())
# print(employee2.get_info())

# -----------------------------Class methods-----------------------------------------

"""Class methods = Allow operations related to the class itself
                   Take (cls) as the first parameter, which represents the class itself"""

"""class methods = Best for class-level data or require access to the class itself"""

# class Student:
#
#     count = 0
#     total_gpa = 0
#
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa
#
#     # INSTANCE METHOD
#     def get_info(self):
#         return f"{self.name}, GPA: {self.gpa}"
#
#     @classmethod
#     def get_count(cls):
#         return f"Total # of students: {cls.count}"
#
#     @classmethod
#     def get_avg_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"{cls.total_gpa / cls.count}"
#
# student1 = Student("Bro code", 4.0)
# student2 = Student("Bro", 3.2)
#
# print(Student.get_count())
# print(Student.get_avg_gpa())

# -----------------------------Magic methods-----------------------------------------

"""Magic methods = Dunder methods (double underscode) __init__, __str__, __eq__
                   They are automatically called by many of Python's built in operations
                   They allow developers to define or customized the behavior of object"""

# class Student:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self): # this will print when we call method print(student1)
#         return f'Student {self.name}, age {self.age}'
#
#     def __eq__(self, other): # print(student1 == student2) compare to object
#         return self.name == other.name
#
#     def __gt__(self, other): # this grater than less than __lt__
#         return self.age > other.age
#
#     def __add__(self, other): # add
#         return self.age + other.age
#
#     def __contains__(self, keyword):
#         return keyword in self.name
#
#     def __getitem__(self, key):
#         if key == 'name':
#             return self.name
#         elif  key == 'age':
#             return self.age
#         else:
#             return f"Key {key} is not found"


# student1 = Student('Bro', 22)
# student2 = Student('Code', 33)

# ----------------------------- @property -----------------------------------------

"""@property = Decorator used to defined a method as a property (it can be accessed like an attribute)
               Benefit: Add additional logic when read, write or delete attributes
               Gives you getter, setter and deleter method"""


# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#
#     @property
#     def width(self):
#         return f"{self._width:.1f}"
#
#     @property
#     def height(self):
#         return f"{self._height:.1f}"
#
#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("width must be greater than 0")
#
#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("height must be greater than 0")
#
#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width has been deleted")
#
#     @height.deleter
#     def height(self):
#         del self._height
#         print("Height has been deleted")
#
# rectangle = Rectangle(3, 4)
#
# rectangle.width = 5
# rectangle.height = 6
#
# del rectangle.width
# del rectangle.height

# print(rectangle.width)
# print(rectangle.height)

# ----------------------------- Decorator -----------------------------------------

"""Decorator = A function that extends the behavior of another function
               w/o modifying base function
               Pass the base function as an argument to the decorator"""

# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print('Adding sprinkles')
#         func(*args, **kwargs)
#     return wrapper
#
# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print('Adding fudge')
#         func(*args, **kwargs)
#     return wrapper
#
# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"Here is your {flavor} ice cream 🍨")
#
# get_ice_cream("vanilla")

# ----------------------------- Exception -----------------------------------------

"""exception = An event that interrupts the flow of a program
               (ZeroDivisionError, TypeError, ValueError)
               1. try, 2. except, 3. finally"""

# try:
#     number = int(input("Enter a number: "))
#     print(1/number)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except ValueError:
#     print("You didn't enter a number")
# except Exception:
#     print("Something went wrong!")
# finally:
#     print("The program has finished running")

# ----------------------------- File detection -----------------------------------------

# import os
#
# file_path = "stuff/test.txt"
#
# if os.path.exists(file_path):
#     print("File exists")
#
#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("File does not exist")

# ----------------------------- File Writing -----------------------------------------

# w -> overwrite
# employees = ["Eugene", "Squidward", "Spongebob" , "Patrick"]

# file_path = "output.txt"

# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

#-------------------------------------------------------------------------

# import json
#
# employee = {
#     "name":"Spongebob",
#     "age":30,
#     "job":"cook"
# }
#
# file_path = "output.json"
#
# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

#-------------------------------------------------------------------------

# import csv
#
# employees = [["Name", "Age", "Job"],
#              ["Spongebob", 30, "Cook"],
#              ["Patrick", 37, "Unemployeed"],
#              ["Sandy", 27, "Scientist"]]
#
# file_path = "output.csv"
#
# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

# ----------------------------- File reading -----------------------------------------

# filepath = "output.txt"
#
# try:
#     with open(filepath, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("Permission denied")

#-------------------------------------------------------------

# import json
#
# filepath = "output.json"
#
# try:
#     with open(filepath, "r") as file:
#         content = json.load(file)
#         # print(content)
#         print(content["job"])
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("Permission denied")

#-------------------------------------------------------------

# import csv
#
# filepath = "output.csv"
#
# try:
#     with open(filepath, "r") as file:
#         content = csv.reader(file)
#         for row in content:
#             # print(row)
#             print(row[2])
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("Permission denied")

# ----------------------------- dates & times -------------------------------------

# import datetime
#
# date = datetime.date(2025,1,2)
# today = datetime.date.today()
#
# time = datetime.time(10,20)
# now = datetime.datetime.now()
#
# now = now.strftime("%H:%M:%S %d-%m-%Y")
#
# target_datetime = datetime.datetime(2020,1,2, 12, 30, 1)
# current_datetime = datetime.datetime.now()
#
# if target_datetime < current_datetime:
#     print("Target date is passed")
# else:
#     print("Target date is NOT passed")
#
#  print(now)

# ----------------------------- multithreading -------------------------------------

"""multithreading = Used to perform multiple tasks concurrently (multitasking)
                    Good for I/O bound tasks like reading files or fetching data from APIs
                    threading. Thread(target=my_function)"""

# import threading
# import time
#
# def walk_dog(first, second):
#     time.sleep(8)
#     print(f"You finished walking the dog {first} {second}")
#
# def take_out_trash():
#     time.sleep(2)
#     print("You take out the trash")
#
# def get_mail():
#     time.sleep(4)
#     print("You get the mail")
#
# chore1 = threading.Thread(target=walk_dog, args=("Scooby","Doo"))
# chore1.start()
#
# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()
#
# chore3 = threading.Thread(target=get_mail)
# chore3.start()
#
# chore1.join()
# chore2.join()
# chore3.join()
#
# print("All done")

# ----------------------------- connecting API -------------------------------------

import requests

base_url ="https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    # print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")