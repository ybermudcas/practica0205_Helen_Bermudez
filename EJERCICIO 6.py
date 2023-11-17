def decimal_binario(decimal):
    """Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
    Parámetros: 
    decimal= el número que queremos introducir para pasarlo
    bin = La función bin convierte un número entero en su representación binaria con formato de texto. El resultado estará precedido por los caracteres "0b"
    
    """
    return bin(decimal)

def binario_decimal(binario):
    decimal = int(binario, 2)
    return decimal

binario_decimal(11001)
print(binario_decimal)