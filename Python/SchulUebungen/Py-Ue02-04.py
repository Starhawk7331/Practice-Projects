size = input("Wie groß sind sie?")

weight = input("Wie viel wiegen Sie?")

bmi = float(weight) / (float(size) * float(size))

print("Ihr BMI ist", bmi)

if bmi < 20:
    print("Untergewicht")
elif bmi < 25:
    print("Normalgewicht")
elif bmi < 30:
    print("Übergewicht")
elif bmi >= 30:
    print("starkes Übergewicht")
