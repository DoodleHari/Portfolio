salary=int(input("Enter ur salary: "))
age=int(input("Enter ur age: "))
if(salary >= 20000 or age <= 25):
    print("Eligible for loan")
    loan=int(input("Enter ur amount: "))
    if(loan >= 50000):
        print("Max amount is 50000")
    else:
        print("You can get")
else:
    print("Not eligible")
