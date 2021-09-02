i = 0
inputval = ["startwert PS", "endwert PS", "Schrittweite"]
while i < 3:
    inputval[i] = input("Gib einen Wert für " + inputval[i] + " ein: ")
    i += 1
ps = list(range(int(inputval[0]), int(inputval[1]) + 1, int(inputval[2])))
kw = [x / 1.35962 for x in ps]
kw = [round(x, 2) for x in kw]
i = 0
while i < len(ps):
    print(str(ps[i]) + " PS sind " + str(kw[i]) + " kW")
    i += 1
