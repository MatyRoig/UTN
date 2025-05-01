from funciones import cargar_matriz, cargar_jugadores, mostrar_jugadores, modificar_informacion_jugadores
def menu_opciones():
    matriz = None
    filas=11
    columnas=5
    
    while True:
        print("\nMenu de opciones:")
        print("1 - Cargar jugadores")
        print("2 - Mostrar jugadores")
        print("3 - Modificar información de jugadores")
        print("4 - Salir")

        opcion = (input("Seleccione una opción:  [1-4]: "))

        if opcion == "1":
            print("\nCargando la informacion de los jugadores... ")
            matriz= cargar_matriz(filas, columnas)
            matriz= cargar_jugadores(matriz)

        elif opcion == "2":
            if matriz is None:
                print("\nPrimero debe cargar la información de los jugadores.")  
            else:
                print("\nMostrando la informacion de los jugadores... ")
                mostrar_jugadores(matriz)

        elif opcion == "3":
            if matriz is None:
                print("\nPrimero debe cargar la información de los jugadores.")  
            else:
                print("\nAqui se modificara la informacion de los jugadores... ")
                matriz= modificar_informacion_jugadores(matriz) 

        elif opcion == "4":
            print("\nGracias por usar el sistema...")
            break
        
        else:
            print("\nOpción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    menu_opciones()
            
                 

