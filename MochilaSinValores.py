#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 05:14:05 2024

@author: javier
"""

from sys import stdin


def maximum_gold(capacity, weights):
    barras = len(weights)
    
    weights.sort()  # Ordeno de manera ascendente
    
    matriz = [[0 for _ in range(capacity + 1)] for _ in range(barras)]
    
    for j in range(barras):
        matriz[j][0] = 0    # La primer columna es 0

    for j in range(1, capacity + 1):
        if weights[0] <= j:
            matriz[0][j] = weights[0]   # Escribo la primer fila
        else:
            matriz[0][j] = 0
        
    for i in range(1, barras):
        for j in range(1, capacity + 1):
            peso = weights[i]
            if peso <= j:
                matriz[i][j] = max(matriz[i-1][j], peso + matriz[i-1][j-peso])
            else:
                matriz[i][j] = matriz[i-1][j]
    
    return matriz[barras-1][capacity]



if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
    
    
    
    