def Quersumme(input):
    calc = 0
    for i in str(input):
        calc = calc + int(i)
    return calc

def getNumberOfChar(inputString,positionString):
    alphabet = ["moin", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    return alphabet.index(inputString[positionString])

def pruefziffer(input):
    if len(input) == 12:
        input = input[:-1]
    letters = sum(c.isalpha() for c in input)
    if letters == 2:
        ergebnis = 7-(Quersumme(str(getNumberOfChar(input,0)) + str(getNumberOfChar(input,1)) + input[2:])%9)
    else:
        ergebnis = 8-(Quersumme(str(getNumberOfChar(input,0)) + input[1:])%9)
    if ergebnis == -1:
        ergebnis = 8
    if ergebnis == 0:
        ergebnis = 9
    return ergebnis

print(pruefziffer("PA3211621532"))
