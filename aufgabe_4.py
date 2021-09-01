a = 0
list = []
while a < 3:
    list.append(input("Gibt eine Zahl " + str(a) + " ein!\n"))
    a += 1
print("Die größte Zahl ist", max(list))