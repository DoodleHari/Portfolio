# return statement = Function send python values/objects back to the caller(function name)
#                    These values/objects are known as the function's returns value

# def multiply(num1, num2):   normal function
#     print(num1 * num2)

# multiply(6, 8)

def multiply(num1, num2):
    # result = num1 * num2
    # return result           # store the returned value within a variable

    return num1 * num2

# print(multiply(6,8))

x = multiply(6, 8)

print(x)