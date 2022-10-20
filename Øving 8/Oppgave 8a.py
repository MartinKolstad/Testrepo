# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:19:33 2022

@author: Martin
"""

#Svar på oppgave 8a-h

class Land:
    #Konstruktør
    def __init__ (self, navn, befolkning=0, areal=0):
        self.navn=navn
        self.befolkning=befolkning
        self.areal=areal
    
    def __str__ (self):
        return f"Land: {self.navn}, Befolkning: {self.befolkning}, Areal: {self.areal}"
    @property
    def befolkningstetthet(self):
        b=float(self.befolkning)
        a=float(self.areal)
        tetthet=b/a
        return tetthet
    
def flest(land1, land2):
    if land1.befolkning>land2.befolkning_:
        return land1
    else:
        return land2

bef=open("befolkning_tabell_csv.txt", "r", encoding="UTF8")
areal=open("areal_tabell_csv.txt", "r", encoding="UTF8")

landliste=dict()

for linje in bef:
    foring=linje.split(";")    
    landliste[foring[0]]=Land(foring[0],foring[1])

bef.close()

for linje in areal:
    funnet=False
    foring=linje.split(";")
    for land in landliste:
        if land==foring[0]:
            landliste[land].areal=foring[1]
            funnet=True
            continue
    if funnet==False:
        print(f"Finner ikke {foring[0]} i denne listen")
        
areal.close()

#Lagrer landene med og uten satt areal i hver sin dictionary
begge=dict()
mangler=dict()

for land in landliste:
    if landliste[land].areal !=0:
        begge[land]=landliste[land]
    else:
        mangler[land]=landliste[land]

print("Disse landene har satt både befolkning og areal:")
for land in begge:
    print(begge[land], end="")
    print(f"Befolkningstetthet: {begge[land].befolkningstetthet:6.2f}")
    print("")

print("Disse landene har ikke satt areal:")
for land in mangler:
    print(land)

#Finner landet med høyest befolkningstetthet
hoyesttetthet=0
for land in begge:
    if begge[land].befolkningstetthet > hoyesttetthet:
        hoyesttetthet=begge[land].befolkningstetthet
        htland=land

print("")
print(f"Landet med høyest befolkningstetthet er {begge[htland].navn}")
print(f"Dette landet har befolkningstetthet på: {hoyesttetthet:6.2f}")

#Legger på en kommentar til slutt




