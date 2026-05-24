# Definir las funciones
def funcion1():
    print("Esta es la función 1")

def funcion2():
    nombre = input("Nombre: ").strip().upper()
    apellidos = input("Apellidos: ").strip().upper()
    return nombre, apellidos

def funcion3(nombre, apellidos):
    print(f"El nombre del alumno es: {nombre} {apellidos}")

def funcion4(nombre, apellidos):
    return nombre, apellidos

# Invocar las funciones
funcion1()

nombre = input("Nombre: ").strip().upper()
apellidos = input("Apellidos: ").strip().upper()
funcion3(nombre, apellidos)

nombre, apellidos = funcion2()
print(f"El nombre del alumno es: {nombre} {apellidos}")

nombre = input("Nombre: ").strip().upper()
apellidos = input("Apellidos: ").strip().upper()
nom, ape = funcion4(nombre, apellidos)
print(f"El nombre del alumno es: {nom} {ape}")