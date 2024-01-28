# str.format() = optional method that gives users
#                more control when displaying output

# animal = "cow"
# item = "moon"

# print("The " + animal + " jumped over the " + item)

# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item)) # positionnal argument
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) # keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal, item))
# 
# name = "Hari"
# padding
# print("Hello, this is {}".format(name))
# print("Hello, this is {:10}. Nice to meet you".format(name))
# print("Hello, this is {:<10}. Nice to meet you".format(name))
# print("Hello, this is {:>10}. Nice to meet you".format(name))
# print("Hello, this is {:^10}. Nice to meet you".format(name))

number = 1000

print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))   # binary
print("The number pi is {:o}".format(number))   # octa
print("The number pi is {:X}".format(number))   # x & X(lowercase & uppercase) hexadecimal
print("The number pi is {:E}".format(number))   # e or E scientific notation