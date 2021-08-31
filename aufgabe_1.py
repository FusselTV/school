name = input("Bitte geben Sie Ihren Namen ein:\n")
gender = input("Bitte geben Sie ihr Geschlecht ein:\n")
if gender == "weiblich":
    salutation = "Frau"
else:
    salutation = "Herr"
print("Guten Tag", salutation, name)
