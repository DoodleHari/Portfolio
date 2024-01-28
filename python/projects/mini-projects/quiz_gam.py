print("Welcome to the Quiz!!!")

playing = input("Do you want to play? ")

# text = "HaRi is a GreaT"
# print(text.lower())

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct")
    score += 1
    # score = score + 1
else:
    print("Not Correct")

answer = input("GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Not Correct")

answer = input("RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Not Correct")

answer = input("ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct")
    score += 1
else:
    print("Not Correct")

print("you answered for " + str(score) + " questions...")
print("you got " + str((score / 4) * 100) + "%")