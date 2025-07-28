# Python Fundamentals Cheat-sheet
---

## Table of Contents

  - [Arithmetic & Math Operations](#1-arithmetic--math-operations)  
  - [Logical Operators](#2-logical-operators)  
  - [Conditional Expressions (Ternary Operators)](#3-conditional-expressions-ternary-operators)  
  - [String Methods](#4-string-methods--indexing)  
  - [String Indexing](#4-string-methods--indexing)  
  - [Format Specifiers](#5-format-specifiers)  
  - [While Loops](#6-loops)  
  - [For Loops](#6-loops)  
  - [Countdown Timer Example](#6-loops)  
  - [Nested Loops](#6-loops)  
  - [Collections (Lists, Sets, Tuples)](#7-collections-lists-sets-and-tuples)  
    - [Lists](#7-collections-lists-sets-and-tuples)  
    - [Sets](#7-collections-lists-sets-and-tuples)  
    - [Tuples](#7-collections-lists-sets-and-tuples)  
    - [Shopping Cart Program Example](#7-collections-lists-sets-and-tuples)  
  - [2D Collections](#8-2d-collections-nested-liststuples)  
  - [Dictionaries](#9-dictionary-key-value)  
    - [Concession Stand Program Example](#9-dictionary-key-value)  
  - [Random Numbers](#10-random-numbers)  
  - [Functions](#11-functions)  
    - [Return Statement](#11-functions)  
    - [Default Arguments](#11-functions)  
    - [Keyword Arguments](#11-functions)  
    - [Arbitrary Arguments (`*args`, `**kwargs`)](#11-functions)  
  - [Iterables](#12-iterables)  
  - [Membership Operators](#13-membership-operators)  
  - [List Comprehension](#14-list-comprehension)  
  - [Match-Case Statement (Switch)](#15-match-case-statement-switch)  
  - [Modules](#16-modules)  
  - [Scope Resolution (LEGB)](#17-variable-scope--scope-resolution-legb-rule)  
  - [`if __name__ == "__main__"`](#18-if-__name__-==-__main__)  
  - [Object-Oriented Programming (OOP)](#19-object-oriented-programming-oop)  
    - [Classes and Objects](#19-object-oriented-programming-oop)  
    - [Class Variables](#19-object-oriented-programming-oop)  
    - [Inheritance](#19-object-oriented-programming-oop)  
    - [Multiple Inheritance](#19-object-oriented-programming-oop)  
    - [Multilevel Inheritance](#19-object-oriented-programming-oop)  
    - [`super()` Function](#19-object-oriented-programming-oop)    

---

## 1. Arithmetic & Math Operations

Python provides built-in functions and the `math` module for common mathematical operations.

### Built-in Functions

|Function|Description|Example|Output|
|---|---|---|---|
|`round(x)`|Rounds a number to the nearest integer.|`round(3.14)`|`3`|
|`abs(y)`|Returns the absolute value of a number.|`abs(-4)`|`4`|
|`pow(base, exp)`|Returns base raised to the power of exp.|`pow(4, 3)`|`64`|
|`max(x, y, z)`|Returns the largest value among arguments.|`max(3.14, 4, 5)`|`5`|
|`min(x, y, z)`|Returns the smallest value among arguments.|`min(3.14, 4, 5)`|`3.14`|

### Math Module

To use functions from the `math` module, you need to import it first (`import math`).

|Attribute/Function|Description|Example|Output|
|---|---|---|---|
|`math.pi`|The mathematical constant pi (pi).|`print(math.pi)`|`3.141592653589793`|
|`math.e`|The mathematical constant e (Euler's number).|`print(math.e)`|`2.718281828459045`|
|`math.sqrt(x)`|Returns the square root of `x`.|`math.sqrt(9)`|`3.0`|
|`math.ceil(x)`|Returns the smallest integer greater than or equal to `x` (rounds up).|`math.ceil(9.1)`|`10`|
|`math.floor(x)`|Returns the largest integer less than or equal to `x` (rounds down).|`math.floor(9.9)`|`9`|

---

## 2. Logical Operators

Logical operators evaluate multiple conditions and return `True` or `False`.

|Operator|Description|Example|
|---|---|---|
|`or`|Returns `True` if at least one condition is true.|`if temp > 35 or temp < 0 or is_raining:`|
|`and`|Returns `True` if all conditions are true.|`if temp >= 28 and is_sunny:`|
|`not`|Inverts the boolean value of a condition.|`if not is_sunny:`|

**Example Usage:**

Python

```
temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
elif 28 > temp > 0 and is_sunny:
    print("It is Warm outside")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside, Cloudy")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside, Cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is Warm outside, Cloudy")
```

---

## 3. Conditional Expressions (Ternary Operators)

A concise way to write if-else statements on a single line.

Syntax: X if condition else Y

**Examples:**

Python

```
num = 6
a = 6
b = 7
age = 25
temp = 30
user_role = "admin"

print("Positive" if num > 0 else "Negative")         # Output: Positive
result = "EVEN" if num % 2 == 0 else "ODD"           # result: "EVEN"
max_num = a if a > b else b                         # max_num: 7
min_num = a if a < b else b                         # min_num: 6
status = "Adult" if age >= 18 else "Child"          # status: "Adult"
weather = "HOT" if temp > 20 else "COLD"            # weather: "HOT"
access_level = "Full Access" if user_role == "admin" else "Limited Access" # access_level: "Full Access"
```

---

## 4. String Methods & Indexing

Python strings are sequences of characters that support various built-in methods and indexing for manipulation.

### String Methods

|Method|Description|Example (`name = "bro code"`)|Output|
|---|---|---|---|
|`len(name)`|Returns the length of the string.|`len(name)`|`8`|
|`name.find("o")`|Returns the index of the first occurrence of a substring.|`name.find("o")`|`2`|
|`name.rfind("o")`|Returns the index of the last occurrence of a substring.|`name.rfind("o")`|`7`|
|`name.capitalize()`|Capitalizes the first letter of the string.|`name.capitalize()`|`"Bro code"`|
|`name.upper()`|Converts all characters to uppercase.|`name.upper()`|`"BRO CODE"`|
|`name.lower()`|Converts all characters to lowercase.|`name.lower()`|`"bro code"`|
|`name.isdigit()`|Returns `True` if all characters are digits, `False` otherwise.|`"123".isdigit()`|`True`|
|`name.isalpha()`|Returns `True` if all characters are alphabetic, `False` otherwise.|`"abc".isalpha()`|`True`|
|`name.count("o")`|Counts occurrences of a substring.|`name.count("o")`|`2`|
|`name.replace("-", " ")`|Replaces occurrences of one substring with another.|`"12-34".replace("-", " ")`|`"12 34"`|

### String Indexing

Accessing individual characters or substrings using `[start : end : step]`.

|Syntax|Description|Example (`credit_number = "1234-5678-9012-3456"`)|Output|
|---|---|---|---|
|`credit_number[index]`|Accesses the character at a specific index.|`credit_number[9]`|`'9'`|
|`credit_number[start:end]`|Accesses a slice from `start` (inclusive) to `end` (exclusive).|`credit_number[0:4]`|`"1234"`|
|`credit_number[:end]`|Accesses a slice from the beginning to `end` (exclusive).|`credit_number[:4]`|`"1234"`|
|`credit_number[start:]`|Accesses a slice from `start` (inclusive) to the end.|`credit_number[5:]`|`"5678-9012-3456"`|
|`credit_number[-1]`|Accesses the last character.|`credit_number[-1]`|`'6'`|
|`credit_number[::step]`|Accesses characters with a specified step.|`credit_number[::2]`|`"13579135"`|
|`credit_number[::-1]`|Reverses the string.|`credit_number[::-1]`|`"6543-2109-8765-4321"`|

**Example: Validate User Input**

This example demonstrates using string methods and conditional statements to validate a username.

Python

```
username = input("Enter username: ")

if len(username) >= 12:
    print("username is no more than 12 characters")
elif username.find(" ") != -1:
    print("username must not contain spaces")
elif not username.isalpha():
    print("username must not contain digits")
else:
    print(f"Welcome {username}!")
```

---

## 5. Format Specifiers

Format specifiers are used with f-strings or `str.format()` to control the output formatting of values.

Syntax: `{value:flags}`

|Flag|Description|Example (`price = 3.14159`)|Output|
|---|---|---|---|
|`.(number)f`|Rounds to `number` decimal places (fixed point).|`f"${price:.2f}"`|`"$3.14"`|
|`:(number)`|Allocates `number` spaces.|`f"${price:10f}"`|`"$ 3.141590"`|
|`:03`|Allocates and zero-pads to `3` spaces.|`f"${1:03d}"`|`"$001"`|
|`:<`|Left-justifies the value.|`f"${price:<10.2f}"`|`"$3.14 "`|
|`:>`|Right-justifies the value.|`f"${price:>10.2f}"`|`" $3.14"`|
|`:^`|Centers the value.|`f"${price:^10.2f}"`|`" $3.14 "`|
|`:+`|Uses a plus sign to indicate positive values.|`f"${price:+.2f}"`|`"+$3.14"`|
|`:=`|Places the sign to the leftmost position.|`f"${-price:=+10.2f}"`|`"-$ 3.14"`|
|`:`|Inserts a space before positive numbers.|`f"${price: .2f}"`|`" $3.14"`|
|`:,`|Adds comma separators for thousands.|`f"${1234567.89:,}"`|`"$1,234,567.89"`|

**Example Usage:**

Python

```
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.1f}")  # Price 1 is $3.1
print(f"Price 2 is ${price2:.2f}")  # Price 2 is $-987.65
print(f"Price 3 is ${price3:.2f}")  # Price 3 is $12.34

print(f"Price 1 is ${price1:,}")    # Price 1 is $3.14159
print(f"Price 2 is ${price2:,}")    # Price 2 is $-987.65
print(f"Price 3 is ${price3:,}")    # Price 3 is $12.34
```

---

## 6. Loops

Loops are used to execute a block of code repeatedly.

### While Loop

Executes code **WHILE** a condition remains true.

Python

```
# Basic example
name = ""
while name == "":
    print("You did not enter a name")
    name = input("Enter your name: ")
print(f"Hello, {name}!")

# Using logical operators
food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
print("Bye")

# Input validation
num = int(input("Enter a # between 1 - 10: "))
while num < 1 or num > 10: # Corrected from num > 1 or num > 10
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))
print(f"Your number is {num}")
```

### For Loop

Executes a block of code a fixed number of times, iterating over a range, string, or sequence.

Python

```
# Iterating over a range
for x in range(1, 11): # Prints 1 to 10
    print(x)

# Reversed range
for x in reversed(range(1, 11)): # Prints 10 down to 1
    print(x)
print("HAPPY NEW YEAR!")

# Stepping in a range
for x in range(3, 31, 3): # Prints multiples of 3 up to 30
    print(x)

# Iterating over a string
credit_number = "1234-5678-9012-3456"
for x in credit_number:
    print(x)

# `continue` statement: skips the current iteration
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# `break` statement: terminates the loop entirely
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)
```

**Countdown Timer Example:**

Python

```
import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")
```

### Nested Loops

A loop within another loop. The inner loop completes all its iterations for each single iteration of the outer loop.

Python

```
# Simple nested loop
for x in range(3): # Outer loop iterates 3 times
    for y in range(1, 10): # Inner loop iterates 9 times for each outer iteration
        print(y, end="")
    print() # Newline after each inner loop completes

# Creating a shape with nested loops
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
```

---

## 7. Collections: Lists, Sets, and Tuples

Collections are single variables used to store multiple values.

### List (`[]`)

- **Ordered** and **changeable**.
    
- Allows **duplicates**.
    

Python

```
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits[::-1])      # Reverse the list: ['coconut', 'banana', 'orange', 'apple']
print(len(fruits))       # Length of the list: 4
print("apple" in fruits) # Check if element exists: True

for fruit in fruits:
    print(fruit)

fruits[0] = "pineapple"  # Replace element at index 0
fruits.append("grape")   # Add element to the end
fruits.remove("orange")  # Remove first occurrence of "orange"
fruits.sort()            # Sorts the list alphabetically/numerically
fruits.reverse()         # Reverses the order of elements
fruits.clear()           # Removes all elements
print(fruits.index("banana")) # Get index of "banana"
print(fruits.count("apple"))  # Count occurrences of "apple"
```

### Set (`{}`)

- **Unordered** and **immutable** (elements themselves cannot be changed after creation), but elements can be **added/removed**.
    
- **No duplicates**.
    

Python

```
fruits = {"apple", "orange", "banana", "coconut"}

print(len(fruits))       # Length of the set
print("apple" in fruits) # Check if element exists

fruits.add("pineapple")  # Add a new element
fruits.remove("apple")   # Remove an element
fruits.pop()             # Removes a random element
fruits.clear()           # Clears all elements

for fruit in fruits:
    print(fruit)
```

### Tuple (`()`)

- **Ordered** and **unchangeable** (immutable).
    
- Allows **duplicates**.
    
- Generally **faster** than lists for iteration when content doesn't need to change.
    

Python

```
fruits = ("apple", "orange", "banana", "coconut")

print(len(fruits))       # Length of the tuple
print("apple" in fruits) # Check if element exists

print(fruits.index("apple")) # Get index of "apple"
print(fruits.count("apple")) # Count occurrences of "apple"

for fruit in fruits:
    print(fruit)
```

### Shopping Cart Program (List Example)

Python

```
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART ------")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total:.2f}")
```

---

## 8. 2D Collections (Nested Lists/Tuples)

Collections can be nested to represent 2D structures (like matrices or grids).

Python

```
fruits =     ["apple", "banana", "cherry"]
vegetables = ["celery", "carrot", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats] # A list of lists

# Accessing elements: [row_index][column_index]
print(groceries[1][0]) # Output: 'celery'

# Iterating through 2D collection
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# Example: Number Pad (using tuple of tuples)
num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
```

---

## 9. Dictionary (`{key: value}`)

A collection of **key-value pairs**.

- **Ordered** (as of Python 3.7+) and **changeable**.
    
- **No duplicate keys**.
    

Python

```
capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("India")) # Get value by key: New Delhi

# Check if a key exists
if capitals.get("Japan"):
    print("That capital Exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"}) # Add new key-value pair
capitals.update({"USA": "Detroit"})   # Update value for existing key
capitals.pop("China")                 # Remove item by key
capitals.popitem()                    # Remove the last inserted item
capitals.clear()                      # Clear all items

# Iterating through keys, values, or items
keys = capitals.keys()
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items() # Returns a view of (key, value) pairs
for key, value in capitals.items():
    print(f"{key}: {value}")
```

### Concession Stand Program (Dictionary Example)

Python

```
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("---------- Menu ------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None: # Check if food item exists in menu
        cart.append(food)
    else:
        print("Invalid item. Please choose from the menu.")

print("-------- YOUR ORDER ----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")
```

---

## 10. Random Numbers

The `random` module provides functions for generating random numbers and making random choices.

Python

```
import random

low = 1
high = 100
options = ("rock", "paper", "scissor")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

number_int = random.randint(low, high) # Random integer between low (inclusive) and high (inclusive)
number_float = random.random()         # Random float between 0.0 (inclusive) and 1.0 (exclusive)
option_choice = random.choice(options) # Random choice from a sequence
random.shuffle(cards)                  # Shuffles a list in place

print(f"Random int: {number_int}")
print(f"Random float: {number_float}")
print(f"Random option: {option_choice}")
print(f"Shuffled cards: {cards}")
```

---

## 11. Functions

Functions are blocks of reusable code designed to perform a specific task. They enhance code organization and reusability.

### Basic Function Definition

Python

```
def greet(name):
    print(f"Hello, {name}!")

greet("Alice") # Invoking the function
```

### Return Statement

The `return` statement is used to end a function and send a result back to the caller.

Python

```
def add(a, b):
    return a + b

sum_result = add(5, 3) # sum_result will be 8
print(sum_result)
```

### Default Arguments

Parameters can have default values. If an argument is omitted during the function call, the default value is used. This makes functions more flexible.

**Order of Arguments:**

1. Positional Arguments
    
2. Default Arguments
    
3. Keyword Arguments
    
4. Arbitrary Arguments (`*args`, `**kwargs`)
    

Python

```
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))         # Output: 525.0 (discount=0, tax=0.05)
print(net_price(100, 0.10))   # Output: 94.5 (discount=0.10, tax=0.05)
print(net_price(100, 0.10, 0.08)) # Output: 97.2 (discount=0.10, tax=0.08)
```

### Keyword Arguments

Arguments preceded by an identifier (`parameter=value`). This improves readability and allows the order of arguments to be flexible.

Python

```
def get_phone(country, area, first, last):
    return f"+{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num) # Output: +1-123-456-7890
```

### Arbitrary Arguments (`*args` and `**kwargs`)

- `*args`: Allows you to pass a variable number of non-keyword arguments (as a tuple).
    
- `**kwargs`: Allows you to pass a variable number of keyword arguments (as a dictionary).
    

Python

```
# *args example
def add(*nums):
    total = 0
    for arg in nums:
        total += arg
    return total

print(add(1, 2, 3))    # Output: 6
print(add(10, 20, 30, 40)) # Output: 100

# **kwargs example
def print_address(**kwargs):
    for key, value in kwargs.items(): # Corrected from .keys()
        print(f"{key}: {value}")

print_address(street="123 Fake St", apt="100", city="Ragama", state="MI", zip="12345")

# Combined *args and **kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    print(f"Street: {kwargs.get('street')}")
    print(f"City: {kwargs.get('city')}")
    print(f"State: {kwargs.get('state')}")
    print(f"Zipcode: {kwargs.get('zipcode')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="MI",
               zipcode="54321")
```

---

## 12. Iterables

An iterable is an object or collection that can return its elements one at a time, allowing it to be iterated over in a loop (e.g., lists, tuples, strings, dictionaries).

Python

```
numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number, end=" - ") # Output: 5 - 4 - 3 - 2 - 1 -
print()
```

---

## 13. Membership Operators

Used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary).

|Operator|Description|
|---|---|
|`in`|Returns `True` if found.|
|`not in`|Returns `True` if not found.|

Python

```
word = "APPLE"
letter = input("Guess a letter in the secret word: ").upper()

if letter in word:
    print(f"{letter} is in the word")
else:
    print(f"{letter} is not in the word")
```

---

## 14. List Comprehension

A concise way to create lists in Python, offering a more compact and readable syntax than traditional loops.

Syntax: [expression for value in iterable if condition]

Python

```
# Basic list comprehension
doubles = [x * 2 for x in range(1, 11)] # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
triples = [y * 3 for y in range(1, 11)] # Output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
squares = [z * z for z in range(1, 11)] # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(doubles)
print(triples)
print(squares)

# Transforming elements
fruits_upper = [fruit.upper() for fruit in ["apple", "banana", "cherry"]]
print(fruits_upper) # Output: ['APPLE', 'BANANA', 'CHERRY']

# Filtering elements
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0] # Output: [1, 3, 5]
negative_nums = [num for num in numbers if num < 0]  # Output: [-2, -4, -6]

print(positive_nums)
print(negative_nums)
```

---

## 15. Match-Case Statement (Switch)

An alternative to using many `elif` statements, offering cleaner and more readable syntax for conditional execution based on value matching.

Python

```
def day_of_week(day_num):
    match day_num:
        case 1:
            return 'Monday'
        case 2:
            return 'Tuesday'
        case 3:
            return 'Wednesday'
        case 4:
            return 'Thursday'
        case 5:
            return 'Friday'
        case 6:
            return 'Saturday'
        case 7:
            return 'Sunday'
        case _: # Default case, like `else`
            return 'Unknown'

print(day_of_week(1)) # Output: Monday

def is_weekend(day_name):
    match day_name:
        case 'Saturday' | 'Sunday': # Multiple cases with `|`
            return True
        case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
            return False
        case _:
            return False

print(is_weekend('Saturday')) # Output: True
```

---

## 16. Modules

A module is a file containing Python code (variables, functions, classes, etc.) that you can include in your program using `import`. They are useful for breaking up large programs into reusable, separate files.

**Example: `example.py`**

Python

```
# example.py
pi = 3.14159

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * radius ** 2
```

**Example: `main.py`**

Python

```
# main.py
import example # Imports the entire module

result_pi = example.pi
result_square = example.square(3)
result_cube = example.cube(3)
result_circumference = example.circumference(3)
result_area = example.area(3)

print(f"PI: {result_pi}")
print(f"Square of 3: {result_square}")
print(f"Cube of 3: {result_cube}")
print(f"Circumference of radius 3: {result_circumference}")
print(f"Area of radius 3: {result_area}")
```

---

## 17. Variable Scope & Scope Resolution (LEGB Rule)

Variable scope defines where a variable is visible and accessible in your code.

Scope resolution in Python follows the LEGB rule:

1. **L**ocal: Defined inside a function.
    
2. **E**nclosed: Defined in a non-local, non-global scope (e.g., a nested function).
    
3. **G**lobal: Defined at the top level of a module.
    
4. **B**uilt-in: Pre-defined names in Python (e.g., `print`, `len`).
    

Python

```
# Global scope
global_var = "I'm global"

def outer_function():
    # Enclosed scope
    enclosed_var = "I'm enclosed"

    def inner_function():
        # Local scope
        local_var = "I'm local"
        print(local_var)
        print(enclosed_var)
        print(global_var)

    inner_function()

outer_function()
# print(local_var) # This would cause an error as local_var is not accessible here
```

---

## 18. `if __name__ == "__main__"`

This conditional statement is a common Python idiom that checks if the script is being run directly (as the main program) or imported as a module into another script.

**Benefits:**

- **Modularity:** Allows a script to be used both as a standalone program and as a reusable module.
    
- **Readability:** Clearly separates the executable part of the code from the module's definitions.
    
- **No Global Variables Execution:** Prevents code within the `if` block from running when the file is imported.
    
- **Avoids Unintended Execution:** Useful for libraries or modules where you might want to display a help page or run tests only when the library is executed directly.
    

**Structure:**

Python

```
# my_module.py

def main():
    """Main execution block of the script."""
    print("This code runs when my_module.py is executed directly.")

def some_function():
    """A function that can be imported and reused."""
    return "This function can be called from other scripts."

if __name__ == "__main__":
    main() # Call the main function if the script is run directly
```

If you `import my_module` into another file, `some_function()` will be available, but `main()` will not automatically execute.

---

## 19. Object-Oriented Programming (OOP)

OOP is a programming paradigm based on the concept of "objects," which are bundles of related attributes (variables) and methods (functions).

### Object & Class

- **Object:** An instance of a class. It represents a real-world entity with its own state (attributes) and behavior (methods).
    
- **Class:** A blueprint or template used to design the structure and layout of objects.
    

**Example: `car.py`**

Python

```
# car.py
class Car:
    def __init__(self, model, year, color, for_sale): # Constructor method
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")
```

**Example: `main.py`**

Python

```
# main.py
# from car import Car # Assuming car.py is in the same directory

car1 = Car('Mustang', 2024, "red", False) # Creating an object (instance) of Car
car2 = Car('Tesla', 2025, "white", True)

car2.drive() # Output: You drive the Tesla
car1.drive() # Output: You drive the Mustang
car1.stop()  # Output: You stop the Mustang
car2.stop()  # Output: You stop the Tesla
```

### Class Variables

Variables that are shared among all instances (objects) of a class. They are defined outside the constructor and within the class.

Python

```
class Student:
    class_year = 2024  # Class variable
    num_students = 0   # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1 # Increment class variable for each new student

student1 = Student("John", 22)
student2 = Student("Wick", 35)
student3 = Student("Dasuni", 45)

print(student1.name)         # Instance variable: John
print(student1.age)          # Instance variable: 22
print(Student.class_year)    # Class variable: 2024
print(f"My Graduating class of {Student.class_year} has {Student.num_students} students")
# Output: My Graduating class of 2024 has 3 students
```

### Inheritance

Allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass). This promotes code reusability and extensibility.

Syntax: `class Child(Parent):`

Python

```
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal): # Dog inherits from Animal
    def speak(self):
        print("WOOLF!")

class Cat(Animal): # Cat inherits from Animal
    def speak(self):
        print("Meow!")

dog = Dog("Tommy")

print(dog.name)      # Output: Tommy (inherited attribute)
print(dog.is_alive)  # Output: True (inherited attribute)
dog.eat()            # Output: Tommy is eating. (inherited method)
dog.sleep()          # Output: Tommy is sleeping. (inherited method)
dog.speak()          # Output: WOOLF! (Dog's own method)
```

### Multiple Inheritance

A class can inherit from more than one parent class.

Syntax: `class Child(Parent1, Parent2):`

Python

```
class Prey:
    def flee(self):
        print("This animal is fleeing.")

class Predator:
    def hunt(self):
        print("This animal is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): # Fish inherits from both Prey and Predator
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee() # Output: This animal is fleeing.
hawk.hunt()   # Output: This animal is hunting.
fish.hunt()   # Output: This animal is hunting.
fish.flee()   # Output: This animal is fleeing.
```

### Multilevel Inheritance

A class inherits from a parent, which in turn inherits from another parent.

Syntax: `C(B) <- B(A) <- A`

Python

```
class Organism: # Grandparent class
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is an organism.")

class Animal(Organism): # Parent class
    def eat(self):
        print(f"{self.name} is eating...")

    def sleep(self):
        print(f"{self.name} is sleeping...")

class Dog(Animal): # Child class inherits from Animal, which inherits from Organism
    def bark(self):
        print(f"{self.name} is barking!")

my_dog = Dog("Buddy") # Output: Buddy is an organism.
my_dog.eat()          # Output: Buddy is eating...
my_dog.sleep()        # Output: Buddy is sleeping...
my_dog.bark()         # Output: Buddy is barking!
```

### `super()` Function

The `super()` function is used in a child class to call methods from its parent class (superclass). It allows you to extend or customize the functionality of the parent class methods.

Python

```
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}.")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled) # Call parent's __init__
        self.radius = radius

    def describe(self):   # Method overriding
        super().describe() # Call parent's describe method
        print(f"It is a circle with area of {round(3.14 * self.radius ** 2, 2)}cm^2.")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled) # Call parent's __init__
        self.width = width

    def describe(self):   # Method overriding
        super().describe() # Call parent's describe method
        print(f"It is a Square with area of {self.width * self.width}cm^2.")

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=7)

circle.describe()
# Output:
# It is red and filled.
# It is a circle with area of 78.5cm^2.

print()

square.describe()
# Output:
# It is blue and not filled.
# It is a Square with area of 49cm^2.
```

### Polymorphism

The Greek word "polymorphism" means "to have many forms." In OOP, it refers to the ability of different objects to respond to the same method call in their own unique ways.

**Two main ways to achieve polymorphism in Python:**

1. **Inheritance:** An object of a child class can be treated as an object of its parent class, and methods are overridden.
    
2. **"Duck Typing":** If an object walks like a duck and quacks like a duck, then it's a duck. This means objects don't need to explicitly inherit from a common base class as long as they have the necessary methods/attributes.
    

Python

```
# Polymorphism through Inheritance (with Abstract Base Classes for clear interface)
from abc import ABC, abstractmethod

class Shape(ABC): # Abstract Base Class
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Pizza is a Circle and also has its own topping
class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius) # Call parent (Circle) constructor

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 9)]

for shape in shapes:
    print(f"Area: {round(shape.area(), 2)}cm^2")
# Output:
# Area: 50.24cm^2
# Area: 25cm^2
# Area: 21.0cm^2
# Area: 254.34cm^2
```
