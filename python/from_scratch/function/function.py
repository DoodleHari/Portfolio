# function = a block of code which is executed only when it is called...

#   def hello(nam, name):
#       print("Hello " + name + " " + nam)
#       print("Hii")

#   hello("NRS", "Hari")

# def hello(name):
#     print("Hello " + name)

# myName = "Leo"

# hello(myName)

# Arbitrary Arguments(*args) - Arbitrary Arguments are often shortened to *args and pack all args into a tuple

# def hello(*name):               # If you do not know how many arguments that will be passed
#     print("Hello " + name[1])   # into your function, add a '*' before the parameter name in the func definition...

# hello("Hari", "Leo")

# def add(*stuff):    # parameter
#     sum = 0
#     stuff = list(stuff)
 #    stuff[0] = 0
 #    for i in stuff:
 #        sum += i
 #    return sum

# print(add(1, 2, 3, 4, 5))   # argument

# Keyword Arguments - You can also send arguments with the key = value syntax.

# def hello(name3, name2, name1):
#     print("My cute name is " + name3)

# hello(name1 = "Hari", name2 = "NRS", name3 = "Leo")

# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
   # print("Hello " + kwargs['first'] + " " + kwargs['last'])
   # print("hello", end=" ")
    
    for key, value in kwargs.items():
        print(value, end="")

hello(first="Hari", middle="N", last="RS")