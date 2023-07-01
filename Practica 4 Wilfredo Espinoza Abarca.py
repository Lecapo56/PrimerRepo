# Problema 1
# import requests

# n = float(input("Ingrese la cantidad de bitcoins que posee: "))

# try:
#     response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
#     data = response.json()
#     precio_usd = data["bpi"]["USD"]["rate_float"]
#     current_cost = n * precio_usd
#     print(f"El costo actual de {n} bitcoins es: ${current_cost:,.4f}")
# except requests.RequestException as e:
#     print("Error al realizar la solicitud:", e)

# Problema 2

# import random

# from pyfiglet import Figlet

# figlet = Figlet()
# available_fonts = figlet.getFonts()

# font_name = input("Ingrese el nombre de la fuente a utilizar (deje en blanco para seleccionar aleatoriamente): ")

# if font_name == "":
#     font_name = random.choice(available_fonts)

# if font_name not in available_fonts:
#     print("La fuente ingresada no es válida. Las fuentes disponibles son:")
#     print(available_fonts)
# else:
#     text_to_print = input("Ingrese el texto a imprimir: ")

#     figlet.setFont(font=font_name)

#     print(figlet.renderText(text_to_print))

# Problema 3

# import requests

# url = 'https://unsplash.com/es/fotos/Qb7D1xw28Co'

# response = requests.get(url)

# with open('Perros.png', 'wb') as f:
#     f.write(response.content)
#     pass

# Problema 4

# def guardar_tabla_multiplicar(numero):
#     try:
#         with open(f"tabla-{numero}.txt", "w") as file:
#             for i in range(1, 11):
#                 resultado = numero * i
#                 file.write(f"{numero} x {i} = {resultado}\n")
#         print(f"La tabla de multiplicar del número {numero} ha sido guardada en el archivo tabla-{numero}.txt")
#     except IOError:
#         print("Error al guardar la tabla de multiplicar.")

# def mostrar_tabla_completa(numero):
#     try:
#         with open(f"tabla-{numero}.txt", "r") as file:
#             tabla = file.read()
#         print(tabla)
#     except FileNotFoundError:
#         print(f"No se encontró el archivo tabla-{numero}.txt")

# def mostrar_linea_tabla(numero, linea):
#     try:
#         with open(f"tabla-{numero}.txt", "r") as file:
#             lineas = file.readlines()
#             if linea <= len(lineas):
#                 print(lineas[linea - 1])
#             else:
#                 print(f"No existe la línea {linea} en el archivo tabla-{numero}.txt")
#     except FileNotFoundError:
#         print(f"No se encontró el archivo tabla-{numero}.txt")

# # Menú principal
# while True:
#     print("\n--- Menú ---")
#     print("1. Guardar tabla de multiplicar")
#     print("2. Mostrar tabla completa")
#     print("3. Mostrar línea de la tabla")
#     print("4. Salir")
#     opcion = input("Seleccione una opción (1-4): ")

#     if opcion == "1":
#         numero = int(input("Ingrese un número entre 1 y 10: "))
#         if 1 <= numero <= 10:
#             guardar_tabla_multiplicar(numero)
#         else:
#             print("Número inválido. Debe ser entre 1 y 10.")
#     elif opcion == "2":
#         numero = int(input("Ingrese un número entre 1 y 10: "))
#         if 1 <= numero <= 10:
#             mostrar_tabla_completa(numero)
#         else:
#             print("Número inválido. Debe ser entre 1 y 10.")
#     elif opcion == "3":
#         numero = int(input("Ingrese un número entre 1 y 10: "))
#         linea = int(input("Ingrese el número de línea a mostrar: "))
#         if 1 <= numero <= 10 and linea >= 1:
#             mostrar_linea_tabla(numero, linea)
#         else:
#             print("Número o línea inválida.")
#     elif opcion == "4":
#         print("¡Hasta luego!")
#         break
#     else:
#         print("Opción inválida. Seleccione una opción válida del menú.")