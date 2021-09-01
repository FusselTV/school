import math
i = 0
sides = ["a", "b", "c"]
while i < 3:
    sides[i] = input("Gibt einen Wert für Seite " + sides[i] + " ein: ")
    i += 1
cside = round(math.sqrt(pow(float(sides[0]), 2) + pow(float(sides[1]), 2)), 2)
if cside == round(float(sides[2]), 2):
    print("\nDas Dreieck ist symetrisch")
else:
    print("\nDas Dreieck ist nicht symetrisch!\nTipp: Seite c müsste", str(cside), "lang sein")
