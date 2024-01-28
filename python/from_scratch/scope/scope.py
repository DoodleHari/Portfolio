# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped variable of a variable can be created

# follows the rule = LEGB - (Local, Enclosing, Global, Built-in)

name = "HariNRS"   # global scope(available inside & outside function)

def myName(name, age):
#    name = "Hari" # local scope(available only inside this function)
    print(name + " " + str(age)) # TypeError: can only concatenate str (not "int") to str - (name + age is error)

myName(name,21)