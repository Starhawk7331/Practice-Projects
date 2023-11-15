# Write a function that takes a directory path as input and returns the number of files in the directory.
# The function should prompt the user for the directory path, and print the number of files in the directory.

import os

directPath = input("What is the directory path.")

onlyfiles = next(os.walk(directPath))

print(len(onlyfiles))
