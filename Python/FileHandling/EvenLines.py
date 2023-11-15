# Write a function that takes a file name as input and prints all the even numbered lines of the file. The function should prompt the user for the file name.

DirecPath = input("What is the directory path")

i = 1

with open(DirecPath, "r") as f:

    text = f.readlines()

    while i < len(text):

        if i % 2 != 0:
            print(text[i])

        i += 1
