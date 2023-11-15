# Write a function that takes a file name as input and creates a new file with the same content but all uppercase.
# The function should prompt the user for the file name, and the new file name.

Directpath = input("What is the Directory Path\n")

with open(Directpath, "r") as f:
    text = f.read()
    print(text.upper())
