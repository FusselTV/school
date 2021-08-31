month = input("geben Sie einen Monat ein:")
list30 = ("April", "Juni", "September", "November")
list28 = "Februar"
if month in list30:
    print("Der", month, "ist 30 Tage lang")
elif month in list28:
    print("Der", month, "ist 28 Tage lang")
else:
    print("Der", month, "ist 31 Tage lang")
