# Reto 5
# 17/10/2025

num_alumnos = int(input("Ingresa la cantidad de alumnos a registrar: "))
lista_nombres = []
lista_calificacion = []

for alumnos in range(num_alumnos):
    nombre = input(f"\nIngresa el nombre del alumno no.{alumnos+1}: ")
    lista_nombres.append(nombre)
    calificacion = int(input(f"Ingresa la calificacion del alumno no.{alumnos+1}: "))
    lista_calificacion.append(calificacion)

aprobados = []
reprobados = []
excelentes = []
promedio_grupo = sum(lista_calificacion) / len(lista_calificacion)

for i in range(len(lista_nombres)):
    if lista_calificacion[i] <= 5:
        reprobados.append(lista_nombres[i])
    elif lista_calificacion[i] == 10:
        excelentes.append(lista_nombres[i])
    else:
        aprobados.append(lista_nombres[i])

print(f"\nLa cantidad de alumnos es: {num_alumnos}")
print(f"El promedio general del grupo es: {promedio_grupo}")
print(f"La calificacion mas alta es {max(lista_calificacion)} y la mas baja es {min(lista_calificacion)}")
print("\nReprobados: ", reprobados)
print("Aprobados: ", aprobados)
print("Excelentes: ", excelentes)