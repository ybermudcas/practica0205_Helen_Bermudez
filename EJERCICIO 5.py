def números(lista):
    """función que reciba una muestra de números en una lista y devuelva otra lista con sus valores al cuadrado.
        Parámetros:
    """
    for i in range(len(lista)):
        lista[i] = lista[i]**2
        
        return lista

print(números([2, 5, 6]))