try:
    with open('C:\\Users\\DELL\\Desktop\\XXX.txt') as file:
        print(file.read())

except FileNotFoundError:
    print("That file is not found")

# print(file.closed)