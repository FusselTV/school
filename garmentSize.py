bodysize = int(input("Gib die Größe ein: "))
chestsize = int(input("Gib den Brustumfang an: "))
gender = (input("Gib ein Geschlecht ein: "))
def computeGarmentSiz(bodysize, chestsize, gender):
    if gender == "w" or "weiblich":
        back = chestsize / 2 - 6
        if bodysize > 170:
            back = back * 2
        elif bodysize < 164:
            back = back / 2
        return back
    return chestsize / 2
garmentSize = computeGarmentSiz(bodysize, chestsize, gender)
print(bodysize, "cm groß,", chestsize, "cm Brustumfang:", garmentSize)
