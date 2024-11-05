import math
import time
import random

def iterativa(arr, elemento):
    inicio = 0
    fim = len(arr) - 1
    comparacoes = 0

    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2
        if arr[meio] == elemento:
            return comparacoes
        elif arr[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1

    return comparacoes

def por_salto(arr, elemento):
    n = len(arr)
    salto = int(math.sqrt(n))
    anterior = 0
    comparacoes = 0

    while arr[min(salto, n) - 1] < elemento:
        comparacoes += 1
        anterior = salto
        salto += int(math.sqrt(n))
        if anterior >= n:
            return comparacoes

    for i in range(anterior, min(salto, n)):
        comparacoes += 1
        if arr[i] == elemento:
            return comparacoes

    return comparacoes

def fibonaci(arr, elemento):
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2
    comparacoes = 0

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        comparacoes += 1
        i = min(offset + fib2, n - 1)
        if arr[i] < elemento:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > elemento:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return comparacoes

    if fib1 and arr[offset + 1] == elemento:
        comparacoes += 1
        return comparacoes

    return comparacoes


def main():
    array = list(range(10000)) 
    elementos_a_procurar = random.sample(range(10000), 100)  

    binaria = []
    salto = []
    fibonacci = []

    for elemento in elementos_a_procurar:
        binaria.append(iterativa(array, elemento))
        salto.append(por_salto(array, elemento))
        fibonacci.append(fibonaci(array, elemento))

    media_binaria = sum(binaria) / len(binaria)
    media_salto = sum(salto) / len(salto)
    media_fibonacci = sum(fibonacci) / len(fibonacci)

    print(f"Media binaria: {media_binaria}\nMedia salto: {media_salto}\nMedia fibonacci {media_fibonacci}")
    
main()
