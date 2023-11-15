floats = int(input("Wie viele Kommazahlen sollen addiert werden?\n"))

sum = 0

for floats in range(floats):
    sum = float(input("Kommazahl:\n")) + sum
else:
    print(sum)
