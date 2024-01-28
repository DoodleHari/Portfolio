# class MyClass:
#     def __init__(self, parameter1, parameter2):
#         # Initialize instance variables
#         self.attribute1 = parameter1
#         self.attribute2 = parameter2

# # Create an instance of MyClass
# my_object = MyClass("value1", "value2")

# # Access the attributes of the instance
# print(my_object.attribute1)  # Output: value1
# print(my_object.attribute2)  # Output: value2


# Define a simple class
# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

# Create instances (objects) of the Car class
# car1 = Car("Toyota", "Camry")
# car2 = Car("Honda", "Accord")

# "car1" and "car2" are instances of the Car class


class Dog:
    def __init__(self, name, age):
        # pass
        self.name = name    # ".name" is a attribute
        self.age = age
        # print(name)
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    # def bark(self):
    #     print("Bow Bow!!!")

    # def add_one(self, x):
    #     return x + 1

# print(pet.add_one(5))
# print(type(pet))

pet = Dog("Hari", 21)
pet.set_name("HariNRS")
pet.set_age(22)
# print(pet.name)
print(pet.get_name())
print(pet.get_age())

# pet.bark()
d = Dog("Leo", 1)
# print(d.name)
print(d.get_name())


