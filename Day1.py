'''a = "Hello, World!     " #Remove whitespace from the right end of the string
print(a.rstrip())
b = "     Hello, World!" #Remove whitespace from the left end of the string
print(b.lstrip())
c = "     Hello, World!     " #Remove whitespace from both ends of the string
print(c.strip())
print(b.replace(" ",""))    #Remove all whitespace from the string
a = ["apple", "banana", "cherry"]
print(a)
print(type(a))
a = ("apple", "banana", "cherry")
print(a)
print(type(a))
a = {"name": "John", "age": 36}
print(a)
print(a["name"])
print(type(a))
b = {1.1, 1, "Hello"}
print(b)
print(type(b))
b = {"vegetable": {"1": "carrot", "2": "potato", "3": "cabbage"},
     "fruit": {"1": "apple", "2": "banana", "3": "cherry"}}
print(len(b["vegetable"]))
print(len(b["fruit"]))
#Conditional statements and loops
password = '1234'
limit = 0
while (limit < 3):
    entry = input("Enter your password: ")
    if(password == entry):
        print("Access granted")
        break
    else:
        print("Access denied. Try again.")
        limit += 1        
else:    
    print("Too many attempts. Access denied.")
#Functions
def greet(name):
    print("Hello, " + name + "!")
greet("Alice")
def add(a, b):
    return a + b   
result = add(5, 3)
print(result)
#Classes and objects
class First:
    a = 10
    def display(self):
        print("This is a method inside the First class.")
        print("Value of a:", self.a)   
obj = First()
print(obj.a)
obj.a = 20
print(obj.a)
obj.display()
#Inheritance
class Second(First):
    b = 45 
    def show(self):
        print("This is a method inside the Second class.")
        print("Value of b:", self.b)
obj2 = Second()
print(obj2.b)
print(obj2.a)
print(obj.display())
#Importing the Calculator MODULE and using its functions
import Calculator 
print(Calculator.add(5, 3))
#Imprting Calculator MODULE with an alias and using its functions
import Calculator as calc
print(calc.multiply(5, 3))
#Importing specific functions from the Calculator MODULE and using them
from Calculator import add, subtract
print(add(10, 5))  
print(subtract(10, 5))
'''
#Importing all functions from the Calculator MODULE and using them
from Calculator import *
print(multiply(10, 5))
print(divide(10, 5))
print(add(10, 0))
