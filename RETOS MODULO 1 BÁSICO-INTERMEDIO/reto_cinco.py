# ---- Código ----

calificaciones =[]
nombres_alumnos =[]
Reprobados=[]
Aprobados=[]
Excelentes=[]

num_alumnos = int(input("Ingrese el número de alumnos en la clase: "))
for i in range(num_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
    nombres_alumnos.append(nombre)
    calificaciones.append(calificacion)
if calificacion <= 0 and calificacion >= 10:
    print("Calificación inválida. Debe estar entre 0 y 10.")
elif calificacion < 6:
    print(f"{nombre} ha reprobado con una calificación de {calificacion}.")
    Reprobados.append(nombre)
elif calificacion >= 6 and calificacion < 10:
    print(f"{nombre} ha aprobado con una calificación de {calificacion}.")
    Aprobados.append(nombre)
else:
    print(f"{nombre} ha obtenido una calificación perfecta de {calificacion}!")
    Excelentes.append(nombre)
print("Aqui tienes un resumen de las calificaciones:")
print("-"*40)
print("tienes un total de", num_alumnos, "alumnos en la clase.")
print(f"Alumnos reprobados: {Reprobados}")
print(f"Alumnos aprobados: {Aprobados}")
print(f"Alumnos con calificación excelente: {Excelentes}")
print("Promedio del grupo:", sum(calificaciones)/num_alumnos)
print("la calificación más alta es:", max(calificaciones))
print("la calificación más baja es:", min(calificaciones))

# ---- fin del código ----