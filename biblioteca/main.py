from biblioteca import *

libros = []
opcion = 0

while opcion != 6:
    print("\n===== BIBLIOTECA =====")
    print("1. Agregar libro")
    print("2. Informacion general")
    print("3. Buscar libros por autor")
    print("4. Mostrar libros prestados")
    print("5. Mostrar los 3 mas costosos")
    print("6. Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        add_book(libros)

    elif opcion == 2:
        get_information(libros)

    elif opcion == 3:
        get_books_author(libros)

    elif opcion == 4:
        get_information_loan(libros)

    elif opcion == 5:
        get_top_3(libros)

    elif opcion == 6:
        print("Hasta luego")

    else:
        print("Opcion incorrecta")
