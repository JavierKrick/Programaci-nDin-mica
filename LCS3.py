#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 01:56:16 2024

@author: javier
"""

def lcs3(first_string, second_string, third_string):
    # Crear la matriz 3D
    matriz = [[[0 for _ in range(len(third_string) + 1)] 
               for _ in range(len(second_string) + 1)] 
               for _ in range(len(first_string) + 1)]

    # Rellenar la matriz
    for i in range(1, len(first_string) + 1):
        for j in range(1, len(second_string) + 1):
            for k in range(1, len(third_string) + 1):
                if first_string[i-1] == second_string[j-1] == third_string[k-1]:  # Si los caracteres coinciden
                    matriz[i][j][k] = matriz[i-1][j-1][k-1] + 1
                else:  # Si no coinciden, tomar el máximo de las opciones
                    matriz[i][j][k] = max(matriz[i-1][j][k], matriz[i][j-1][k], matriz[i][j][k-1])

    
    return matriz[len(first_string)][len(second_string)][len(third_string)]





if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))