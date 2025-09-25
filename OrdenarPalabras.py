"""

costos =   [ 100 ,  200,  300, 400 , 600 ,  800  ]
palabras = ["bbcab","jjb","cih","hij","lmk","asdfz"]


"""



# Es muy parecido a House Robber
# Tengo que elegir entre:
# bbcab + 0        jjb  +  min(anteriorPosible+0)     
# bacbb + 100      bbj  +  min(anteriorPosible+100)


def actualizarCosto(palabraAnterior, palabraAnteriorInv, costoAnterior, costoAnteriorInv, c, p):
  costo1 = costoAnterior + c
  costo2 = costoAnteriorInv + c
  if (palabraAnterior <= p and palabraAnteriorInv <= p):
    costo = min(costo1,costo2)
  elif (palabraAnterior <= p):
    costo = costo1
  elif (palabraAnteriorInv <= p):
    costo = costo2
  else:
    costo = float('inf')
  return costo





def elegir(palabraAnterior, palabraAnteriorInv, costoAnterior, costoAnteriorInv, c, p):
  costoAnteriorAux = costoAnterior
  costoAnterior = actualizarCosto(palabraAnterior, palabraAnteriorInv, costoAnterior, costoAnteriorInv, 0, p)
  costoAnteriorInv = actualizarCosto(palabraAnterior, palabraAnteriorInv, costoAnteriorAux, costoAnteriorInv, c, p[::-1])
  palabraAnterior = p
  palabraAnteriorInv = p[::-1]
  return palabraAnterior, palabraAnteriorInv, costoAnterior, costoAnteriorInv



def ordenarPalabras(palabras,costos):
  palabraAnterior    =  ""
  palabraAnteriorInv =  ""
  costoAnterior      =  0
  costoAnteriorInv   =  0

  for c, p in zip(costos, palabras):
    palabraAnterior, palabraAnteriorInv, costoAnterior, costoAnteriorInv = elegir(palabraAnterior,palabraAnteriorInv, costoAnterior, costoAnteriorInv, c, p)
  if costoAnterior == float('inf') and costoAnteriorInv == float('inf'):
      return -1
  else: return min(costoAnterior, costoAnteriorInv)






import sys


if __name__ == "__main__":
  n = int(sys.stdin.readline())
  costos = list(map(int, sys.stdin.readline().split()))
  palabras = [sys.stdin.readline().strip() for _ in range(n)]

  res = ordenarPalabras(palabras, costos)
  print(res)











