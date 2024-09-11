
import numpy as np

## Arma una lista con los indices y las longitudes hasta el momento de las subsecuencias mas largas ()

def subSecuenciaAsc(lista, n):
    longitudAsc = [1] * n
    indicesAsc = [[-1] for _ in range(n)]  # Inicializamos con listas que contengan -1
    
    for i in range(1, n):
        for j in range(0, i):
            if lista[j] < lista[i]:
                if longitudAsc[j] + 1 > longitudAsc[i]:
                    longitudAsc[i] = longitudAsc[j] + 1
                    indicesAsc[i] = [j]  # Reiniciamos la lista con el nuevo índice
                elif longitudAsc[j] + 1 == longitudAsc[i]:
                    indicesAsc[i].append(j)  # agregamos el nuevo
    
    return longitudAsc, indicesAsc





def subSecuenciaDesc(lista, n):
    longitudDesc = [1] * n
    indicesDesc = [[-1] for _ in range(n)]  # Inicializamos con listas que contengan -1
    
    for i in range(1, n):
        for j in range(0, i):
            if lista[j] > lista[i]:
                if longitudDesc[j] + 1 > longitudDesc[i]:
                    longitudDesc[i] = longitudDesc[j] + 1
                    indicesDesc[i] = [j]  # Reiniciamos la lista con el nuevo índice
                elif longitudDesc[j] + 1 == longitudDesc[i]:
                    indicesDesc[i].append(j)  # Añadimos el índice relevante a la lista
    
    return longitudDesc, indicesDesc





def valorEIndiceMax(longitudAsc,n):
    
    indicesMax = []
    valorMax = longitudAsc[0]
    
    for i in range(0, n):
        if longitudAsc[i] > valorMax:
            valorMax = longitudAsc[i]
            indicesMax = [i]  # Reinicio
        elif longitudAsc[i] == valorMax:
            indicesMax.append(i)  # Agrego el índice si tiene el valor máximo igual
    
    return (indicesMax, valorMax)



#Bueno, acá tengoq ue reconstruir las secuencias máximas, voy a usar memonization o como se llame
## De eesta manera no calculo todo dos veces.
## si tengo [1, 2,5] [1 , 3, 5] tengo que poder reconstruir ambas desde el 5
## Desde el 5 tengo que poder reconstruir todo 
## Lo armo de manera recursiva
## Si lo calculé, devolverlo, y sino, calcular una iteración más abajo



def construirSecuencia(indice, indicesAsc, memo):
    if indice == -1:
        return [set()]

    # Si ya calculaste las subsecuencias para este índice, las devuelves
    if memo[indice] is not None:
        return memo[indice]

    subsecuencias = []
    for anterior in indicesAsc[indice]:
        for subsecuencia in construirSecuencia(anterior, indicesAsc, memo):
            nueva_subsecuencia = subsecuencia.copy()
            nueva_subsecuencia.add(indice)
            subsecuencias.append(nueva_subsecuencia)

    # Guarda las subsecuencias que salen de este número
    memo[indice] = subsecuencias
    return subsecuencias

def indicesDeLaSubSecs(indicesMax, indicesAsc, n):
    # Matriz para almacenar subsecuencias ya calculadas
    memo_matrix = np.array([None] * n)

    secuencias = []
    for indice in indicesMax:
        secuencias.extend(construirSecuencia(indice, indicesAsc, memo_matrix))

    return secuencias







def subsecuenciasAD(n,lista):
    

    
    if (n <= 1): return 0 #hay una función que llama desde n+1
    
    ## Tengo que evitar los casos donde el hecho de que las subsecuecnias más largas tengan repetidos,
    ## Osea si comparten números
    ## Haga que haya una combinación donde puedo pintar más
    ## Si hay un numero repetido, sólo puede haber un único numero repetido
    ## Esto se debe a que si a5 = d5  entonces los demás numeros son distintos porque una era ascendente 
    ## y la otra ascendente
    ## Osea sólo tengo que revisar si los que tienen los valores máximos tienen algun repetido
    
    ## Como resolver lo de los repetidos:
    ## Si hay dos repetidos, entonces en el ascendente tiene que agarrar uno, y en el descendente tiene que agarrar el otro
    ## puedo hacer que en el primero agarre la primer aparición y en el segundo la ultima aparcición.
    # En el descendente cambia el codigo y agarra la ultima aparicion del numero si tengo 4 4 4 agarra el ultimo 4 como indice

                
    #imero agarre la primer aparición y en el segundo la ultima aparcición.
    # En el descendente cambia el codigo y agarra la ultima aparicion del numero si tengo 4 4 4 agarra el ultimo 4 como indice

                
    
    
    
    longitudAsc = []
    indicesAsc = []
    longitudAsc, indicesAsc = subSecuenciaAsc(lista,n)
    
    longitudDesc = []
    indicesDesc = []
    longitudDesc, indicesDesc = subSecuenciaDesc(lista, n)
    

    
                    
    ## Ahora tengo que evitar los casos donde el hecho de que las subsecuecnias más largas tengan repetidos,
    ## Osea si comparten números
    ## Haga que haya una combinación donde puedo pintar más
    ## Si hay un numero repetido, sólo puede haber un único numero repetido
    ## Esto se debe a que si a5 = d5  entonces los demás numeros son distintos porque una era ascendente 
    ## y la otra ascendente
    ## Osea sólo tengo que revisar si los que tienen los valores máximos tienen algun repetido
    
    
    #busco los indices de las máximas secuencias (pueden haber muchas)
    
    indicesMax, valorMax = valorEIndiceMax(longitudAsc,n)
    
    indicesMin, valorMin = valorEIndiceMax(longitudDesc,n)
    





    ## Acá ya puedo tener una respuesta provisoria, si llegan a compartir un número después resto 1
    pintados = valorMax + valorMin  
                                            
    

    
    
    ## Armo listas con los indices, el objetivo final es ver si hay alguna lista sin repetidos
    
    
    iSubsecsAsc = indicesDeLaSubSecs(indicesMax,indicesAsc,n)
    iSubsecsDesc = indicesDeLaSubSecs(indicesMin,indicesDesc,n)
    
    
    
    
    longitudAsc = []
    indicesAsc = []
    longitudAsc, indicesAsc = subSecuenciaAsc(lista,n)
    
    longitudDesc = []
    indicesDesc = []
    longitudDesc, indicesDesc = subSecuenciaDesc(lista, n)
    

    
                    
    ## Ahora tengo que evitar los casos donde el hecho de que las subsecuecnias más largas tengan repetidos,
    ## Osea si comparten números
    ## Haga que haya una combinación donde puedo pintar más
    ## Si hay un numero repetido, sólo puede haber un único numero repetido
    ## Esto se debe a que si a5 = d5  entonces los demás numeros son distintos porque una era ascendente 
    ## y la otra ascendente
    ## Osea sólo tengo que revisar si los que tienen los valores máximos tienen algun repetido
    
    
    #busco los indices de las máximas secuencias (pueden haber muchas)
    
    indicesMax, valorMax = valorEIndiceMax(longitudAsc,n)
    
    indicesMin, valorMin = valorEIndiceMax(longitudDesc,n)
    





    ## Acá ya puedo tener una respuesta provisoria, si llegan a compartir un número después resto 1
    pintados = valorMax + valorMin  
                                            
    

    
    
    ## Armo listas con los indices, el objetivo final es ver si hay alguna lista sin repetidos
    
    
    iSubsecsAsc = indicesDeLaSubSecs(indicesMax,indicesAsc,n)
    iSubsecsDesc = indicesDeLaSubSecs(indicesMin,indicesDesc,n)
    

    

    
    

    
    # Verificar si alguna combinación de secuencias no tiene elementos repetidos ¿Se podrá optimizar con programación Dinámica?
    # Y BackTracking??
    hayRep = True
    for conjAsc in iSubsecsAsc:
        for conjDesc in iSubsecsDesc:
            if (conjAsc &  conjDesc == set()):
                hayRep = False
                break
        if (hayRep == False):
            break
            
    if (hayRep == True):
        pintados = pintados-1
    

    respuesta = n-pintados
    
 
    return respuesta



i = 0
actual = 0
n = 0
while True:
    # Tipo de Input
    if i % 2 == 0:
        actual = int(input())
        if actual == -1:
            break
        else:
            n = actual
    else:
        lista = list(map(int, input().split()))
        print(subsecuenciasAD(n, lista))
    i += 1




