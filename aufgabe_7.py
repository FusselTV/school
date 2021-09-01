i = 0
timeinput = []
while i < 3:
    timetypes = ("Stunden", "Minuten", "Sekunden")
    timeinput.append(input("Gibt einen Wert für " + timetypes[i] + " ein!\n"))
    i += 1
seconds = int(timeinput[0]) * 3600 + int(timeinput[1]) * 60 + int(timeinput[2]) + int(input("Wie viele Sekunden addieren?\n"))
realhours = int(seconds / 3600)
realminutes = (seconds % 3600) / 60
realseconds = int((realminutes % 1) * 60)
realminutes = int(realminutes)
print(f"{realhours:02}:{realminutes:02}:{realseconds:02}")