def factorial(i):
    """Escribir una función que reciba un número entero positivo y devuelva su factorial.
    Realiza el ejercicio mediante bucles interactivos y mediante una función recursiva.
    Parámetros:
    i=número entero positivo
    """
    if i == 0:
        return 1
    else: 
        return i * factorial(i-1)
    
factorial(9)
print(factorial(9))

