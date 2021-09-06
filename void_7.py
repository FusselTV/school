numbers = []
val = 0
numbers = list(range(1, int(input("Zahl eingeben: "))+1 ))
for x in numbers:
    val = val + (numbers[x-1])
print("Das Ergebnis ist", str(val))
