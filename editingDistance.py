def edit_distance(first_string, second_string):
    matriz = [[float('inf') for _ in range(len(first_string) + 1)] for _ in range(len(second_string) + 1)] 

    for i in range(len(first_string) + 1):
        matriz[0][i] = i

    for j in range(len(second_string) + 1):
        matriz[j][0] = j
    
    for i in range(1, len(first_string) + 1):
        for j in range(1, len(second_string) + 1):
            if first_string[i-1] != second_string[j-1]:  ## si son distintons el mínimo de los 3 de arriba a la izq +1
                matriz[j][i] = min(matriz[j-1][i], matriz[j][i-1], matriz[j-1][i-1]) + 1 
            else: ## sino copiar el de arriba a la izquierda
                matriz[j][i] = matriz[j-1][i-1]
        
    return matriz[len(second_string)][len(first_string)] 



if __name__ == "__main__":
    print(edit_distance(input(), input()))