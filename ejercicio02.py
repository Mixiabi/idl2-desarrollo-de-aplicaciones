a = int(input("Ingresa un número entero positivo: "))

#*  Validar que el número sea positivo
if a < 0:
    print("Por favor, ingresa un número entero positivo.")
else:

    #* Invertir el número convirtiéndolo en cadena
    numero_invertido = int(str(a)[::-1])
    
    #* Imprimir el número invertido
    print(f"El número invertido es: {numero_invertido}")
