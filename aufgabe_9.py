points = ["x", "y"]
i = 0
section = int(1)
while i <= 1:
    points[i] = (input("Gib den " + points[i] + "-Wert ein: "))
    i += 1
if "-" in points[0]:
    section += 1
if "-" in points[1]:
    section += 1
if int(points[0]) >= 0 and "-" in points[1]:
    section = 4
print("\nDer Punkt (" + str(points[0]) + "|" + str(points[1]) + ") ist in Abschnitt " + str(section) +"!")
