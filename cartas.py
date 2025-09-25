
def contarCantidadDeFavoritosPorFavorito(secuenciaDeFavoritos):
    conteoDeFavoritos = {}
    for n in secuenciaDeFavoritos:
        conteoDeFavoritos[n] = conteoDeFavoritos.get(n, 0) + 1
    listaDeFavoritos = list(conteoDeFavoritos)

    return conteoDeFavoritos, listaDeFavoritos

def contarCartasPorNumero(listaDeCartas):
    conteo_cartas = {}

    for n in listaDeCartas:
        conteo_cartas[n] = conteo_cartas.get(n, 0) + 1
    return conteo_cartas
      






def repartirCartas(listaDeCartas, secuenciaDeFavoritos, cantidadDeJugadores,alegrias,maximasCartasPorJugador):
  


    QdeFavoritos, listaDeFavoritos = contarCantidadDeFavoritosPorFavorito(secuenciaDeFavoritos)
    QporNumero = contarCartasPorNumero(listaDeCartas)
    res = 0



    for i in listaDeFavoritos:
        cantidadDeJugadores = QdeFavoritos[i]
        if i in QporNumero:
            totalDeCartas = QporNumero[i]
            res = res +obtenerAlegriaMaximaPorNumero(alegrias, totalDeCartas, cantidadDeJugadores,maximasCartasPorJugador)
    
    return res











    

  
def obtenerAlegriaMaximaPorNumero(alegrias, totalDeCartas, jugadores, maximasCartasPorJugador):


   
    tabla = []
    fil = jugadores + 1
    col = totalDeCartas + 1



    for _ in range(fil):
        nueva_fila = [0] * col
        tabla.append(nueva_fila)


    for j in range(jugadores):
        for cartasUsadas in range(totalDeCartas + 1):
            


            for cartasNuevas in range(maximasCartasPorJugador + 1):
                
                if cartasUsadas + cartasNuevas <= totalDeCartas:
                    if cartasNuevas < len(alegrias):
                        
                        actual = tabla[j][cartasUsadas] + alegrias[cartasNuevas]
                        
                        cartasTotales = cartasNuevas + cartasUsadas

                        if (actual > tabla[j + 1][cartasTotales]): #tomo el máximo
                            tabla[j+1][cartasTotales] = actual

    return tabla[jugadores][totalDeCartas]


      

  


  

"""


alegría          10    20     30     45
              
primeraCarta  :  10    20     30     45
segundaCarta  :        20     30     40/45  ?? 
tengo que fijarme los distintos caminos, no es greedy

me fijo en el primer Jugador y lo comparo con todos los del segundo (conlos resultados que ya calculé del primero)


        
"""

"""
jugadores = 5
maximasCartasPorJugador = 5
cartas = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
favoritos = [1,2,3,4,5]
alegrias = [0, 10,20,30,40,50]

"""
"""
jugadores = 2
maximasCartasPorJugador = 2
cartas = [2,1,2,1]
favoritos = [1,1]
alegrias = [0,10,20]
"""
"""
jugadores = 3
maximasCartasPorJugador = 4
cartas = [1,1,1,1,1,1,1,1,1,2,2,2]
favoritos = [1,1,1]
alegrias = [0,110,120,130]
"""

"""
res = repartirCartas(cartas,favoritos,jugadores,alegrias,maximasCartasPorJugador)
print(res)
"""


if __name__ == "__main__":
    jugadores, maximasCartasPorJugador = map(int, input().split())
    cartas = list(map(int, input().split()))
    favoritos = list(map(int, input().split()))
    h = list(map(int, input().split()))
    alegrias = [0] + h
    res = repartirCartas(cartas,favoritos,jugadores,alegrias,maximasCartasPorJugador)
    print(res)
