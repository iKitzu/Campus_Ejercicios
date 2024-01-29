# Secuencia fibonacci

print("¡Bienvenido al generador de la Secuencia de Fibonacci!")
print("La Secuencia de Fibonacci comienza con 0 y 1, y cada término subsiguiente es la suma de los dos términos anteriores.")
print("Ingrese un valor entero para generar la secuencia hasta ese término ")

x=0
y=1
z=0

while True:
    n=int(input("Porfavor ingresa un numero mayor a 1 (presione 0 para salir): "))
    if n==0:
        print("Hasta luego")
        break
    elif n<0:
        print("ERROR -> El numero deberia ser positivo")
    else:
        for i in range(0,n):
            z=x+y
            print(f"{z}",end=" ")
            x=y
            y=z
        break
print("")