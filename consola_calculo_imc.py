# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:51:42 2023

@author: John Pardo
"""

import calculadora_indices as calc

print("En esta funcion se va a calcula el índice de masa corporal de una persona apartir de la informacion recibida")


peso = float(input("Ingrese el peso de la persona (en Kilogramos):   "))

altura = float(input("Ingrese la altura de la persona (en centimetros):   "))

resultado = calc.calcular_IMC(peso, altura)

print(resultado)