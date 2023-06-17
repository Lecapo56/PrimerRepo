import random

def generar_numeros_aleatorios():
    numeros = []
    for _ in range(20):
        numero = random.randint(0, 100)
        numeros.append(numero)
    return numeros

def mostrar_lista(numeros):
    for numero in numeros:
        print(numero)

def ordenar_lista(numeros):
    numeros.sort()