#### Estructuras de control ####

## Condicionales
edad = 20

if edad < 18:
    print('Menor de edad')
elif edad > 18:
    print('Mayor de edad')
else:
    print('Recién nacido')

## Recorrer un array (ciclo for)
frutas = ["Manzana", "Pera", "Uva"]

for fruta in frutas:
    print(fruta)

    # Recorrer un rango de números
for i in range(1, 6): # <- Iteramos del 1 al 5 (el 6 es exclusivo)
    print(i)

## Ciclo While
contador = 0
while contador < 5:
    print(f"Vuelta {contador}")
    contador += 1

print("fin del bucle")

## Break/continue (control dentro de bucles)
for n in range(10):
    if n == 4:
        break # <- Le estamos diciendo que cuando n=4 detenga el bucle
    print(n)

print("-------------------------")

    # continue: saltar esta iteración y seguir
for n in range(6):
    if n % 2 == 0:
        continue
    print(n)

## for + enumarate/zip (patrones comunes)
nombres = ["Manuel", "Ana", "Mía"]
notas = [9.5, 7.0, 8.2]

    # enumarate: índice + valor
        # Recorre una lista y da dos cosas a la vez: índice y valor
for i, nombre in enumerate(nombres):
    print(f"{i}: {nombre}")

    #zip: recorrer dos listas a la vez
        # Recorrer dos listas en paralelo
for nombre, nota in zip(nombres, notas):
    print(f"{nombre} -> {nota}")