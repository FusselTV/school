humanAge = int(input("Hundealter in Jahren eingeben (1-∞)\n"))
dogAge = 14
if humanAge == 2:
    dogAge = 22
elif humanAge > 2:
    dogAge = humanAge * 5 + 12
print("Der ist", dogAge, "Hundjahre alt")