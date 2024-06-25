import csv
import json
import re

# Función para escribir en un archivo de texto
def escribir_texto(nombre_archivo, texto):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(texto)

# Función para leer de un archivo de texto
def leer_texto(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()

# Función para escribir en un archivo CSV
def escribir_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        for fila in datos:
            escritor_csv.writerow(fila)

# Función para leer de un archivo CSV
def leer_csv(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        return [[int(celda) if celda.isdigit() else celda for celda in fila] for fila in lector_csv]

# Función para escribir en un archivo JSON
def escribir_json(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

# Función para leer de un archivo JSON
def leer_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return json.load(archivo)

# Función para validar un correo electrónico usando expresiones regulares
def validar_correo(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None

# Ejecución automática
if __name__ == "__main__":
    # Trabajo con archivo de texto
    archivo_texto = 'archivo.txt'
    texto = "Hola, este es un archivo de texto."
    escribir_texto(archivo_texto, texto)
    contenido_texto = leer_texto(archivo_texto)
    print(f"Contenido del archivo de texto: {contenido_texto}")
    assert contenido_texto == texto

    # Trabajo con archivo CSV
    archivo_csv = 'archivo.csv'
    datos_csv = [['Nombre', 'Edad'], ['Juan', 30], ['Ana', 25]]
    escribir_csv(archivo_csv, datos_csv)
    contenido_csv = leer_csv(archivo_csv)
    print(f"Contenido del archivo CSV: {contenido_csv}")
    assert contenido_csv == datos_csv

    # Trabajo con archivo JSON
    archivo_json = 'archivo.json'
    datos_json = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
    escribir_json(archivo_json, datos_json)
    contenido_json = leer_json(archivo_json)
    print(f"Contenido del archivo JSON: {contenido_json}")
    assert contenido_json == datos_json

    # Validación de correo electrónico
    correo = "correo@example.com"
    es_valido = validar_correo(correo)
    print(f"{correo} es un correo válido: {es_valido}")
    assert es_valido

    print("Todas las acciones se realizaron correctamente.")
