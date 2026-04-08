import gestion_libros 
import buscar_libros
import prestamos
import reportes

libros = gestion_libros.cargar_libros()

while True:

    print(
        "==========================================\n"
        "GESTOR DE INVENTARIO PARA UNA BIBLIOTECA VIRTUAL\n"
        "==========================================\n"
        "1. Registrar un nuevo libro\n"
        "2. Ver el inventario de libros\n"
        "3. Buscar un libro\n"
        "4. Prestar un libro\n"
        "5. Devolver un libro\n"
        "6. Generar un reporte del inventario\n"
        "7. Salir\n"
        "==========================================\n"
    )

    opcion = int(input("Seleccione una opcion: "))

    match opcion:
        case 1:
            gestion_libros.registrar_libro(libros)
        case 2:
            gestion_libros.ver_inventario(libros)
        case 3:
            buscar_libros.buscar_libro(libros)
        case 4:
            prestamos.prestar_libro(libros)
        case 5:
            prestamos.devolver_libro(libros)
        case 6:
            reportes.generar_reporte(libros)
        case 7:
                break  
        case _:
            print("Error, opcion invalida\n")