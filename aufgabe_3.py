try:
    i = 1
    grade = 6
    points = int(input("Bitte Notenpunkte eingeben: "))
    if points in list(range(0, 14)):
        while i <= points:
            i += 3
            grade -= 1
        print(points, "Notenpunkte entspricht der Note", grade)
    else:
        ex
except:
    print("Error")
