#  contadores para cada carrera
arquitectura = 0
medicina = 0
ingenieria = 0
economia = 0

# mostrar menú y obtener elección usuario
def mostrar_menu():
    print("\nSeleccione la carrera del estudiante que ingresa al ascensor:")
    print("1. Arquitectura")
    print("2. Medicina")
    print("3. Ingeniería")
    print("4. Economía")
    print("5. Salir")
    return input("Ingrese el número de la opción: ")

# Bucle
while True:
    opcion = mostrar_menu()
    
    if opcion == '1':
        arquitectura += 1
        print("Un estudiante de Arquitectura ha ingresado al ascensor.")
    elif opcion == '2':
        medicina += 1
        print("Un estudiante de Medicina ha ingresado al ascensor.")
    elif opcion == '3':
        ingenieria += 1
        print("Un estudiante de Ingeniería ha ingresado al ascensor.")
    elif opcion == '4':
        economia += 1
        print("Un estudiante de Economía ha ingresado al ascensor.")
    elif opcion == '5':
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

# Mostrar resultados
print("\nResultados finales:")
print(f"Arquitectura: {arquitectura} estudiantes")
print(f"Medicina: {medicina} estudiantes")
print(f"Ingeniería: {ingenieria} estudiantes")
print(f"Economía: {economia} estudiantes")

# Calcular el total de estudiantes
total = arquitectura + medicina + ingenieria + economia
print(f"\nTotal de estudiantes que usaron el ascensor: {total}")

# Encontrar carrera con más estudiantes
max_estudiantes = max(arquitectura, medicina, ingenieria, economia)
if max_estudiantes == arquitectura:
    print("La carrera que más usó el ascensor fue Arquitectura.")
elif max_estudiantes == medicina:
    print("La carrera que más usó el ascensor fue Medicina.")
elif max_estudiantes == ingenieria:
    print("La carrera que más usó el ascensor fue Ingeniería.")
elif max_estudiantes == economia:
    print("La carrera que más usó el ascensor fue Economía.")