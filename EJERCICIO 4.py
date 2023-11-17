def calcular_media_números(lista):
    """Escribir una función que reciba una muestra de números en una lista y devuelva su media.
       lista: números introducidos por el ususario
    """
    suma_lista = sum(lista)
    cantidad = len(lista)
    return suma_lista/cantidad

print(calcular_media_números([2, 7, 6]))
