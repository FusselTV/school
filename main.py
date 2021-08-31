aufgabe = input('Gib die Aufgaben Nummer ein\n')
if aufgabe == "1":
    import aufgabe_1
elif aufgabe == "2":
    import aufgabe_2
elif aufgabe == "3":
    import aufgabe_3
elif aufgabe == "4":
    import aufgabe_4
elif aufgabe == "5":
    import aufgabe_5
else:
    print("falsche Eingabe")