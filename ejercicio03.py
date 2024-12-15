"""
Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; se quiere saber cuánto lleva ahorrado cada vez que haga un deposito en cada mes y luego mostrar el ahorro final de 12 meses.
"""
import calendar
import locale

# Cambia 'es_ES.UTF-8' según tu sistema para CALENDAR
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  

def deposito_ahorro_anual():

    print('\n'+'=' * 10 +"  B A N C O   D E   A H O R R O  "+'=' * 10 + '\n')

    # Inicializar el ahorro total en 0
    ahorro_total = 0

    # Recorrer los meses del año
    for mes in range(1, 13):

        # Obtener el nombre del mes
        nombre_mes = calendar.month_name[mes] 
        deposito = float(input(f"    {nombre_mes}:\t\t   S/\t"))


        # Validar que el depósito sea un número positivo
        if deposito < 0:
            print('_' * 55)
            print("El depósito no puede ser negativo. Inténtalo de nuevo.")
            print('-' * 55)
            deposito = float(input(f"\n\033[1;31mIngrese un monto válido para el mes de {nombre_mes}: \033[0m"))
            print('-' * 55)    

        # Sumar el depósito al ahorro total
        ahorro_total += deposito

        # # Mostrar el ahorro acumulado hasta el momento
        print(f"\n\033[1;34mAhorro acumulado hasta el mes de {nombre_mes}: {ahorro_total:.2f} soles\033[0m\n")

    return ahorro_total

def mostrar_resultado(ahorro_total):
    print (
        f"\033[1;32m{'_' * 55}\033[0m\n"
        f"\033[1;32mEl ahorro total al final del año es: {ahorro_total:.2f} soles\033[0m\n"
        f"\033[1;32m{'-' * 55}\033[0m\n\n"
        f"{'_' * 55}\n"
        f"\tGracias por usar nuestros servicios.\n"
        f"{'-' * 55}"
    )


if __name__ == '__main__':
    ahorro_total = deposito_ahorro_anual()
    mostrar_resultado(ahorro_total)