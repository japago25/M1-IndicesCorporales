# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:51:42 2023

@author: John Pardo
"""

import calculadora_indices as calc

print("En esta funcion se va a culcular la cantidad de calorias recomendadas que una persona debe consumir a diario, en caso de que desee adelgazar")


peso = float(input("Ingrese el peso de la persona (en Kilogramos):   "))

altura = float(input("Ingrese la altura de la persona (en centimetros):   "))

edad = int(input("Ingrese la edad de la persona (en años):   "))

valor_genero = float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer:   "))

resultado = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)

print(resultado)