# Ejercicio 1
def porcentaje_combustible():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            numerador, denominador = (int, fraccion.split('/'))

            if denominador == 0:
                print("Error: El denominador (Y) no puede ser cero.")
                continue
            if numerador < denominador or numerador <= 0 or denominador <= 0:
                print("Error: X y Y deben ser números enteros positivos y X debe ser mayor o igual a Y.")
                continue

            porcentaje = numerador / denominador * 100

            if porcentaje < 1:
                print("E")
            elif porcentaje > 99:
                print("F")
            else:
                print(f"{round(porcentaje)}%")

            break

        except ValueError:
            print("Error: La fracción debe estar en formato X/Y con X e Y números enteros.")
        except ZeroDivisionError:
            print("Error: El denominador (Y) no puede ser cero.")

porcentaje_combustible()

# Ejercicio 2

def obtener_calificaciones():
    while True:
        try:
            calificaciones = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones_lista = calificaciones.split(',')
            calificaciones_enteros = [int(calificacion) for calificacion in calificaciones_lista]
            break

        except ValueError:
            print("Error: Las calificaciones deben ser números enteros y deben estar separadas por comas.")

    return calificaciones_enteros

calificaciones = obtener_calificaciones()
print("Calificaciones ingresadas:", calificaciones)

# Ejercicio 3

def triangulo_pascal(n):
    triangulo = [[1]]

    for i in range(1, n):
        fila_anterior = triangulo[i - 1]
        nueva_fila = [1]

        for j in range(1, i):
            nuevo_elemento = fila_anterior[j - 1] + fila_anterior[j]
            nueva_fila.append(nuevo_elemento)

        nueva_fila.append(1)
        triangulo.append(nueva_fila)

    for fila in triangulo:
        print(' '.join(str(num) for num in fila))

n = 7
triangulo_pascal(n)

# Ejercicio 4

def longitud_ultima_palabra(string):
    string = string.strip()

    palabras = string.split()

    if len(palabras) == 0:
        return 0

    return len(palabras[-1])
cadena = "Bienvenidos al curso de python"
longitud = longitud_ultima_palabra(cadena)
print(longitud)

# Ejercicio 5

import numeros_aleatorios

lista_numeros = numeros_aleatorios.generar_numeros_aleatorios()

numeros_aleatorios.mostrar_lista(lista_numeros)

numeros_aleatorios.ordenar_lista(lista_numeros)

numeros_aleatorios.mostrar_lista(lista_numeros)