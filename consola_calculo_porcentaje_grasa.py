# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:51:42 2023

@author: John Pardo
"""

import calculadora_indices as calc

print("En esta funcion se va a Calcula el porcentaje de grasa de una persona a partir de la informacion recibida.")


peso = float(input("Ingrese el peso de la persona (en Kilogramos):   "))

altura = float(input("Ingrese la altura de la persona (en centimetros):   "))

edad = int(input("Ingrese la edad de la persona (en años):   "))

valor_genero = float(input("Ingrese en caso de ser masculino 10.8 y en caso de ser femenino 0:   "))

resultado = str(calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero))

print(resultado + " %")
