start = int(input("Startwert\n"))

end = int(input("Endwert\n"))

sum = 0

for i in range(end - start + 1):
    sum = (start + i) + sum
else:
    print(sum)
