filas = 11
columnas = 5
def cargar_matriz(filas, columnas):
    return [[None for _ in range(columnas)] for _ in range(filas)]

def cargar_jugadores(matriz):
    for i in range(len(matriz)):
        matriz[i][0] = input("Ingrese el nombre del jugador: ")
        matriz[i][1] = int(input("Ingrese el documento del jugador: "))
        matriz[i][2] = int(input("Ingrese la edad del jugador: "))
        matriz[i][3] = int(input("Ingrese la cantidad de goles realizados: "))
        matriz[i][4] = int(input("Ingrese la posicion en la que juega el jugador: "))
    return matriz

def mostrar_jugadores(matriz):
    for i in range(len(matriz)):
        print(f"Nombre: {matriz[i][0]}, Documento: {matriz[i][1]}, Edad: {matriz[i][2]}, Goles: {matriz[i][3]}, Posición: {matriz[i][4]}")

def modificar_informacion_jugadores(matriz):
    documento = int(input("Ingrese el documento del jugador a modificar: "))
    
    fila=-1
    for i in range(len(matriz)):
        if matriz[i][1] == documento:
            fila = i
            break
    if fila == -1:
        print("Jugador no encontrado.")
        return None
    
    print("Usted puede realizar las siguientes modificaciones:")
    print("1 - Modificar nombre")
    print("2 - Modificar documento")
    print("3 - Modificar edad")
    print("4 - Modificar cantidad de goles")
    print("5 - Modificar posición")

    columna=int(input("Seleccione la opción que desea modificar:   [1-5] "))
    if columna < 0 or columna >= len(matriz[0]):
        print("Opción no válida.")
    else:
        if columna in (1, 2, 3):
            nuevo_valor = int(input(f"Ingrese el nuevo valor para {["nombre," "documento," "edad," "goles," "posicion"] [columna]}: "))
        else:
            nuevo_valor = int(input(f"Ingrese el nuevo valor para {["nombre," "documento," "edad," "goles," "posicion"] [columna]}: "))

        matriz[fila][columna] = nuevo_valor
        print("Información del jugador modificada correctamente!")
    
    return matriz

        