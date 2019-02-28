# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:02:30 2019

@author: f556085
"""

n = int(input("Digite um número inteiro positivo:"))
i = 1
n_fat = 1
while i <= n:
    n_fat = n_fat * i
    i += 1
    
print("O valor de {0}! é {1}".format(n, n_fat))