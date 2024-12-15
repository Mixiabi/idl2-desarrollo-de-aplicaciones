def registrar_invitado(edadPorSexo):
    while True:
        try:
            # INGRESO DE EDAD POR PERSONA
            edad = int(input(f"Ingrese la edad:\t"))
            if edad <= 0 or isinstance(edad,str):
                print('\033[1;31m-\033[0m' * 43)
                print('\033[1;31m\tIngrese una edad válida.\033[0m')
                print('\033[1;31m-\033[0m' * 43)
                continue

            # INGRESO DE SEXO POR PERSONA
            sexo = input(f"Ingrese el sexo:\t").casefold().strip()
            print()
            if sexo not in ['m', 'f']:
                print('\033[1;31m-\033[0m' * 43)
                print("\033[1;31mSexo no válido. Ingrese el sexo correcto\n'M' para masculino y 'F' para femenino\033[0m")
                print('\033[1;31m-\033[0m' * 43)
                continue

            # AGREGAR A LA LISTA
            edadPorSexo[sexo].append(edad)
            break

        except ValueError:
            print('\033[1;31m-\033[0m' * 43)
            print('\033[1;31mDato no válido, solo se permiten números.\033[0m')
            print('\033[1;31m-\033[0m' * 43)

def mostrar_resultados(edadPorSexo, invitados):
    # MACIMO Y MINIMO DE AMBOS SEXOS
    maxHombres = max(edadPorSexo['m'], default=0)
    maxMujeres = max(edadPorSexo['f'], default=0)
    minHombres = min(edadPorSexo['m'], default=0)
    minMujeres = min(edadPorSexo['f'], default=0)

    # PROMEDIO DE EDAD ENTRE HOMBRES Y MUJERES
    totalHombres = sum(edadPorSexo['m']) / len(edadPorSexo['m']) if len(edadPorSexo['m']) > 0 else 0
    totalMujeres = sum(edadPorSexo['f']) / len(edadPorSexo['f']) if len(edadPorSexo['f']) > 0 else 0
    # TITULO
    print('\n' + '=' * 43)
    print("== C O N T R O L  D E  I N V I T A D O S ==")
    print('=' * 43)
    # LISTA DE EDADES POR SEXO
    print(f"Hombres: {edadPorSexo['m']}")
    print(f"Mujeres: {edadPorSexo['f']}")
    # TOTAL DE INVITADOS
    print(f"Total de personas que asistieron: {invitados}")
    # CANTIDAD DE INVITADOS POR SEXO
    print(f"Hombres: {len(edadPorSexo['m'])}")
    print(f"Mujeres: {len(edadPorSexo['f'])}")
    # MAXIMO Y MINIMO POR SEXOo
    print(f"Max. edad en Hombres: {maxHombres}")
    print(f"Max. edad en Mujeres: {maxMujeres}")
    print(f"Min. edad en Hombres: {minHombres}")
    print(f"Min. edad en Mujeres: {minMujeres}")
    # PROMEDIO DE EDADES POR SEXO
    print(f"Promedio de edades de Hombres: {totalHombres}")
    print(f"Promedio de edades de Mujeres: {totalMujeres}")
    # AGRADECIMIENTO
    print('\033[1;32m-\033[0m' * 43)
    print("\033[1;32m** Gracias por usar nuestros servicios. **\033[0m")
    print('\033[1;32m-\033[0m' * 43)

def main():
    # DICCIONARIO
    edadPorSexo = {'m': [], 'f': []}
    # CONTADOR DE INVITADOS
    invitados = 0
    print('\n' + '=' * 43)
    print("=========== B I E N V E N I D O ===========")
    print('=' * 43)
    # INGRESAR NUMERO DE PERSONAS A REGISTRAR
    cantidad_invitados = int(input('Personas a registrar:\t '))
    print()
    # REGISTRAR PERSONAS
    for i in range(cantidad_invitados):
        registrar_invitado(edadPorSexo)
        invitados += 1

    # PREGUNTAR SI SE DESEA AGREGAR MAS PERSONAS
    while True:
        agregar_mas = input("¿Desea registrar más personas? (s/n): ").casefold().strip()
        if agregar_mas == 's':
            registrar_invitado(edadPorSexo)
            invitados += 1
        elif agregar_mas == 'n':
            break
        else:
            print('\033[1;31m-\033[0m' * 43)
            print("Respuesta no válida. Por favor ingrese 's' o 'n'.")
            print('\033[1;31m-\033[0m' * 43)

    # MOSTRAR RESULTADO FINAL
    mostrar_resultados(edadPorSexo, invitados)

if __name__ == '__main__':
    # LLAMA AL MAIN Y DE AHI LLAMA A LAS OTRAS
    main()
