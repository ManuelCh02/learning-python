## Promedio notas 1 estudiante
import array ## Python no incluye array

average = 0
notes = array.array('d', [])

for i in range(1, 6):
    note = float(input(f'Ingrese la {i} nota: '))
    notes.append(note)

average = sum(notes) / len(notes)

if average >= 3:
    print(f'Su promedio es de {average}. ¡Curso aprobado!')
else:
    print(f'Su promedio es de {average}. Curso Reprobado')