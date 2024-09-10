def conting(array):
    if not array:
        return array
    
    val_min = min(array)
    val_max = max(array)

    range_element = val_max - val_min + 1
    cont = [0] * (range_element)

    for numb in array:
        cont[numb  - val_min] += 1
    
    index = 0
    for i in range(range_element):
        while cont[i] > 0:
            array[index] = i
            index += 1
            cont[i] -= 1
    return array

array = [4,5,2,8,6,4,1]
sorted_arr = conting(array)
print(f"Array ordenado é {sorted_arr}")
