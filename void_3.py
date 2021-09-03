integer = int(input("Ganzzahl eingeben: "))
normalints = list(range(2, integer, 1))
normalints = [i for i in normalints if i%2 == 0]
print(normalints)
