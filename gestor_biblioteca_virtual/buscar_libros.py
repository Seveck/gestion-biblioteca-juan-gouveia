import gestion_libros
import os

libro = gestion_libros.cargar_libros()
RUTA = os.path.join(os.path.dirname(__file__), "data", "libros.json")

def buscar_libro(libros):
    categoria = input("Escoga la categoria por la que buscara el libro (Titulo/Autor/Genero): ").lower()
    buscar = input("Escriba lo que quiere buscar: ").lower()

    encontrados = []

    if categoria not in ["titulo", "autor", "genero"]:
        print("Error, categoria invalida")
        return

    for libro in libros:
        if buscar in libro[categoria]:
            encontrados.append(libro)

    if encontrados:
        print("\nLibros encontrados:\n")
        for libro in encontrados:
            if libro["estado"] == "disponible":
                estado = "Disponible"
            else:
                estado = f'Prestado a {libro["prestado_a"]}'

            print(f"- {libro['titulo']} | Autor: {libro['autor']} | Estado: {estado}")
    else:
        print("\nNo se encontraron libros")