import gestion_libros
import os

RUTA = os.path.join(os.path.dirname(__file__), "data", "libros.json")

def prestar_libro(libros):
    titulo_prestar = input("Escriba el libro que desea pedir prestado: ").lower()
    nombre = input("Escriba su nombre: ").lower()

    for libro in libros:
        if libro["titulo"] == titulo_prestar:
            if libro["estado"] == "disponible":
                libro["estado"] = "prestado"
                libro["prestado_a"] = nombre

                gestion_libros.guardar_libro(libros)

                print(f"\nEl libro '{titulo_prestar}' fue prestado a {nombre}\n")
                return
            else:
                print("\nEl libro ya está prestado\n")
                return

    print("\nEl libro no existe en la biblioteca\n")

def devolver_libro(libros):
    libro_devolver = input("Escriba el libro que quiere devolver: ").lower()
    
    for libro in libros:
        if libro["titulo"] == libro_devolver:
            if libro["estado"] == "prestado":
                nombreAsegurar = input("Escriba su nombre: ").lower()
                if libro["prestado_a"] == nombreAsegurar:
                    print(f"\nMuchas gracias por devolver el libro {libro_devolver}, {nombreAsegurar}\n")
                    libro["estado"] = "disponible"
                    libro["prestado_a"] = None

                    gestion_libros.guardar_libro(libros)
                    return
                else:
                    print(f"\nError, el libro '{libro_devolver}' no fue prestado a {nombreAsegurar}\n")
                    return
            else:
                print(f"\nError, el libro '{libro_devolver}' no se encuentra prestado\n")
                return
        else:
            print(f"\nError, el libro '{libro_devolver}' no se encuentra disponible\n")
            return
