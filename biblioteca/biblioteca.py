def add_book(libros):
    identificador = input("Identificador: ")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    precio = float(input("Precio: "))
    genero = input("Genero: ")
    prestamo = input("Prestado (Si/No): ")

    datos = (identificador, titulo, autor, precio, genero, prestamo)

    libro = {
        "identificador": datos[0],
        "titulo": datos[1],
        "autor": datos[2],
        "precio": datos[3],
        "genero": datos[4],
        "prestamo": datos[5]
    }

    libros.append(libro)
    print("Libro agregado correctamente")

def get_information(libros):
    if len(libros) == 0:
        print("No hay libros registrados")
        return

    mayor = libros[0]
    menor = libros[0]
    suma = 0

    for libro in libros:
        if libro["precio"] > mayor["precio"]:
            mayor = libro

        if libro["precio"] < menor["precio"]:
            menor = libro

        suma = suma + libro["precio"]

    promedio = suma / len(libros)

    print("Libro mas caro:", mayor["titulo"])
    print("Libro mas barato:", menor["titulo"])
    print("Precio promedio:", promedio)

def get_books_author(libros):
    autor = input("Ingrese el autor: ")
    encontrado = False

    for libro in libros:
        if libro["autor"] == autor:
            print("Titulo:", libro["titulo"])
            print("Precio:", libro["precio"])
            encontrado = True

    if encontrado == False:
        print("No se encontraron libros de ese autor")

def get_information_loan(libros):
    encontrado = False

    for libro in libros:
        if libro["prestamo"].lower() == "si":
            print("Titulo:", libro["titulo"])
            print("Autor:", libro["autor"])
            encontrado = True

    if encontrado == False:
        print("No hay libros en prestamo")

def get_top_3(libros):
    ordenados = libros[:]

    for i in range(len(ordenados)):
        for j in range(i + 1, len(ordenados)):
            if ordenados[j]["precio"] > ordenados[i]["precio"]:
                auxiliar = ordenados[i]
                ordenados[i] = ordenados[j]
                ordenados[j] = auxiliar

    cantidad = 3

    if len(ordenados) < 3:
        cantidad = len(ordenados)

    for i in range(cantidad):
        print("Titulo:", ordenados[i]["titulo"])
        print("Precio:", ordenados[i]["precio"])
