year = int(input("Bitte Jahres Zahl eingeben: "))
if year % 400 == 0:
    print("\nDem Jahr", year, "wird ein Schalttag hinzugefügt!")
    exit()
if year % 4 == 0 and year % 100 != 0:
    print("\nDas Jahr", year, "ist ein Schaltjahr!")
else:
    print("\nDas Jahr", year, "ist kein Schaltjahr!")
