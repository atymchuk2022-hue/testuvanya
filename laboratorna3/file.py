#1
my_text = "Hello, this is my first Python code"
my_int = 7
my_float = 3.1415
my_list = ["apple", my_int, my_float, "text", my_text]
my_dict = {
    "fruit": "banana",
    "number": my_int,
    "message": my_text
}
my_tuple = ("Python", my_text)
my_set = {"hello", my_text + "!", str(my_int)}

print("Text variable:", my_text)
print("Integer:", my_int)
print("Float:", my_float)
print("List:", my_list)
print("Dictionary:", my_dict)
print("Tuple:", my_tuple)
print("Set:", my_set)

#2
print("First constant:", True)
print("Second constant:", None)
print(f"Using a constant inside f-string: {False}")
import keyword
print("\nList of Python reserved words:")
print(keyword.kwlist)

print("Absolute value of -12.5:", abs(-12.5), f"is equal to {abs(12.5)}", "and comparison:", abs(-12.5) == abs(12.5))
print("Maximum value among 5, 10, 3:", max(5, 10, 3))
print("Minimum value among 5, 10, 3:", min(5, 10, 3))
print("Length of the string 'Python':", len("Python"))

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Fruit at position {index} is {fruit}")
#3
from random import randint

A = randint(0, 1)
print(f"So A={A}" if A else "But it could be that A={}".format(A))

#4
A = 0
try:
    print("What happens if", 10/A, "?")
except Exception as e:
    print("Is this an error? >", e)
finally:
    print("Here we go anyway!")

#5
def get_name_age(name, age):
    return name, age

#6
with open("example.txt", "w") as f:
    f.write("Hello\n")
    f.write("This is a test file\n")
    f.write("Goodbye\n")
#7
with open("example.txt", "r") as f:
    for index, line in enumerate(f):
        print(f"{index})> {line.strip()}")
#8
my_lambda = lambda first, age: f'This code was written by: {first}, I am {age:10d} years old'

print("This is a regular function:", get_name_age)
print("And this is a lambda:", my_lambda)
print("Calling the lambda:", my_lambda('Artem', 1_000_000))
print(my_lambda(*get_name_age("Alice", 25)))

