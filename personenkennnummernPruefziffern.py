def replaceChars(text, dictonary):
    for key in dictonary.keys():
        text = text.upper().replace(key, dictonary[key])
    return text

def removeDigits(string):
    return ''.join([i for i in string if not i.isdigit()])

def removeChars(string):
    return ''.join(filter(str.isdigit, string))

def checkNumber(input):
    try:
        test = input.split("-")
        letterDic = {
        "A": "12","B": "14","C": "16","D": "18","E": "20","F": "22","G": "24","H": "26","I": "28","J": "6","K": "8","L": "10","M": "12","N": "14","O": "16","P": "18","Q": "20","R": "22","S": "4","T": "6","U": "8","V": "10","W": "12","X": "14","Y": "16","Z": "18",}
        if len(test) != 3:
            return "Gebe drei Elemente die durch - getrennt sind ein"
        if len(test[0]) != 6 or not test[0].isdigit():
            return "Gebe eine Datum mit folgenden Format ein DDMMYY"
        elif len(test[1]) != 1 or test[1] not in letterDic:
            return "Gebe 1. Buchstabe des Geburtsnamens ein (Großbuchstabe)"
        elif len(test[2]) != 4 or not test[2].isdigit():
            return "Gebe eine KWEA Kennziffer und eine vortlaufende einstellige Zahl ein"
        
        i = 0
        produktGewichtung = 0
        onlyNumberInput = removeChars(input)
        gewichtung = [2,3,4,5,6,7,6,7,2,3]
        while i < len(onlyNumberInput):
            produktGewichtung = int(onlyNumberInput[i]) * int(gewichtung[i]) + produktGewichtung
            i+= 1
        pruefziffer = 11 - ((produktGewichtung + int(removeChars(replaceChars(removeDigits(input), letterDic)))) % 11)
        if pruefziffer == 10:
            return input + "-0"
        if pruefziffer == 11:
            return input + "-1"
        else:
            return input + "-" + str(pruefziffer)
    except:
        return "Fehler"
        
input = ["988979-M-9434"]
for x in input:
    print(checkNumber(x))
