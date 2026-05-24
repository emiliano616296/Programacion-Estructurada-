print("\033c")  # Limpiar pantalla

num_tabla = int(input("¿Qué tabla quieres? "))
num = 1

while num <= 10:
    multi = num_tabla * num
    print(f"{num_tabla} x {num} = {multi}")
    num += 1