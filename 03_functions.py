#### Funciones ####

## Definir una función básica
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Manuel"))
print(saludar("Luis"))

## Parámetros por defecto
    # Lo usamos cuando queremos dar un valor por defecto al parámetro en caso que no se le de un valor cuando se llame a la función
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(5))
print(potencia(2, 10)) # <- Aquí si definimos el parámetro
print(potencia(exponente=3, base=3)) # Argumento nombrado (indicamos explícitamente el nombre)

## Múltiples return (devolver varios valores)
def estadisticas(numeros):
    total = sum(numeros) # <-Devuelve la suma de todos los elementos de una colección numérica
    promedio = total / len(numeros) # <- Devuelve la cantidad de elementos de un array (similar al .length en JavaScript)
    maximo = max(numeros) # <- Devuelve el valor más grande de una colección
    return total, promedio, maximo # <- Devuelve una tupla

notas = [8, 6, 9, 7, 10]
total, prom, mx = estadisticas(notas) # Desempaquetando (similar a desestrucrurar en JavaScript)
print(f"Total: {total}, Promedio: {prom}, Máx: {mx}")

## *args y **kwargs (cantidad variable de arugmentos)
    # *args -> tupla de valores
        # "*" empaqueta todos los argumentos que reciba la función en una tupla. No importa cuantos valores se pasen, todas quedan dentro de numeros
def sumar(*numeros): 
    print(numeros)
    return sum(numeros)

print(sumar(1, 2, 3))
print(sumar(10, 20, 30, 40)) # <- PAsa a (10, 20, 30, 40)

    # **kwargs -> diccionario
        # "**" empaqueta todos los argumentos nombrados en un diccionario. Cada clave=valor que se pase se convierte en una entrada del diccionario
def perfil(**datos):
    for clave, valor in datos.items(): # -> Devuelve todos los pares clave-valor de un diccionario
        print(f"{clave}: {valor}")

perfil(nombre="Ana", edad=28, ciudad="Bogotá")

## Lambda (funciones de una sola línea)
# Función normal
def doble(x): return x * 2

# Equivalente con lambda
doble2 = lambda x: x * 2

print(doble(5))
print(doble2(5))

# Útil para ordenar
personas = [("Ana", 28), ("Luis", 22), ("Mía", 35)]
    # -> sort() ordena una lista en su lugar, es decir, modifica la lista original
personas.sort(key=lambda p: p[1]) # -> ordena por edad
print(personas)
    # -> p representa cada tupla ("Ana", 28)
    # -> p[0] sería el nombre -> "Ana"
    # -> p[1] sería la edad -> 28
    # -> Al decir key=lambda p: p[1], le indicas a sort() que ordene comparando solo la edad de cada tupla.


## Scope (variables locales vs globales)
mensaje = "Soy global"

def mostrar():
    local = "soy local" # -> Solo existe dentro de la función
    print(mensaje)
    print(local)

mostrar()
print(mensaje)