value = "Hari"
if value == "Har":
    print(value)
elif value == "Hari":
    print("Enter value: " + value)
else:
    print("Not Detected")


try:
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))

    print("1-add, 2-sub, 3-mul, 4-div")
    
    operation = int(input("Enter operation (1-4): "))

    if operation == 1:
        print(a + b)
    elif operation == 2:
        print(a - b)
    elif operation == 3:
        print(a * b)
    elif operation == 4:
        print("Error: Division by zero is not allowed.")

except:
    print("Error: Please enter valid numerical values for the operands and operation.")

