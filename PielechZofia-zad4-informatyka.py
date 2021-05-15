# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

lista=[8,9,3,12,1]
print (lista)
n= len(lista)

for b in range (0,n-1):
    for j in range (b+1,n):
        print ('j:',j)
        if lista [b] > lista [j]:
                pom = lista[b]
                lista [b] = lista[j] 
                lista [j]= pom
print (lista)