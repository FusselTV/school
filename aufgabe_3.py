try:
    points = int(input("Bitte Notenpunkte eingeben\n"))
    if points in list(range(0, 14)):
    #if points >= 0 and points <= 13:
        if points > 11:
            grade = 1
        elif points > 9:
            grade = 2
        elif points > 6:
            grade = 3
        elif points > 3:
            grade = 4
        elif points > 0:
            grade = 5
        else:
            grade = 6
        print("Note", grade)
    else:
        print("####")
except:
    print("####")