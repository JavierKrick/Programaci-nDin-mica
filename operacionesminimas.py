#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:30:55 2024

@author: javier
"""

## adapte el algoritmo de la menda




def compute_operations(n):
    # Inicializamos la matriz para almacenar los costos mínimos
    matriz = [[float('inf') for _ in range(3)] for _ in range(n+2)] 
    secuencias = [[] for _ in range(n+1)]  # Almacenará las secuencias de operaciones

    matriz[1] = [0, 0, 0]  
    secuencias[1] = [1]

    for i in range(2, n+1):
        # Operación de restar 1
        min_cost = min(matriz[i-1])
        matriz[i][0] = min_cost + 1
        secuencias[i] = secuencias[i-1] + [i]

        # Operación de dividir por 2
        if i % 2 == 0:
            if matriz[i][0] > min(matriz[i//2]) + 1:
                matriz[i][0] = min(matriz[i//2]) + 1
                secuencias[i] = secuencias[i//2] + [i]

        # Operación de dividir por 3
        if i % 3 == 0:
            if matriz[i][0] > min(matriz[i//3]) + 1:
                matriz[i][0] = min(matriz[i//3]) + 1
                secuencias[i] = secuencias[i//3] + [i]

    return matriz[n][0], secuencias[n]




if __name__ == '__main__':
    input_n = int(input())
    min_operations, output_sequence = compute_operations(input_n)
    print(min_operations)
    print(*output_sequence)
