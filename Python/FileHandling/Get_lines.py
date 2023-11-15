# Write a function that takes a file name as input and returns the number of lines in the file.
# The function should prompt the user for the file name, and print the number of lines in the file.

with open("C:\SEW\Random_Files\RandomText.txt", "r") as f:
    print(len(f.readlines()))
