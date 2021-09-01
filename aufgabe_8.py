import math
i = 0
sidelengths = []
while i < 3:
    sides = ("a", "b", "c")
    sidelengths.append(input("Gibt einen Wert für Seite " + sides[i] + " ein!\n"))
    i += 1
cside = round(math.sqrt(pow(float(sidelengths[0]), 2) + pow(float(sidelengths[1]), 2)), 2)
if cside == round(float(sidelengths[2]), 2):
    print("Das Dreieck ist symetrisch")
else:
    print("Das Dreieck ist nicht symetrisch\nSeite c müsste", str(cside), "lang sein")