## Promedio notas 1 estudiante

average = 0
nota1 = float(input('Introduzca la primera nota'))
nota2 = float(input('Introduzca la primera nota'))
nota3 = float(input('Introduzca la primera nota'))
nota4 = float(input('Introduzca la primera nota'))
nota5 = float(input('Introduzca la primera nota'))

average = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if average >= 3:
    print(f'Su promedio es de {average}. ¡Curso aprobado!')
else:
    print(f'Su promedio es de {average}. Curso Reprobado')