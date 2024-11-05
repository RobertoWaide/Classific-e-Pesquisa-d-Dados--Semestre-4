import math

def por_salto(arr, elemento):
    n = len(arr)
    salto = int(math.sqrt(n)) 
    anterior = 0

    while arr[min(salto, n) - 1] < elemento:
        anterior = salto
        salto += int(math.sqrt(n))
        if anterior >= n:
            return -1  

    for i in range(anterior, min(salto, n)):
        if arr[i] == elemento:
            return i  

    return -1  

def fibonacci(arr, elemento):
    n = len(arr)
    fib2 = 0   
    fib1 = 1 
    fib = fib1 + fib2 

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
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
            return i  

    if fib1 and arr[offset + 1] == elemento:
        return offset + 1

    return -1  

def main():
    array = [1, 3, 5, 7, 9, 11, 13, 15]
    elemento = int(input("- "))

    print(f"\nElemento encontrado na posição {por_salto(array, elemento)} (salto)\n")

    print(f"Elemento encontrado na posição {fibonacci(array, elemento)} (Fibonacci)\n")

    print(array)
    
main()
