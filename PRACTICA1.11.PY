#Programa para calcular la potencia de un numero
#Requisitos crear una funcion que reciba parametros y regresa valor sin pow

print("\033c")

def potencia(num,expo):
    potencia=num**expo
    return potencia

num=int(input("Numero: "))
expo=int(input("Exponente: "))

resul=potencia(num,expo)

print(f"La potencia es: {resul}")