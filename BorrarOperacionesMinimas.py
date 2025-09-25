#Pensar cuánto tardo en borrar es análogo a cuánto tardo en construir
# si tengo aaa tardo 1
# si tengo aaba debería tardar 2
# para simplificar puedo eliminar a los duplicados
# aaaaba = aba

# entonces si tengo abcda
# para la primera a s[i], ya gaste 1
# y luego queda un problema más pequeño que es ver el costo de lo que queda s[i+1]
# si me encontré con otra a me tengo que fijar si puedo usar una sola operación par aambas
# esto me abre distintas alternativas, y me tengo que quedar con la mínima
#voy guardando en memo




def recursion(i, j, s, memo):
    # i es desde,  j es hasta
    if i > j:
        return 0

    if (i, j) in memo:  #si ya lo tengo no lo calculo
        return memo[(i, j)]

    minimo = 1 + recursion(i + 1, j, s, memo)
    for k in range(i + 1, j + 1):
        if s[i] == s[k]:
            costoAlt = (recursion(i + 1, k, s, memo) + recursion(k + 1, j, s, memo))
            minimo = min(minimo, costoAlt)

    memo[(i, j)] = minimo  #guardo el minimo hasta el momento
    return minimo


def eliminarDuplicados(s,largo):
  if (largo == 0):
     return s
  else:
    sAux = s[0]
    for i in range(1,largo):
        if (s[i] != sAux[-1]):
            sAux = sAux + s[i]
    return sAux


def operacionesMinimas(s,largo):
  s = eliminarDuplicados(s,largo)
  memo = {}
  res = recursion(0,len(s)-1,s,memo)
  return res




def main():
  largo = int(input())
  s = input()
  resultado = operacionesMinimas(s,largo)
  print(resultado)

if __name__ == "__main__":
    main()