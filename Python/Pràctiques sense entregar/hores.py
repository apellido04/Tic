#coding=utf-8
from __future__ import print_function
from pickle import FALSE

run = True
primer = True
segon = False
tercer = False

while primer == True:
    print("Introdueix el primer temps")
    hores1 = int(input("Hores: "))
    if hores1 > 24:
        print("Fora de rang!")
        continue
    minuts1 = int(input("Minuts: "))
    if minuts1 > 60:
        print("Fora de rang!")
        continue
    segons1 = int(input("Segons: "))
    if segons1 > 60:
        print("Fora de rang!")
        continue
    segon = True
    primer = False

while segon == True:
    print("Introdueix el segon temps")
    hores2 = int(input("Hores: "))
    if hores2 > 24:
        print("Fora de rang!")
        continue
    minuts2 = int(input("Minuts: "))
    if minuts2 > 60:
        print("Fora de rang!")
        continue
    segons2 = int(input("Segons: "))
    if segons2 > 60:
        print("Fora de rang!")
        continue
    tercer = True
    segon = False

while tercer == True:
    print("Introdueix el tercer temps")
    hores3 = int(input("Hores: "))
    if hores3 > 24:
        print("Fora de rang!")
        continue
    minuts3 = int(input("Minuts: "))
    if minuts3 > 60:
        print("Fora de rang!")
        continue
    segons3 = int(input("Segons: "))
    if segons3 > 60:
        print("Fora de rang!")
        continue
    tercer = False

hores = hores1 + hores2 + hores3
minuts = minuts1 + minuts2 + minuts3
segons = segons1 + segons2 + segons3
    
print(hores, minuts, segons)
    
def converteix_a_segons(h, m, s):
    return h * 3600 + m * 60 + s


def temps(s):
    #s = s % 3600
    global hores_totals
    hores_totals = s // 3600
    s %= 3600
    global minuts_totals
    minuts_totals = s // 60
    global segons_totals
    segons_totals = s % 60
    return hores_totals, minuts_totals, segons_totals


segons_total = converteix_a_segons(hores, minuts, segons)
print(segons_total)
print(segons)
temps_complet = temps(segons)
print(temps_complet)

print("Temps total: ", hores, "hores,", minuts, "minuts,", "i", segons, "segons")


