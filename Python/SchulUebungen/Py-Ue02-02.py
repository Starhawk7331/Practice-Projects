num1 = float(input("Erste Zahl\n"))

num2 = float(input("Zweite Zahl\n"))

if num2 != 0:
    sum = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    quot = num1 / num2

    print("Addition:", sum)
    print("Subtraktion:", diff)
    print("Produkt:", prod)
    print("Quotient:", quot)
else:
    print("Man kann nicht durch 0 dividieren")
