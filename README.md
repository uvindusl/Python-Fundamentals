# Python Fundamentals

This repository contains a collection of Python code snippets and examples covering fundamental concepts, from basic arithmetic and data types to control flow, functions, and advanced topics like list comprehensions and modules. It serves as a quick reference and learning resource for various Python functionalities.

---

## Table of Contents

- [Arithmetic & Math Operations](https://www.google.com/search?q=%23arithmetic--math-operations)
    
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
    

---

## Arithmetic & Math Operations

Basic arithmetic operations and common mathematical functions using the `math` module.

Python

```
import math

x = 3.14
y = 4
z = 5

# Built-in functions
result = round(x)  # 3
result = abs(-y)   # if y = -4 output will be 4
result = pow(4, 3) # 64
result = max(x, y, z) # 5
result = min(x, y, z) # 3.14

# Math module functions
print(math.pi)
print(math.e)
result = math.sqrt(9)  # 3.0
result = math.ceil(9.1) # 10
result = math.floor(9.9) # 9
```

---

## Logical Operators

Evaluate multiple conditions (`or`, `and`, `not`).

- `or`: At least one condition must be `True`.
    
- `and`: Both conditions must be `True`.
    
- `not`: Inverts the condition (`not False` is `True`, `not True` is `False`).
    

Python

```
# Example with 'or'
temp = 20
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is ok")

# Example with 'and' and 'not'
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

## Conditional Expressions (Ternary Operators)

A one-line shortcut for `if-else` statements, allowing you to print or assign one of two values based on a condition.

Syntax: `X if condition else Y`

Python

```
num = 6
a = 6
b = 7
age = 25
temp = 30
user_role = "admin"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temp > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
```

---

## String Methods

Common methods for manipulating strings.

Python

```
name = "Bro Code"

print(len(name))        # Get length of a string
print(name.find("o"))   # Find the element and print index (first occurrence)
print(name.rfind("o"))  # Last occurrence, returns -1 if not found
print(name.capitalize())# Capitalizes the first letter
print(name.upper())     # Makes all characters uppercase
print(name.lower())     # Makes all characters lowercase
print("123".isdigit())  # Returns True if string contains only digits
print("Hello".isalpha())# Returns True if string contains only alphabetical characters
print("Programming".count("m")) # Counts how many times a character appears
print("Hello-World".replace("-", " ")) # Replaces occurrences of a substring
```

### Exercise: Validate User Input

An example to validate user input for a username.

Python

```
# 1. username is no more than 12 chars
# 2. username must not contain spaces
# 3. username must not contain digits

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

## String Indexing

Accessing elements of a sequence using `[]` (indexing operator).

Syntax: `[start : end : step]`

Python

```
credit_number = "1234-5678-9012-3456"

print(credit_number[9])   # 9th digit
print(credit_number[0:4]) # 0 to 4th digit (exclusive of 4)
print(credit_number[:4])  # Same as above, defaults start to 0
print(credit_number[5:])  # Prints from 5th digit to the last index
print(credit_number[-1])  # Last index
print(credit_number[::2]) # Prints every second character in the string

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# Reversing a string
credit_number_reversed = credit_number[::-1]
print(credit_number_reversed)
```

---

## Format Specifiers

Format a value based on flags inserted into f-strings.

Syntax: `{value:flags}`

- `. (number)f`: Round to that many decimal places (fixed-point).
    
- `:(number)`: Allocate that many spaces.
    
- `:03`: Allocate and zero-pad that many spaces.
    
- `:<`: Left justify.
    
- `:>`: Right justify.
    
- `:` `^`: Center justify.
    
- `:+`: Use a plus sign to indicate a positive value.
    
- `:=`: Place sign to the leftmost position.
    
- `:` ``: Insert a space before a positive number.
    
- `:,`: Comma separator for thousands.
    

Python

```
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.1f}") # Rounds to one decimal place
print(f"Price 2 is ${price2:.2f}") # Rounds to two decimal places
print(f"Price 3 is ${price3:.2f}")

print(f"Price 1 is ${price1:,}")   # Adds comma separators
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")
```

---

## While Loops

Execute code WHILE some condition remains true.

Python

```
# Example: Looping until a valid name is entered
name = input("Enter your name: ")

while name == "":
    print("You did not enter a name")
    name = input("Enter your name: ")

print(f"Hello, {name}!")

# Example: Looping with a quit condition
food = input("Enter a food you like (q to quit): ")

while not food.lower() == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("Bye")

# Example: Validating numerical input
num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10: # Corrected condition to include both checks
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")
```

---

## For Loops

Execute a block of code a fixed number of times. You can iterate over a range, string, sequence, etc.

Python

```
# Iterate through a range
for x in range(1, 11):
    print(x)

# Iterate in reverse
for x in reversed(range(1, 11)):
    print(x)
print("HAPPY NEW YEAR!")

# Iterate with a step
for x in range(3, 31, 3):
    print(x)

# Iterate through a string
credit_number = "1234-5678-9012-3456"
for char in credit_number:
    print(char)

# 'continue' statement: skips the current iteration
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# 'break' statement: exits the loop entirely
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)
```

---

## Countdown Timer Example

A simple countdown timer using a `for` loop and `time.sleep()`.

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

---

## Nested Loops

A loop within another loop (outer, inner).

Python

```
# Basic nested loop example
for x in range(3): # Outer loop iterates 3 times
    for y in range(1, 10): # Inner loop iterates 9 times for each outer loop iteration
        print(y, end="")
    print() # Newline after each inner loop completes

# Activity: Print a rectangle of symbols
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
```

---

## Collections (Lists, Sets, Tuples)

A single 'variable' used to store multiple values.

### Lists

Ordered and changeable. Duplicates are allowed. Represented by `[]`.

Python

```
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits[::-1])      # Reverse the list
print(len(fruits))       # Get length
print("apple" in fruits) # Check for membership

for fruit in fruits:
    print(fruit)

fruits[0] = "pineapple"  # Replace an element
fruits.append("grape")   # Add to the end
fruits.remove("orange")  # Remove by value
fruits.sort()            # Sort alphabetically
fruits.reverse()         # Reverse the order
fruits.clear()           # Clear all elements
print(fruits.index("banana")) # Get index of an element
print(fruits.count("apple")) # Count occurrences of an element
```

### Sets

Unordered and immutable, but elements can be added/removed. No duplicates allowed. Represented by `{}`.

Python

```
fruits = {"apple", "orange", "banana", "coconut"}

print(len(fruits))
print("apple" in fruits)

fruits.add("pineapple")  # Add an element
fruits.remove("apple")   # Remove an element
fruits.pop()             # Remove a random element
fruits.clear()           # Clear all elements

for fruit in fruits:
    print(fruit)
```

### Tuples

Ordered and unchangeable. Duplicates are allowed. Generally faster than lists for iteration. Represented by `()`.

Python

```
fruits = ("apple", "orange", "banana", "coconut")

print(len(fruits))
print("apple" in fruits)

print(fruits.index("apple")) # Get index of an element
print(fruits.count("apple")) # Count occurrences of an element

for fruit in fruits:
    print(fruit)
```

### Shopping Cart Program Example

A practical example demonstrating list usage for a simple shopping cart.

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

print("Items:", end=" ")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total:.2f}")
```

---

## 2D Collections

Lists of lists (or tuples of tuples, etc.) to represent grids or tables.

Python

```
fruits = ["apple", "banana", "cherry"]
vegetables = ["celery", "carrot", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
# Or directly:
# groceries = [["apple", "banana", "cherry"],
#              ["celery" , "carrot" , "potatoes"],
#              ["chicken" , "fish" , "turkey"]]

print(groceries[1][0]) # Accessing element at row 1, column 0 (e.g., "celery")

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# Activity: Numpad representation
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

## Dictionaries

A collection of `{key:value}` pairs. Ordered and changeable. No duplicate keys.

Python

```
capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("India")) # Get value by key, returns None if key not found

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"}) # Add new key-value pair
capitals.update({"USA": "Detroit"})    # Update existing value
capitals.pop("China")                  # Remove by key
capitals.popitem()                     # Remove the last inserted item
capitals.clear()                       # Clear all items

# Iterating through keys, values, and items
for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

for key, value in capitals.items():
    print(f"{key}: {value}")
```

### Concession Stand Program Example

A program simulating a concession stand using a dictionary for the menu.

Python

```
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda" : 3.00,
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
    elif menu.get(food) is not None: # Check if the food exists in the menu
        cart.append(food)

print("-------- YOUR ORDER ----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")
```

---

## Random Numbers

Using the `random` module for generating random numbers and choices.

Python

```
import random

low = 1
high = 100
options = ("rock", "paper", "scissor")
cards = ["2", "3" , "4" , "5" , "6" , "7" , "8" , "9", "10", "J", "Q", "K", "A"]

number = random.randint(low, high) # Random integer between low and high (inclusive)
number_float = random.random()      # Random float between 0.0 and 1.0
option = random.choice(options)     # Random choice from a sequence
random.shuffle(cards)               # Shuffles a list in place

print(cards)
```

---

## Functions

A block of reusable code. Use `()` after the function name to invoke it.

Python

```
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

### Return Statement

Used to end a function and send a result back to the caller.

Python

```
def multiply(a, b):
    return a * b

result = multiply(5, 3)
print(result) # 15
```

### Default Arguments

A default value for a parameter that is used when that argument is omitted. Makes functions more flexible.

Order of arguments: 1. Positional, 2. Default, 3. Keyword, 4. Arbitrary.

Python

```
def net_price(list_price, discount=0, tax=0.05):
    # Corrected formula for net price (assuming discount is a percentage or absolute value based on context)
    # If discount is a percentage (e.g., 0.10 for 10%):
    # return list_price * (1 - discount) * (1 + tax)
    # If discount is an absolute amount to subtract:
    return (list_price - discount) * (1 + tax)

print(net_price(500))         # Uses default discount and tax
print(net_price(100, 50))     # Uses provided discount, default tax
print(net_price(100, 50, 0.10)) # Uses provided discount and tax
```

### Keyword Arguments

An argument preceded by an identifier. Helps with readability and the order of arguments doesn't matter.

Python

```
print("1", "2", "3", "4", "5", sep="-") # Example of a keyword argument 'sep'

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=465, last=7890)
print(phone_num)
```

### Arbitrary Arguments (`*args`, `**kwargs`)

- `*args`: Allows you to pass multiple non-keyworded (positional) arguments as a tuple.
    
- `**kwargs`: Allows you to pass keyworded arguments as a dictionary.
    
- `*`: Also used as an unpacking operator for sequences.
    

#### `*args` Example

Python

```
def add(*nums):
    total = 0
    for arg in nums:
        total += arg
    return total

print(add(1, 2))
print(add(1, 2, 3, 4, 5))
```

#### `**kwargs` Example

Python

```
def print_address(**kwargs):
    for key, value in kwargs.items(): # Corrected to .items() to iterate through key-value pairs
        print(f"{key}: {value}")

print_address(street="123 Fake St", apt="100", city="Ragama", state="MI", zip="12345")
```

#### Combined `*args` and `**kwargs` Example

Python

```
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print() # Newline after printing names
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

## Iterables

An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop.

Python

```
numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number, end=" - ")
print()
```

---

## Membership Operators

Used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary).

- `in`
    
- `not in`
    

Python

```
word = "APPLE"
letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"{letter} is in the word")
else:
    print(f"{letter} is not in the word")

if letter not in word:
    print(f"{letter} is not in the word")
else:
    print(f"{letter} is in the word")
```

---

## List Comprehension

A concise way to create lists in Python. Compact and often easier to read than traditional loops.

Syntax: `[expression for value in iterable if condition]`

Python

```
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(squares)
print(triples)
print(doubles)

# Example: Converting list elements to uppercase
fruits = [fruit.upper() for fruit in ["apple", "banana", "cherry"]]
print(fruits)

# Example: Filtering elements
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]

print(positive_nums)
print(negative_nums)
```

---

## Match-Case Statement (Switch)

An alternative to using many `elif` statements. Executes code if a value matches a 'case'. Benefits include cleaner and more readable syntax. (Available in Python 3.10+)

Python

```
def day_of_week(day):
    match day:
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
        case _: # Default case
            return 'Unknown'

print(day_of_week(1))

def is_weekend(day):
    match day:
        case 'Saturday' | 'Sunday': # Multiple patterns for a single case
            return True
        case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
            return False
        case _:
            return False
```

---

## Modules

A file containing code you want to include in your program. Use `import` to include a module (built-in or your own). Useful to break up a large program into reusable separate files.

**`example.py` (simulated module file):**

Python

```
# pi = 3.14159
#
# def square(x):
#     return x ** 2
#
# def cube(x):
#     return x ** 3
#
# def circumference(radius):
#     return 2 * pi * radius
#
# def area(radius):
#     return pi * radius ** 2
```

**`main.py` (simulated main program file):**

Python

```
# import example # Assumes example.py is in the same directory or Python path
#
# result_pi = example.pi
# result_square = example.square(3)
# result_cube = example.cube(3)
# result_circumference = example.circumference(3)
# result_area = example.area(3)
#
# print(result_pi)
# print(result_square)
# print(result_cube)
# print(result_circumference)
# print(result_area)
```

---

## Scope Resolution (LEGB)

variable scope: Where a variable is visible and accessible.

scope resolution: The order in which Python looks for variables:

- `L`: Local
    
- `E`: Enclosed (nonlocal)
    
- `G`: Global
    
- `B`: Built-in
    

---

## `if __name__ == "__main__"`

A common Python idiom. Code inside this block only runs when the script is executed directly (not when imported as a module).

Python

```
# This is a common construct in Python scripts.
# It means "If this script is being run directly (not imported as a module), then execute the code below."

def main():
    print("This code runs when the script is executed directly.")

if __name__ == "__main__":
    main()
```

---
