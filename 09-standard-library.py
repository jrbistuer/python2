"""
Python Standard Library
The Python Standard Library is a collection of modules and packages that come bundled with Python.
It provides a wide range of functionality, including file I/O, data manipulation, networking, and more.
The standard library is an essential part of Python programming and allows developers to perform various tasks without needing to install
additional packages.
Some commonly used modules in the Python Standard Library include:"""

import math  # Provides mathematical functions and constants
print(math.sqrt(16))  # Using the sqrt function from the math module
num = 4.9
print(math.ceil(num))  # Using the ceil function from the math module
print(math.floor(num))  # Using the floor function from the math module
print(math.trunc(num))  # Using the trunc function from the math module

import random  # Provides functions for generating random numbers
print(random.randint(1, 10))  # Using the randint function from the random module
type_of_fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(random.choice(type_of_fruits))  # Using the choice function from the random module
print(random.sample(type_of_fruits, 2))  # Using the sample function from the random module

import datetime  # Provides classes for manipulating dates and times
now = datetime.datetime.now()  # Getting the current date and time
print(now)  # Printing the current date and time
today = datetime.date.today()  # Getting the current date
print(today)  # Printing the current date
# formatting the date in a specific way
formatted_date = now.strftime("%Y/%m/%d %H:%M")
print(formatted_date)  # Printing the formatted date
print(now.year)  # Printing the current year
print(now.month)  # Printing the current month
print(now.day)  # Printing the current day
print(now.hour)  # Printing the current hour
print(now.minute)  # Printing the current minute
# delta
today = datetime.date.today()  # Getting the current date
in_10_days = today + datetime.timedelta(days=10)  # Adding 10 days to the current date
print(in_10_days)  # Printing the date 10 days from today
in_10_weeks = today + datetime.timedelta(weeks=10)  # Adding 10 weeks to the current date
print(in_10_weeks)  # Printing the date 10 weeks from today
# difference between two dates
date1 = datetime.date(2024, 1, 1)  # Creating a date object for January 1, 2024
date2 = datetime.date.today()  # Creating a date object for the current date
date_difference = date1 - date2  # Calculating the difference between the two dates
print(date_difference)  # Printing the difference between the two dates
