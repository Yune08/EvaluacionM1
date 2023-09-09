#Realiza un programa en python que calcule el promedio de los estudiantes utilizando el siguiente diccionario:
 #   'Juan': 3.2, 4.5, 5
 #  'Maria': 4.2, 3.5, 4.3
 #   'Pedro': 3.9, 2.5, 4.8

def prom (notas):
    return sum(notas) / len(notas)

estudiantes = {
    'Juan': [3.2, 4.5, 5],
    'Maria': [4.2, 3.5, 4.3],
    'Pedro': [3.9, 2.5, 4.8]
}

def menu():
    print("Estudiantes")
    print("Seleccione un estudiante: (1-3)")
    print("1. Juan")
    print("2. Maria")
    print("3. Pedro")
    
    opcion = int(input("Ingrese el número segun tu nombre: "))

    if opcion == 1:
        promedio = prom (estudiantes['Juan'])
        print(f"Hola Juan tu promedio es: {promedio}")
    elif opcion == 2:
        promedio = prom (estudiantes['Maria'])
        print(f"Hola Maria tu promedio es: {promedio}")
    elif opcion == 3:
        promedio = prom (estudiantes['Pedro'])
        print(f"Hola Pedro tu promedio es: {promedio}")
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú (1-3).")

menu()
