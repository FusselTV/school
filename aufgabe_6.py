year = int(input("Bitte Jahres Zahl eingeben!\n"))
if year % 400 == 0:
    print("Das Jahr", year, "ist ein Schaltjahr")
    exit()
if year % 4 == 0 and year % 100 != 0:
    print("Das Jahr", year, "ist ein Schaltjahr")
else:
    print("Das Jahr", year, "ist kein Schaltjahr")