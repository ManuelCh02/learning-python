##### Variables #####

## -> Las variables se declaran indicando el nombre de la misma, puden contener cualquier tipo de dato.
# -> En python no se necesita declarar el tipo de dato
edad = 25
año = 2026
temperatura = -3
precio = 3.99
promedio = 7 / 2 
nombre = 'Manuel'
activo = True

print(edad) # <- Imprimir en colosa
print(type(año)) # <- Imprimir el tipo de dato

## Convertir los tipos de datos (casting)
texto = "42"
numero = int(texto) # string -> integer
decimal = float(texto) # string -> float
string = str(numero) # integer -> string
boolean = bool(texto)
print(numero, string)
print(type(numero), type(string))

# Python es tipado dinámico - el tipo depende del valor actual
x = 10          # x es int
print(type(x))  # <class 'int'>
x = "diez"      # ahora x es str — Python lo permite
print(type(x))  # <class 'str'>

# Las f-strings son la forma moderna de concatenar
print(f"Hola {nombre}")