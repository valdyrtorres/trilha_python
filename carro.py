# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:22:36 2018

@author: Valdir
"""

class Carro(object):
    
    # Construtor
    def __init__(self, cor, potencia):
        self.cor = cor
        self.potencia = potencia
        self._velocidade = 0
        
    def __atualiza_velocidade(self, valor):
        self._velocidade = valor
        
    def acelerar(self):
        self.__atualiza_velocidade(valor=10)
        print("Vrummm")
        
    def freiar(self):
        self.__atualiza_velocidade(valor=0)
        print("parando")

