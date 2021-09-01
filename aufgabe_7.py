i = 0
timeinput = ["Stunden", "Minuten", "Sekunden"]
while i < 3:
    timeinput[i] = input("Gibt einen Wert für " + timeinput[i] + " ein: ")
    i += 1
seconds = int(timeinput[0]) * 3600 + int(timeinput[1]) * 60 + int(timeinput[2]) + int(input("Wie viele Sekunden addieren: "))
realhours = int(seconds / 3600)
realminutes = (seconds % 3600) / 60
realseconds = int((realminutes % 1) * 60)
realminutes = int(realminutes)
print(f"\nEs ist {realhours:02}:{realminutes:02}:{realseconds:02} Uhr!")
