# Write a function that takes a file name as input and checks if the file contains a specific word.
# The function should prompt the user for the file name and the word to search for, and return whether the word was found in the file or not.

word = input("Für welches Wort wollen Sie suchen?\n")

DirectPath = input("Was ist der Pfad")

with open(DirectPath, "r") as f:
    Text = f.read()
    print(Text.count(word))
