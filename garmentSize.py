bodysize = int(input())
chestsize = int(input())
def computeGarmentSizW(bodysize, chestsize):
    back = chestsize / 2 - 6
    if bodysize > 170:
        back = back * 2
    elif bodysize < 164:
        back = back / 2
    return back
def computeGarmentSize(bodysize, chestsize):
    back = chestsize / 2
    return back
garmentSize = computeGarmentSizW(bodysize, chestsize)
print(bodysize, "cm groß,", chestsize, "cm Brustumfang:", garmentSize)
