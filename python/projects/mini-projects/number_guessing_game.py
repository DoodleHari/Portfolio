import random

top_of_range = input("Type a number: ")

# int("25") -> 25

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

random_number = random.randrange(-5, 11)

