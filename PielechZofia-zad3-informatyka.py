# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 1
b = 9
suma = 0
i = 0

if a % 2 == 0:
    a = a + 1 
    print (a)
else:
    print (a)
while a <= b:
    suma = suma + a
    i = i + 1
    a = a + 2
srednia = suma / i
print (srednia)