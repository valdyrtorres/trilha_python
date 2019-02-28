# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:22:57 2019

@author: f556085
"""

n = int(input("Digite um número inteiro positivo:"))
fatorial = lambda x: (x <= 1 and 1) or fatorial(x - 1) * x
    
print("O valor de {0}! é {1}".format(n, fatorial(n)))