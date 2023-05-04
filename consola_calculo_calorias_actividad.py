# -*- coding: utf-8 -*-

"""
Created on Fri Apr 14 16:51:42 2023

@author: John Pardo
"""

import calculadora_indices as calc

print("En esta funcion se va a culcular la cantidad de calorías que una persona quema al realizar algún tipo de actividad física (esto es, su tasa metabólica basal según actividad física), a partir de la informacion recibida.")


peso = float(input("Ingrese el peso de la persona (en Kilogramos):   "))

altura = float(input("Ingrese la altura de la persona (en centimetros):   "))

edad = int(input("Ingrese la edad de la persona (en años):   "))

valor_genero = float(input("Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer:   "))

print("\nValor que depende de la actividad física semanal:\n   • 1.2: poco o ningún ejercicio\n   • 1.375: ejercicio ligero (1 a 3 días a la semana)\n   • 1.55: ejercicio moderado (3 a 5 días a la semana)\n   • 1.725: deportista (6 -7 días a la semana)\n   • 1.9: atleta (entrenamientos mañana y tarde)")

valor_actividad = float(input())


resultado = str(calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad))

print(resultado + " cal")