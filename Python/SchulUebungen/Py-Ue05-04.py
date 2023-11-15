Bars = int(input("Wie viele Balken gibt es?"))

Values = []

for i in range(Bars):
    Values.append(int(input("Balken: ")))

for i in range(Bars):
    print("Balken", i, ":", "*" * Values[i], Values[i])
