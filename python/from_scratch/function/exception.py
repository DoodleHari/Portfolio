# exception = events detected during execution that interrupt the flow of the program

try:
    numerator = int(input("Enter a number: "))
    denominator = int(input("Enter a number: "))

    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("can't divide by 0")

except ValueError as e:
    print(e)
    print("Enter only the num")
    
except Exception as e:
    print(e)
    print("something went wrong :(")

else:
    print(result)

finally:
    print("This will always execute")