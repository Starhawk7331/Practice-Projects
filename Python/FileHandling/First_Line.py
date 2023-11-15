# Write a function that takes a file name as input and returns the first line of the file.
# The function should prompt the user for the file name, and print the first line of the file.

Directpath = input("What is the Directory Path\n")

with open(Directpath, "r") as f:
    print(f.readline())
