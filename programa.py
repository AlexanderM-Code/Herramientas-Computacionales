def registrar_uso_ascensor(carrera, registro):
    # Si la carrera ya está en el diccionario, incrementar el contador
    if carrera in registro:
        registro[carrera] += 1
    # Si no, agregar la carrera al diccionario con un contador inicial de 1
    else:
        registro[carrera] = 1

def carrera_mas_uso(registro):
    # Encontrar la carrera con más usos
    carrera_mas_utilizada = max(registro, key=registro.get)
    return carrera_mas_utilizada, registro[carrera_mas_utilizada]

def main():
    registro_ascensor = {}
    
    while True:
        # Pedir al usuario que ingrese una carrera o salir
        carrera = input("Ingrese la carrera (o 'salir' para terminar): ")
        if carrera.lower() == 'salir':
            break
        
        # Registrar el uso del ascensor
        registrar_uso_ascensor(carrera, registro_ascensor)
    
    if registro_ascensor:
        carrera, usos = carrera_mas_uso(registro_ascensor)
        print(f"La carrera que más ha utilizado el ascensor es {carrera} con {usos} usos.")
    else:
        print("No se han registrado usos del ascensor.")

if __name__ == "__main__":
    main()
