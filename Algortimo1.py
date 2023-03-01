#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
#************************************************************
# Algoritmo1.py
#
# Asignatura : Algoritmos en Bioinformatica
#
# Algoritmo Tema 1
#
Aplicación del empalme de secuencias
#
# Autora: Qinding Xie
# Fecha: 27/02/2023
#
#************************************************************
'''


import os, time, functools

# Empeza
startTime = time.time()

# Leer fechiro
with open("Secuencias_2023.fa.fa", "rt", encoding="utf8") as f:
    datas = [each.strip() for each in f.readlines()]
    datas = list(filter(lambda x:len(x) > 6, datas))

def join(str1, str2):
    result = None
    # Obtener la longitud de la cadena más corta
    minLength = len(str1) if len(str1) < len(str2) else len(str2)

    # Detección de discordancias para obtener 
    # la cadena repetida más larga
    for i in range(1, minLength+1):
        a = str1[-i:]
        b = str2[:i]
        if a == b:
            result = b

    # Si el resultado está presente y es mayor que 11, se desduplica
    #  y se empalma posteriormente, de lo contrario se descarta str2.
    if result and len(result) > 11:
        return str1 + str2[len(result):], len(result) if result else 0, result
    else:
        return str1, len(result) if result else 0, result

def enum(first:str, other:list) -> (str, int):
    result = []
    for each in other:
        result.append(join(first, each))

    a = max(result, key=lambda x:x[1])
    # print(a)
    if first == a[0]:
        return a[0], None
    else:
        return a[0], result.index(a)

result = datas.pop(0)
i = 0
while datas:
    result, index = enum(result, datas)
    if index is None:
        datas.append(result)
        result = datas.pop(0)
        i += 1
        if i == len(datas):
            datas.append(result)
            break
        continue
    i = 0
    #print(result)
    datas.pop(index)



for each in datas:
    print(each)
    print("\n")



print(f"Se ejecuta durante un total de {time.time() - startTime}segundos")

input()