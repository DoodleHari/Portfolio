totalNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
givenNumber = [3, 4, 8]


for num in totalNumber:
    if num not in givenNumber:
       print(num)

# List comprehension to create a new list containing numbers not in givenNumber
balanceNumber = [num for num in totalNumber if num not in givenNumber]

# Print the result
print("Balance Numbers:", balanceNumber)
