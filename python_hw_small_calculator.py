a = int(input("write a number: "))
b = int(input("write another number:"))
def multiply_two_strings(a,b):
    c = a * b
    return c 
def divide_two_strings(a,b):
    d = a / b
    return d
def add_two_strings(a,b):
    e = a + b 
    return e 
def minus_two_strings(a,b):
    f = a - b
    return f
g = input(" pick x, /, -, or + so that you can use these functions on the numbers you picked")
if g == "x":
    print(multiply_two_strings(a,b))
if g == "/":
    print(divide_two_strings(a,b))
if g == "-":
    print(minus_two_strings(a,b))
if g == "+":
    print(add_two_strings(a,b))