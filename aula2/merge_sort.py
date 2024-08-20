def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]
    
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = 0
    j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
    while j < len(direita):
        resultado.append(direita[j])
        j += 1
    
    return resultado

lista = [48,32,67,36,25,80,43,39,98,10]
print("Lista original:", lista)

print("Lista ordenada:", merge_sort(lista))
