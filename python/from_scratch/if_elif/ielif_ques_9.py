score=int(input("Enter the score:"))
if(score < 35):
    print("Poor student")
elif(score > 35 and score < 75):
    print("Average student")
elif(score > 75 and score <= 100):
    print("Excellent")
else:
    print("Invalid score")
