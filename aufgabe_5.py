dogAge = 14
humanAge = int(input("Hundealter in Jahren eingeben (1-∞): "))
if humanAge == 2:
    dogAge = 22
elif humanAge > 2:
    dogAge = humanAge * 5 + 12
print("\nDer ist Hund ", dogAge, "Hundjahre alt!")
