import json
import os

RUTA = os.path.join(os.path.dirname(__file__), "data", "reportes", "reporte_libros.json")

def generar_reporte(libros):

    os.makedirs(os.path.dirname(RUTA), exist_ok=True)

    categorias = []
    lista_reporte = []

    for libro in libros:
        if libro["genero"] not in categorias:
            categorias.append(libro["genero"])

    print("\nREPORTE:\n")

    for genero in categorias:
        print(f"{genero}:")

        libros_genero = []

        for libro in libros:
            if libro["genero"] == genero:

                if libro["estado"] == "disponible":
                    estado = "Disponible"
                else:
                    estado = f'Prestado a {libro["prestado_a"]}'

                print(f"- {libro['titulo']} | {libro['autor']} | {estado}")

                libros_genero.append({
                    "titulo": libro["titulo"],
                    "autor": libro["autor"],
                    "estado": estado
                })

        lista_reporte.append({
            "categoria": genero,
            "libros": libros_genero
        })

    input("\nPresione ENTER para continuar...")

    with open(RUTA, "w") as archivo:
        json.dump(lista_reporte, archivo, indent=4)

    print("\nReporte guardado\n")