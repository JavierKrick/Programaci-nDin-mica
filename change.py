def change(n):
    monedas = [1,3,4]
    lista = list(range(n+1))
    lista[0]=0
    for moneda  in monedas:
        for i in range(moneda, n+1):
            lista[i] = min(lista[i], lista[i - moneda] + 1) ##sería el mínimo entre lo que tengo
                                                        ## en este momento o sumarle 1 moneda a una moneda restada.
                    
    return lista[n]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
    
    

