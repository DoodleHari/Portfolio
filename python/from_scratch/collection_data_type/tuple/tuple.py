# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Hari",21,"Male")

print(student.count("Hari"))

print(student.index("Male"))

for x in student:
    print(x)

if "Hari" in student:
    print("Hari is here!")