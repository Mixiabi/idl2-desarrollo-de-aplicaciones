def clasificar_numero(numeros):
    # Estructura de datos anidad
    clasificacion = {
        'pares': {'conteo':0,'numeros':[]},
        'impares': {'conteo':0,'numeros':[]},
        'positivos': {'conteo':0,'numeros':[]},
        'neutros': {'conteo':0,'numeros':[]},
        'negativos': {'conteo':0,'numeros':[]}
    }
    for num in numeros:
        if num % 2 == 0:
            # Agrega o suma a conteo cualquier coincidencia
            clasificacion['pares']['conteo'] += 1
            # Agrega a la lista anidada todos los elementos que coincidan
            clasificacion['pares']['numeros'].append(num)
        else:
            clasificacion['impares']['conteo'] += 1
            clasificacion['impares']['numeros'].append(num)
        if num > 0:
            clasificacion['positivos']['conteo'] += 1
            clasificacion['positivos']['numeros'].append(num)
        elif num == 0:
            clasificacion['neutros']['conteo'] += 1
            clasificacion['neutros']['numeros'].append(num)
        else:
            clasificacion['negativos']['conteo'] += 1
            clasificacion['negativos']['numeros'].append(num)
    return clasificacion

if __name__ == '__main__':
    # Bucle principal para preguntar si desea continuar
    while True:  
        listaNumeros = []

        print('_' * 55)
        print("\tIngresa 10 números para clasificarlos\n\tPresiona 'ENTER' para ingresar")
        print('-' * 55)

        # Bucle para ingresar 10 elementos
        for i in range(10):
            while True:
                ingresoNumero = input().strip()
                if ingresoNumero == "":
                    print("\tEntrada vacía no permitida. Por favor,\n\tingresa un número válido.")
                    continue
                try:
                    numero = int(ingresoNumero)
                    listaNumeros.append(numero)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número entero.")

        # Clasificar y mostrar los resultados
        clasificacion = clasificar_numero(listaNumeros)
        print('_' * 55)
        print("\t\tClasificación de números:")
        print('-' * 55)

        # Bucle para imprimir cada item del diccionario
        for categoria, data in clasificacion.items():
            print(f"'{categoria}': {data['conteo']}\t ==>  {data['numeros']}")

        # Preguntar si desea continuar
        continuar = input("\n¿Deseas clasificar otro conjunto de números? (s/n): ").strip().casefold()
        if continuar != 's':
            print('_' * 55)
            print("\tGracias por usar el programa. ¡Hasta luego!")
            print('-' * 55)
            break