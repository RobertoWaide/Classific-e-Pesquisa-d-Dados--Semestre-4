def iterativa(arr, elemento):
    inicio = 0
    fim = len(arr) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if arr[meio] == elemento:
            return meio 
        elif arr[meio] < elemento:
            inicio = meio + 1 
        else:
            fim = meio - 1  

    return -1 


def recursiva(arr, elemento, inicio, fim):
    if inicio > fim:
        return -1 

    meio = (inicio + fim) // 2
    if arr[meio] == elemento:
        return meio 
    elif arr[meio] < elemento:
        return recursiva(arr, elemento, meio + 1, fim) 
    else:
        return recursiva(arr, elemento, inicio, meio - 1) 


def main():
    array = [1, 3, 5, 7, 9, 11, 13, 15]
    elemento = int(input("- "))

    print(f"Elemento encontrado na posição {iterativa(array, elemento)} (iterativa)\n")

    print(f"Elemento encontrado na posição {recursiva(array, elemento, 0, len(array) - 1)} (recursiva)\n")
    
    print(array)

main()
