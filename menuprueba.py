from bd import agregar_pelicula, obtener_peliculas, eliminar_pelicula, modificar_pelicula

def mostrar_menu():
    print("\n📌 MENU DE PELICULAS")
    print("1. Agregar película")
    print("2. Mostrar todas las películas")
    print("3. Modificar película")
    print("4. Eliminar película")
    print("5. Salir")

def pedir_datos_pelicula():
    titulo = input("Ingrese el título: ")
    año = int(input("Ingrese el año: "))
    genero = input("Ingrese el género: ")
    return titulo, año, genero

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                print("\n🎬 AGREGAR PELICULA")
                titulo, año, genero = pedir_datos_pelicula()
                agregar_pelicula(titulo, año, genero)
                print("✔ Película agregada con éxito.")

            case "2":
                print("\n📋 LISTA DE PELICULAS")
                peliculas = obtener_peliculas()
                for peli in peliculas:
                    print(f"🎞 {peli['titulo']} ({peli['año']}) - {peli['genero']}")

            case "3":
                print("\n✏ MODIFICAR PELICULA")
                titulo_actual = input("Ingrese el título de la película a modificar: ")
                print("👉 INGRESE NUEVOS DATOS:")
                titulo, año, genero = pedir_datos_pelicula()
                modificar_pelicula(titulo_actual, titulo, año, genero)
                print("✔ Película modificada con éxito.")

            case "4":
                print("\n🗑 ELIMINAR PELICULA")
                titulo = input("Ingrese el título de la película a eliminar: ")
                eliminar_pelicula(titulo)
                print("✔ Película eliminada con éxito.")

            case "5":
                print("\n👋 Saliendo del sistema. ¡Hasta la próxima!")
                break

            case _:
                print("❌ Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
