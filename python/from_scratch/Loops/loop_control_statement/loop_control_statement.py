# Loop control statement = change = loops execution from it's normal sequence

# break    = uesd to terminate the loop entirely,
# continue = skips to the next iteration of the loop,
# pass     = does nothing, acts as a placeholder

# while True:
#     name = input("Enter ur name: ")
#     if name != "Hari":
#         break

# phoneNumber = "90257-19990"
# 
# for i in phoneNumber:
#     if i == "-":
#         continue
#     print(i, end="")

for i in range(10, 21):
    if i == 13:
        pass
    else:
        print(i)