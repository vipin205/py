# 1. Write a Python program to define a function that accepts two numbers and returns their addition, subtraction, and multiplication as multiple returned values.
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add, sub, mul = calculate(a, b)

print("Addition =", add)
print("Subtraction =", sub)
print("Multiplication =", mul)
# 2. Create a program demonstrating function calls with positional arguments, keyword arguments (name="Sagar", marks=59.53), and default parameter values (b=10).
def display(name, marks=50):
    print("Name =", name)
    print("Marks =", marks)


display("Rahul", 80)

display(name="Sagar", marks=59.53)

display("Amit")
# 3. Write a Python function using variable-length arguments (*args) to calculate the total sum of an arbitrary number of numerical inputs passed during a function call.
def total_sum(*args):
    total = 0

    for num in args:
        total = total + num

    return total


result = total_sum(10, 20, 30, 40, 50)

print("Total sum =", result)
# 4. Implement a function using **kwargs that accepts variable keyword-value pairs and iterates through them to display key-value pairs.
def display(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)


display(name="Sagar", age=21, course="MCA", marks=85)
# 5. Write a program that reads space-separated numerical input into a list, passes the list to a function, and calculates both the sum and average of the elements.
def calculate(numbers):
    total = sum(numbers)
    average = total / len(numbers)

    return total, average


numbers = list(map(float, input("Enter numbers: ").split()))

total, average = calculate(numbers)

print("Sum =", total)
print("Average =", average)
# 6. Construct a Python program utilizing list comprehension to iterate through a range of numbers and construct a list consisting only of even values.
numbers = [x for x in range(1, 21) if x % 2 == 0]

print("Even numbers:", numbers)
# 7. Write a recursive function factorial(n) that calls itself to compute the factorial of a non-negative integer n.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial =", factorial(n))
# 8. Write a program using an anonymous lambda function along with Python's built-in filter() to extract even numbers from a given list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)
# 9. Demonstrate higher-order functions by using map() with lambda to compute the square of each list item, and reduce() from functools to calculate the cumulative product of the list.
from functools import reduce

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

product = reduce(lambda x, y: x * y, numbers)

print("Original list:", numbers)
print("Squares:", squares)
print("Cumulative product:", product)
# 10. Write a Python function using variable-length positional arguments (*args) to compute the L₂ norm (Euclidean length) of an arbitrary n-dimensional coordinate vector {v} = (v₁, v₂, ..., vₙ) calculated as:
# $$ \|v\|_2 = \sqrt{\sum_{i=1}^{n}v_i^2} $$
import math

def l2_norm(*args):
    total = 0

    for value in args:
        total = total + value ** 2

    return math.sqrt(total)


result = l2_norm(3, 4)

print("L2 Norm =", result)