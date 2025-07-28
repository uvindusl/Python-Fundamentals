
Python Fundamentals
-----

## Table of Contents

  - [Arithmetic & Math Operations](Arithmetic&MathOperations)
  - [Logical Operators](https://www.google.com/search?q=%23logical-operators)
  - [Conditional Expressions (Ternary Operators)](https://www.google.com/search?q=%23conditional-expressions-ternary-operators)
  - [String Methods](https://www.google.com/search?q=%23string-methods)
  - [String Indexing](https://www.google.com/search?q=%23string-indexing)
  - [Format Specifiers](https://www.google.com/search?q=%23format-specifiers)
  - [While Loops](https://www.google.com/search?q=%23while-loops)
  - [For Loops](https://www.google.com/search?q=%23for-loops)
  - [Countdown Timer Example](https://www.google.com/search?q=%23countdown-timer-example)
  - [Nested Loops](https://www.google.com/search?q=%23nested-loops)
  - [Collections (Lists, Sets, Tuples)](https://www.google.com/search?q=%23collections-lists-sets-tuples)
      - [Lists](https://www.google.com/search?q=%23lists)
      - [Sets](https://www.google.com/search?q=%23sets)
      - [Tuples](https://www.google.com/search?q=%23tuples)
      - [Shopping Cart Program Example](https://www.google.com/search?q=%23shopping-cart-program-example)
  - [2D Collections](https://www.google.com/search?q=%232d-collections)
  - [Dictionaries](https://www.google.com/search?q=%23dictionaries)
      - [Concession Stand Program Example](https://www.google.com/search?q=%23concession-stand-program-example)
  - [Random Numbers](https://www.google.com/search?q=%23random-numbers)
  - [Functions](https://www.google.com/search?q=%23functions)
      - [Return Statement](https://www.google.com/search?q=%23return-statement)
      - [Default Arguments](https://www.google.com/search?q=%23default-arguments)
      - [Keyword Arguments](https://www.google.com/search?q=%23keyword-arguments)
      - [Arbitrary Arguments (`*args`, `**kwargs`)](https://www.google.com/search?q=%23arbitrary-arguments-args-kwargs)
  - [Iterables](https://www.google.com/search?q=%23iterables)
  - [Membership Operators](https://www.google.com/search?q=%23membership-operators)
  - [List Comprehension](https://www.google.com/search?q=%23list-comprehension)
  - [Match-Case Statement (Switch)](https://www.google.com/search?q=%23match-case-statement-switch)
  - [Modules](https://www.google.com/search?q=%23modules)
  - [Scope Resolution (LEGB)](https://www.google.com/search?q=%23scope-resolution-legb)
  - [`if __name__ == "__main__"`](https://www.google.com/search?q=%23if-__name__----__main__)
  - [Object-Oriented Programming (OOP)](https://www.google.com/search?q=%23object-oriented-programming-oop)
      - [Classes and Objects](https://www.google.com/search?q=%23classes-and-objects)
      - [Class Variables](https://www.google.com/search?q=%23class-variables)
      - [Inheritance](https://www.google.com/search?q=%23inheritance)
      - [Multiple Inheritance](https://www.google.com/search?q=%23multiple-inheritance)
      - [Multilevel Inheritance](https://www.google.com/search?q=%23multilevel-inheritance)
      - [`super()` Function](https://www.google.com/search?q=%23super-function)

-----

## Arithmetic & Math Operations

Basic arithmetic operations and common mathematical functions using the **`math`** module.

```python
# Arithmetic & maths

x = 3.14
y = 4
z = 5

result = round(x) # 3
result = abs(y) # if y = -4 output will be 4
result = pow(4,3) # 64
result = max(x, y, z) # 5
result = min(x, y, z) # 3.14

# ------------Math Operations---------------------------------------------------

import math

x = 9.9

print(math.pi)
print(math.e)
result = math.sqrt(x) # if x = 9 output will be 3.0
result = math.ceil(x) # if x = 9.1 output will be 10
result = math.floor(x) # if x = 9.9 output will be 9
```

-----

## Logical Operators

Evaluate multiple conditions (**`or`**, **`and`**, **`not`**).

```python
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
```

-----

## Conditional Expressions (Ternary Operators)

A one-line shortcut for the **`if-else`** statement.

```python
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
```

-----

## String Methods

Common methods for manipulating strings.

```python
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
```

### Exercise: Validate User Input

An example to validate user input for a username.

```python
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
```

-----

## String Indexing

Accessing elements of a sequence using **`[]`** (indexing operator).

```python
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
```

-----

## Format Specifiers

Format a value based on flags inserted into f-strings.

```python
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
```

-----

## While Loops

Execute some code WHILE some condition remains true.

```python
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
```

-----

## For Loops

Execute a block of code a fixed number of times. You can iterate over a range, string, sequence, etc.

```python
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
```

-----

## Countdown Timer Example

A simple countdown timer using a **`for`** loop and **`time.sleep()`**.

```python
# ----------------------countdown timer-----------------------------------

import time

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
```

-----

## Nested Loops

A loop within another loop (outer, inner).

```python
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
```

-----

## Collections (Lists, Sets, Tuples)

A single 'variable' used to store multiple values.

### Lists

**Ordered** and **changeable**. Duplicates are allowed. Represented by **`[]`**.

```python
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
```

### Sets

**Unordered** and **immutable**, but elements can be added/removed. **No duplicates** allowed. Represented by **`{}`**.

```python
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
```

### Tuples

**Ordered** and **unchangeable**. Duplicates are allowed. Generally **faster** than lists for iteration. Represented by **`()`**.

```python
#           --------Tuple----------

# fruits = ("apple" , "orange" , "banana" , "coconut")

# print(len(fruits))
# print("apple" in fruits)

# fruits.index("apple")
# fruits.count("apple")

# print(fruits)

# for fruit in fruits:
#     print(fruit)
```

### Shopping Cart Program Example

A practical example demonstrating list usage for a simple shopping cart.

```python
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
```

-----

## 2D Collections

Lists of lists (or tuples of tuples, etc.) to represent grids or tables.

```python
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
```

-----

## Dictionaries

A collection of **`{key:value}`** pairs. **Ordered** and **changeable**. **No duplicate keys**.

```python
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
```

### Concession Stand Program Example

A program simulating a concession stand using a dictionary for the menu.

```python
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
```

-----

## Random Numbers

Using the **`random`** module for generating random numbers and choices.

```python
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
```

-----

## Functions

A block of reusable code. Use **`()`** after the function name to invoke it.

```python
# ----------------------Functions-----------------------------------

"""functions = A block of reusable code
                place () after the function name to invoke it"""
```

### Return Statement

Used to end a function and send a result back to the caller.

```python
# ----------------------return--------------------------------------

"""return = statement used to end a function
            and send a result back to the caller"""
```

### Default Arguments

A default value for a parameter that is used when that argument is omitted. Makes functions more flexible.

```python
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
```

### Keyword Arguments

An argument preceded by an identifier. Helps with readability and the order of arguments doesn't matter.

```python
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
```

### Arbitrary Arguments (`*args`, `**kwargs`)

  - **`*args`**: Allows you to pass multiple non-keyworded (positional) arguments as a tuple.
  - **`**kwargs`**: Allows you to pass keyworded arguments as a dictionary.
  - **`*`**: Also used as an unpacking operator for sequences.

<!-- end list -->

```python
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
```

-----

## Iterables

An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop.

```python
# ----------------------Iterables------------------------------

"""Iterables = An object/collection that can return its elements one at a time,
               allowing it to be iterated over in a loop"""

# numbers = [1,2,3,4,5]
#
# for number in reversed(numbers):
#     print(number, end=" - ")
```

-----

## Membership Operators

Used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary).

```python
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
```

-----

## List Comprehension

A concise way to create lists in Python. Compact and often easier to read than traditional loops.

```python
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
```

-----

## Match-Case Statement (Switch)

An alternative to using many `elif` statements. Executes code if a value matches a 'case'. Benefits include cleaner and more readable syntax. (Available in Python 3.10+)

```python
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
```

-----

## Modules

A file containing code you want to include in your program. Use `import` to include a module (built-in or your own). Useful to break up a large program into reusable separate files.

**`example.py` (simulated module file):**

```python
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
```

**`main.py` (simulated main program file):**

```python
# main.py

# import example
#
# result = example.pi
# result = example.square(3)
# result = example.cube(3)
# result = example.circumference(3)
#
# print(result)
```

-----

## Scope Resolution (LEGB)

`variable scope`: Where a variable is visible and accessible.
`scope resolution`: The order in which Python looks for variables:

  - `L`: Local
  - `E`: Enclosed (nonlocal)
  - `G`: Global
  - `B`: Built-in

<!-- end list -->

```python
# ------------------------scope resolution------------------------------

"""variable scope = where a variable is visible and accessible
   scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in"""
```

-----

## `if __name__ == "__main__"`

A common Python idiom. Code inside this block only runs when the script is executed directly (not when imported as a module).

```python
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
```

-----

## Object-Oriented Programming (OOP)

### Classes and Objects

An **`object`** is a "bundle" of related attributes (variables) and methods (functions). A **`class`** is a "blueprint" used to design the structure and layout of an object.

```python
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
```

### Class Variables

Variables shared among all instances of a class, defined outside the constructor.

```python
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
```

### Inheritance

Allows a class to inherit attributes from another class, promoting code reusability and extensibility. Syntax: `class Child(Parent)`.

```python
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
```

### Multiple Inheritance

Inheriting from more than one parent class. Syntax: `class Child(Parent1, Parent2)`.

```python
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
```

### Multilevel Inheritance

Inheriting from a parent which itself inherits from another parent. Syntax: `C(B) <- B(A) <- A`.

```python
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
```

### `super()` Function

Used in a child class to call methods from a parent class (superclass), allowing you to extend the functionality of a child class.

```python
# -----------------------------super-----------------------------------------
#
# """super() = Function used in a child class to call methods from a parent class (superclass)
#               Allows you to extend the functionality of a child class"""
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
#     def describe(self):    # method overriding
#         super().describe()
#         print(f"It is a circle with area of {3.14 * self.radius * self.radius}cm^2.")
#
# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width
#
#     def describe(self):    # method overriding
#         super().describe()
#         print(f"It is a Square with area of {self.width * self.width}cm^2.")
#
# class Rectangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height
#
#     def describe(self):    # method overriding
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
```
