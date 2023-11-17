def factorial(i):
      """Escribir una función que reciba un número entero positivo y devuelva su factorial.
    Realiza el ejercicio mediante bucles interactivos y mediante una función recursiva.
    Parámetros:
    i=número entero positivo
    """
      resultado = 1
      
      for j in range(1, i + 1):
          resultado *= j
        
      return resultado