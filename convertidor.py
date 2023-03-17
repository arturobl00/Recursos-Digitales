# solicitar al usuario un número decimal y asignarlo a una variable
numero_decimal = int(input("Ingrese un número decimal: "))


# convertir el número a binario y hexadecimal y asignar los resultados a variables
def decimal_a_binario(numero_decimal):
    # manejar el caso especial de 0
    if numero_decimal == 0:
        return '0'
    
    # inicializar una lista para almacenar los bits del número binario
    bits = []
    
    # calcular los bits del número binario
    while numero_decimal > 0:
        # calcular el siguiente bit del número binario
        bit = numero_decimal % 2
        
        # agregar el bit a la lista de bits
        bits.append(str(bit))
        
        # dividir el número decimal por 2
        numero_decimal //= 2
    
    # invertir la lista de bits y unirlos en una cadena de texto
    bits.reverse()
    numero_binario = ''.join(bits)
    
    # devolver el número binario como una cadena de texto
    return numero_binario

num = decimal_a_binario(numero_decimal)

print("Tu Número en binario es: ", num)