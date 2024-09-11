#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 06:07:44 2024

@author: javier
"""

def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def MinAndMax(i, j, m, M, operators):
    min_value = float('inf')
    max_value = float('-inf')
    for k in range(i, j):
        a = evaluate(M[i][k], M[k+1][j], operators[k])
        b = evaluate(M[i][k], m[k+1][j], operators[k])
        c = evaluate(m[i][k], M[k+1][j], operators[k])
        d = evaluate(m[i][k], m[k+1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value



def maximum_value(dataset):
    n = len(dataset) // 2 + 1
    digitos = [int(dataset[i]) for i in range(0, len(dataset), 2)]
    operaciones = [dataset[i] for i in range(1, len(dataset), 2)]

    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]

    for i in range(n):
        m[i][i] = digitos[i]
        M[i][i] = digitos[i]

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, m, M, operaciones)

    return M[0][n-1]




if __name__ == "__main__":
    print(maximum_value(input()))