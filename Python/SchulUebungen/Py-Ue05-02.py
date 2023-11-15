tenints = []

tenints.append(int(input("Was ist der Startwert?")))

size = int(input("Wie oft soll es multipliziert werden?"))

mult = int(input("Soll es verdoppelt(2) oder verdreifacht(3) werden?"))

for i in range(size):
    tenints.append(tenints[i] * mult)

print(tenints)
