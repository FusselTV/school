"""
Calculation form https://www.omnicalculator.com/sports/elo
Make sure every Clan has 1400 Elo at start!
"""
from math import pow
K = 31 #constant K use 30 to make it like PvPGym

ratA = int(input("Gebe die Elo für SWA ein!\nElo: "))
ratB = int(input("Gebe die Elo für Heroes ein!\nElo: "))

print("\nWelcher Clan gewinnt? \n0 Damit Heroes mit", ratB, "Elo gewinnt\n1 Damit SWA mit", ratA, "Elo gewinnt")
score = int(input("Clan: ")) #0 means losing 1 means winning

expectedScore = 1 / (1 + pow(10,(ratB - ratA) / 400)) #see omnicalculator

newRatA = round((ratA + K * (score - expectedScore)),0) #round to avoid +0 for high elo players
newRatB = round((ratB + (ratA - newRatA)),0)

print("\nSWA hat nun", int(newRatA), "Elo!\nHeroes hat nun", int(newRatB), "Elo!")
