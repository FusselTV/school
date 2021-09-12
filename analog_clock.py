hours = int(input("Gib einen Wert für Stunden ein: "))
minutes = int(input("Gib einen Wert für Minuten ein: "))
def computeHourHandAngle (hours, minutes):
    return 1 / 2 * (60 * hours + minutes)
def computeMinuteHandAngle (minutes):
    return 6 * minutes
hoursAngle = computeHourHandAngle(hours, minutes)
minutesAngle = computeMinuteHandAngle(minutes)
print(str(hours) + ":" + str(minutes), "Uhr:", "\n■ Stundenzeiger bei", str(hoursAngle) + "°\n■ Minutenzeiger bei", str(minutesAngle) + "°")
