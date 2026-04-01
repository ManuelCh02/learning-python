# Calcular cuota moderadora

SALARIO_MINIMO = 2000000
ingresoAfiliado = int(input('Ingrese el salario del afiliado: '))

diferenciaIngresoMinimo = ingresoAfiliado / SALARIO_MINIMO

if diferenciaIngresoMinimo < 2:
    print('Cuota moderadora: 4000')
else:
    if diferenciaIngresoMinimo >= 2 and diferenciaIngresoMinimo <= 5:
        print('Cuota moderadora: 15000')
    else:
        if diferenciaIngresoMinimo > 5:
            print('Cuota moderadora: 40000')
        else:
            print('Valor incorrecto')