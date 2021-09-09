numbers = []
i = 0
lastval = 0
val = int(0)
numbers = list(range(1, int(input("Zahl eingeben: "))))
while int(val) < numbers[-1]:
    lastval = val
    val = val + (numbers[i])
    i += 1
print("Das Ergebnis ist", lastval, "\nDie Zahlen waren:", numbers)
