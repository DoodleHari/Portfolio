# logical operator (and, or, not) = used to check if two or more conditional statement, and - both true, or - any one condition true, not - opposite like if true it show false...

temp = int(input("what is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("good temperature!")
    print("go outside")
elif not(temp < 0 or temp > 30):
    print("bad temperature")
    print("stay inside")