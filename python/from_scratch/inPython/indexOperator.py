# index operator [] = gives access to a sequence's element element(str, list, tuples)

name = "hari Hari"

# if (name[0].islower()):
#     name = name.capitalize()

first_name = name[1:4].upper()  # [0:2] 0 - index form where it should start, 2 - range, where to end
last_name = name[5:].lower()
last_character = name[-3]

print(first_name)
print(last_name)
print(last_character)