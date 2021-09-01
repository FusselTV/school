month = input("geben Sie einen Monat ein: ")
days30 = ("April", "Juni", "September", "November")
days28 = "Februar"
if month in days30:
    print("\nDer", month, "ist 30 Tage lang!")
elif month in days28:
    print("\nDer", month, "ist 28 Tage lang!")
else:
    print("\nDer", month, "ist 31 Tage lang!")
