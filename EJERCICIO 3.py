def área_círculo(radio):
    import math
    """Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
    Parámetros:
    área_circulo: voy a solicitar el radio
    agrego función math.pi para que represente el número que vale pi
    volúmen_cilindro: utilizo el radio del circulo y solicito la altura nada mas
    """
    return math.pi * radio**2

def volúmen_cilindro(radio, altura):
    return área_círculo(radio) * altura

print(volúmen_cilindro(10,10))