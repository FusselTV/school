name = input("Bitte geben Sie Ihren Namen ein: ")
gender = input("Bitte geben Sie ihr Geschlecht ein: ")
if gender == "weiblich":
    salutation = "Frau"
else:
    salutation = "Herr"
print("\nGuten Tag", salutation, name)
