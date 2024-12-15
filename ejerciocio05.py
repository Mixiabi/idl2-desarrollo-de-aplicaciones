cursos = [
    "Matemática",
    "Ciencia y Tecnología",
    "Química",
    "Física",
    "Arte",
    "Educación Física",
    "Inglés",
    "Cívica",
    "Historia y Geografía",
]

#* ***************************************************************
#* CALCULA RESULTADOS DE CADA NOTA,PROMEDIO,CANTIDAD Y PORCENTAJE
#* ***************************************************************

def registrar_alumnos_y_notas():
    alumnos = {}
    print('\n' + '\033[1;36m=' * 50)
    print(" I N G R E S O   G E N E R A L   D E   N O T A S:")
    print('\033[1;36m=\033[0m' * 50)
    while True:
        try:
            cantidad_alumnos = int(input("\nIngrese la cantidad de alumnos a registrar (5-20): ").strip())
            if 5 <= cantidad_alumnos <= 20:
                break
            else:
                print('\n' + '\033[1;31m-\033[0m' * 80)
                print('\033[1;31mError: La cantidad de alumnos debe estar entre 5 y 20.\033[0m')
                print('\033[1;31m-\033[0m' * 80)
        except ValueError:
            print('\n' + '\033[1;31m-\033[0m' * 80)
            print('\033[1;31mError: Debe ingresar un número entero.\033[0m')
            print('\033[1;31m-\033[0m' * 80)

    for _ in range(cantidad_alumnos):

        while True:
                nombre = input("\nIngrese el nombre del alumno: ").strip()
                if not nombre.isalpha():
                    print("Error: El nombre debe contener solo letras y no debe estar vacío. Intente nuevamente.")
                else:
                    break

        alumnos[nombre] = {}

        for curso in cursos:
            while True:
                try:
                    nota = float(input(f"Ingrese la nota del curso \033[1;32m{curso}\033[0m (0-20): ").strip())
                    if 0 <= nota <= 20:
                        # Asignar la nota al curso
                        alumnos[nombre][curso] = nota
                        break
                    else:
                        print('\033[1;31m-\033[0m' * 80)
                        print("\033[1;31mError: La nota debe estar en el rango de 0 a 20.\033[0m")
                        print('\033[1;31m-\033[0m' * 80)
                except ValueError:
                    print('\033[1;31m-\033[0m' * 80)
                    print("\033[1;31mError: La nota debe ser un número válido.\033[0m")
                    print('\033[1;31m-\033[0m' * 80)

    return alumnos


#* ***************************************************************
#* CALCULA RESULTADOS DE CADA NOTA,PROMEDIO,CANTIDAD Y PORCENTAJE
#* ***************************************************************

def calcular_resultados(alumnos):

    estadisticas_por_curso = {}

    mayor_nota_por_alumno = {}
    menor_nota_por_alumno = {}

    cantidad_alumnos_mayor_nota = 0
    cantidad_alumnos_menor_nota = 0

    promedio_notas_salon = 0

    cantidad_total_notas_pares = 0
    cantidad_total_notas_impares = 0

    cantidad_total_alumnos_aprobados = 0
    cantidad_total_alumnos_desaprobados = 0

    porcentaje_total_alumnos_aprobados = 0
    porcentaje_total_alumnos_desaprobados = 0

    for alumno, cursos in alumnos.items():
        #! Usamos diccionario con sus items para obtener tuplas de clave:valor y accedemos al primer valor de cada clave con lambda[1]
        mayor_nota_por_alumno[alumno] = max(cursos.items(),key=lambda x: x[1])
        menor_nota_por_alumno[alumno] = min(cursos.items(), key=lambda x: x[1])

        for curso, nota in cursos.items():  #!
            if nota == 20:
                cantidad_alumnos_mayor_nota += 1
            elif nota <= 13:
                cantidad_alumnos_menor_nota += 1
        
            promedio_notas_salon += nota    #! acumula todas las notas ingresadas y las suma

            if nota % 2 == 0:
                cantidad_total_notas_pares += 1
            else:
                cantidad_total_notas_impares += 1

            if curso not in estadisticas_por_curso: #! REGISTRAR LAS ESTADISTICAS
                estadisticas_por_curso[curso] = {'total': 0, 'notas': [], 'aprobados': 0, 'desaprobados': 0}
                estadisticas_por_curso[curso]['total'] += 1
                estadisticas_por_curso[curso]['notas'].append(nota)

            if nota >= 13 :
                cantidad_total_alumnos_desaprobados += 1
                estadisticas_por_curso[curso]['aprobados'] += 1
            else:
                cantidad_total_alumnos_aprobados += 1
                estadisticas_por_curso[curso]['desaprobados'] += 1

    total_notas = sum(len(cursos) for cursos in alumnos.values())    #! calcula el total de notas ingresadas
    promedio_notas_salon = promedio_notas_salon / total_notas if total_notas > 0 else 0
        
    total_alumnos = cantidad_total_alumnos_aprobados + cantidad_total_alumnos_desaprobados
    
    porcentaje_total_alumnos_aprobados = (cantidad_total_alumnos_aprobados/total_alumnos)*100
    porcentaje_total_alumnos_desaprobados = (cantidad_total_alumnos_desaprobados/total_alumnos)*100

    return {
        "estadisticas_por_curso": estadisticas_por_curso,
        "mayor_nota_por_alumno": mayor_nota_por_alumno,
        "menor_nota_por_alumno": menor_nota_por_alumno,
        "cantidad_alumnos_mayor_nota": cantidad_alumnos_mayor_nota,
        "cantidad_alumnos_menor_nota": cantidad_alumnos_menor_nota,
        "promedio_notas_salon": promedio_notas_salon,
        "cantidad_total_notas_pares": cantidad_total_notas_pares,
        "cantidad_total_notas_impares": cantidad_total_notas_impares,
        "cantidad_total_alumnos_aprobados": cantidad_total_alumnos_aprobados,
        "cantidad_total_alumnos_desaprobados": cantidad_total_alumnos_desaprobados,
        "porcentaje_total_alumnos_aprobados": porcentaje_total_alumnos_aprobados,
        "porcentaje_total_alumnos_desaprobados": porcentaje_total_alumnos_desaprobados,
    }


#* *****************************************************
#*   IMPRIME RESULTADOS EXTRAIDOS DE LA FUNCION MAIN()
#* *****************************************************

def imprimir_resultados(resultados):
    print('\n' + '\033[1;36m=' * 50)
    print("R E S U M E N   G E N E R A L   D E   N O T A S:\033[0m")
    print('\033[1;36m=\033[0m' * 50)
    print(f"Mayor nota por alumno: {resultados['mayor_nota_por_alumno']}")
    print(f"Menor nota por alumno: {resultados['menor_nota_por_alumno']}")
    print(f"Cantidad de notas máximas (20): {resultados['cantidad_alumnos_mayor_nota']}")
    print(f"Cantidad de notas menores a 13: {resultados['cantidad_alumnos_menor_nota']}")
    print(f"Promedio de notas del salón: {resultados['promedio_notas_salon']:.2f}")
    print(f"Cantidad de notas pares: {resultados['cantidad_total_notas_pares']}")
    print(f"Cantidad de notas impares: {resultados['cantidad_total_notas_impares']}")
    print(f"Cantidad de alumnos aprobados: {resultados['cantidad_total_alumnos_aprobados']}")
    print(f"Cantidad de alumnos desaprobados: {resultados['cantidad_total_alumnos_desaprobados']}")
    print(f"Porcentaje de alumnos aprobados: {resultados['porcentaje_total_alumnos_aprobados']:.2f}%")
    print(f"Porcentaje de alumnos desaprobados: {resultados['porcentaje_total_alumnos_desaprobados']:.2f}%")


#* *****************************************************
#* BUSCARA EN LA LISTA ALUMNOS POR EL NOMBRE INGRESADO
#* *****************************************************

def buscar_alumno(alumnos):

    while True:
        nombre = input("\n\033[33mIngrese el nombre del alumno que desea consultar (o 'salir' para terminar):\033[0m ").strip()
        if nombre.lower() == "salir":
            break
        elif nombre in alumnos:
            print(f"\n\033[32;43mDatos del alumno {nombre}:\033[0m")
            for curso, nota in alumnos[nombre].items():
                print(f"  {curso}: {nota}")
        else:
            print("\033[1;31mError: El nombre ingresado no está registrado. Intente nuevamente.\033[0m")


#* ***************************************************************
#*     EJECUTA EL RESGITRO DE ALUMNOS,RESULTADOS E IMPRIME
#* ***************************************************************

def main():

    alumnos = registrar_alumnos_y_notas()
    resultados = calcular_resultados(alumnos)
    imprimir_resultados(resultados)
    
    while True:
        opcion = input("\n\033[32m¿Desea buscar datos de un alumno en particular? (s/n):\033[0m ").strip().casefold()
        if opcion == "s":
            buscar_alumno(alumnos)
        elif opcion == "n":
            print('\033[1;36m-' * 50)
            print("¡Gracias por usar el sistema de estadísticas!")
            print('-' * 50)
            break
        else:
            print('\033[1;31m-' * 50)
            print("Error: Respuesta no válida. Ingrese 's' o 'n'.")
            print('-' * 50)


#* ***************************************************************
#* EJECUTA TODO EN EL MISMO ARCHIVO
#* ***************************************************************

if __name__ == "__main__":
    main()
