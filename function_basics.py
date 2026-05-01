# Day 3 - Function Basics

# simple function
def greet(name):
    print("Hello,", name)

greet("Priyanka")

# return example
def add(a, b):
    return a + b

print("Sum:", add(5, 3))

# default argument
def greet_user(name="Guest"):
    print("Welcome,", name)

greet_user()

# *args example
def total_sum(*numbers):
    return sum(numbers)

print(total_sum(1, 2, 3, 4))

# **kwargs example
def display_info(**data):
    for key, value in data.items():
        print(key, ":", value)

display_info(name="Priyanka", age=21)