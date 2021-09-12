from math import acos, sin, cos, pi
lat1 = float(input("Gebe einen Wert für den ersten Breitengrad ein: "))
lon1 = float(input("Gebe einen Wert für den ersten Längengrad ein: "))
lat2 = float(input("Gebe einen Wert für den zweiten Breitengrad ein: "))
lon2 = float(input("Gebe einen Wert für dem zweiten Längengrad ein: "))
def toRadians(degree):
    return (degree / float(180)) * float(pi)
def gpsDistanz(lat1, lat2, lon1, lon2):
    return (acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1))) * 6378.137
distance = gpsDistanz(toRadians(lat1), toRadians(lat2), toRadians(lon1), toRadians(lon2))
print("Die Luftlinie beträgt", round(distance, 3), "km")
