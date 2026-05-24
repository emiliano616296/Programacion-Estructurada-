

print("\033c")

num_tabla = int(input("Numero de la tabla de multiplicar: "))

for num in range(1, 11):
    multi = num_tabla * num
    print(f"{num_tabla} x {num} = {multi}")