intinput = []
while "0" not in intinput:
    intinput.append(input("Gibt eine Zahl ein: "))
print("\nEs wurden", str(len(intinput)-1), "Zahlen eingegeben", "\nDie größte Zahl ist", str(max(intinput)), "\nDie kleinste Zahl ist",min(intinput[:-1]))
