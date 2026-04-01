# Encontrar grupo generacional

edad = int(input('Ingrese su edad: '))

if edad <= 12 and edad > 0:
    print('Grupo generacional: Niño')
elif edad >= 13 and edad <= 17:
    print('Grupo generacional: Adolescente')
elif edad >= 18 and edad <= 34:
    print('Grupo generacional: Joven')
elif edad >= 35 and edad <= 63:
    print('Grupo generacional: Adulto')
elif edad > 63:
    print('Adulto Mayor')
else:
    print('Valor ingresado incorrecto')