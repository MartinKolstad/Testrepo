# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 08:54:59 2022

@author: Martin
"""

import random


strategi1=0
strategi2=0

#Strategi 1
for i in range(1000):
    premie=random.randint(1,3)
    valg=random.randint(1,3)
    if valg==premie:
        strategi1+=1

#Strategi 2
for i in range(1000):
    premie=random.randint(1,3)
    valg=random.randint(1,3)
    #Tar bort et alternativ
    tavekk=random.randint(1,3)
    while tavekk==premie or tavekk==valg:
        tavekk=random.randint(1,3)
    #Velger på ny
    valg2=random.randint(1,3)
    while valg2==valg or valg2==tavekk:
        valg2=random.randint(1,3)
    valg=valg2
    if valg==premie:
        strategi2+=1

print(f"Du vant {strategi1} ganger med strategi 1")
print(f"Du vant {strategi2} ganger med strategi 2")