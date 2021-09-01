task = input('Gib die Aufgaben Nummer ein\n')
if task == "1":
    import aufgabe_1
elif task == "2":
    import aufgabe_2
elif task == "3":
    import aufgabe_3
elif task == "4":
    import aufgabe_4
elif task == "5":
    import aufgabe_5
elif task == "6":
    import aufgabe_6
else:
    print("Die Aufgabe ist nicht verfügbar!")