i = 0
numbers = ["erste", "zweite", "dritte"]
while i < 3:
    numbers[i] = int(input("Gibt die " + numbers[i] + " Zahl ein: ")) # int() is very important lulW
    i += 1
print("\nDie größte Zahl ist " + str(max(numbers)) + "!")
