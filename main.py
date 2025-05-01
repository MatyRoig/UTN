from funciones import cargar_matriz, cargar_jugadores, mostrar_jugadores, modificar_informacion_jugadores
def menu_opciones():
    while True:
        print("Menu de opciones:")
        print("1 - Cargar jugadores")
        print("2 - Mostrar jugadores")
        print("3 - Modificar información de jugadores")
        print("4 - Salir")

        opcion = int(input("Seleccione una opción:  [1-4]: "))

        if opcion == "1":
            print("Cargando la informacion de los jugadores... ")
            cargar_matriz()
            cargar_jugadores()

        elif opcion == "2":
            print("Mostrando la informacion de los jugadores... ")
            mostrar_jugadores()

        elif opcion == "3":
            print("Aqui se modificara la informacion de los jugadores... ")
            modificar_informacion_jugadores() 

        elif opcion == "4":
            print("Gracias por usar el sistema...")
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


menu_opciones()
            
                 

