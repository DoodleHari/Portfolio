import os

    # use '\\' it's a escape sequence for a backslash

path = "C:\\Users\\DELL\\Desktop\\XXX"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):            # to detect file
        print("That is a file")
    elif os.path.isdir(path):           # to detect driectory
        print("It's a folder")
else:
    print("not exists...")