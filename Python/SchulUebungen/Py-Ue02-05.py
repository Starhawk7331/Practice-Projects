points = int(input("wie viele Punkte haben Sie?\n"))

if points < 0 or points >= 25:
    print("Ungültige Punkteanzahl")
elif points <= 12:
    print("Nicht Genügend")
elif points <= 15:
    print("Genügend")
elif points <= 19:
    print("Befriedigend")
elif points <= 21:
    print("Gut")
elif points <= 24:
    print("Sehr Gut")
