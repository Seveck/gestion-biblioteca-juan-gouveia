import json
import os

RUTA = os.path.join(os.path.dirname(__file__), "data", "libros.json")

def cargar_libros():
    try:
        with open(RUTA, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_libro(libros):
    with open(RUTA, "w") as archivo:
        json.dump(libros, archivo, indent=4)

def registrar_libro(libros):

    titulo = input("Escriba el titulo del libro: ").lower()
    
    for libro in libros:
        if libro["titulo"] == titulo:
            print(f"Error, el libro {titulo} ya ha sido agregado")
            return
        
    autor = input("Escriba el nombre del autor: ").lower()
    genero = input("Escriba el genero del libro: ").lower()
    
    while True:
        try:
            anio_publicacion = int(input("Digite el año en el que se publico el libro: "))
            break
        except ValueError:
            print("Error, valor invalido, vuelva a digitarlo")

    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "anio_publicacion": anio_publicacion,
        "estado": "disponible",
        "prestado_a": None
    }

    libros.append(nuevo_libro)
    guardar_libro(libros)

    print(f"\nEl libro {titulo} ha sido agregado correctamente\n")

def ver_inventario(libros):
    print("=" * 75)
    print(f"| {'Título':20} | {'Autor':20} | {'Género':15} | {'Estado':15} |")
    print("=" * 75)

    for libro in libros:
        if libro["estado"] == "disponible":
            estado = "Disponible"
        else:
            estado = f'Prestado a {libro["prestado_a"]}'

        print(f"| {libro['titulo']:20} | {libro['autor']:20} | {libro['genero']:15} | {estado:15} |")

    print("=" * 75)