# Reto 7
# 21/10/2025

diccionario_principal = {}
tupla_materias = ("resistencia de los materiales", "electronica analogica", "programacion avanzada", "procesos de manufactura")

estado_menu = True
while estado_menu:
    print("\nMenú de opciones")
    print("1. Registrar")
    print("2. Buscar")
    print("3. Promedio")
    print("4. Ver todos")
    print("5. Salir")
    respuesta_usuario = input("¿Qué desea hacer?: ").lower()

    if respuesta_usuario == "registrar":
        # *Registrar
        print("Has decidido registrar un nuevo alumno.")
        id_registrar = input("Ingrese el id del alumno: ").lower()
        if id_registrar in diccionario_principal:
            print("Error: Ese alumno ya esta registrado.")
        else:
            nombre_nuevo_alumno = input("Ingresa el nombre del alumno que deseas registrar: ")
            materias_nuevo_alumno = input("Ingresa la materia del alumno que deseas registrar: ").lower()
            if materias_nuevo_alumno not in tupla_materias:
                print("Error: No existe esa materia.")
            else:
                elementos = input("Ingrese las calificaciones separadas por comas: ")
                calificaciones_nuevo_alumno = [] 
                while True: # Bucle para forzar una entrada numérica válida entrada = input("Ingrese las 3 calificaciones separadas por comas: ") elementos = entrada.split(",")
                    try:
                        # Usamos una "list comprehension" para intentar convertir todo
                        calificaciones_nuevo_alumno = [float(cal.strip()) for cal in elementos]

                        # (Recomendado) Verificamos que sean 3 calificaciones
                        if len(calificaciones_nuevo_alumno) == 3:
                            break # ¡Éxito! Salimos del bucle
                        else:
                            print(f"Error: Debes ingresar exactamente 3 calificaciones. (Ingresaste {len(calificaciones_nuevo_alumno)})")
                    except ValueError:
                        print("Error: Una de las calificaciones no es un número. Intenta de nuevo.")
                nuevo_alumno = {"Nombre": nombre_nuevo_alumno, "Materia": materias_nuevo_alumno, "Calificaciones": calificaciones_nuevo_alumno}

    elif respuesta_usuario == "buscar":
        # *Buscar
        print("Has decidido buscar un alumno.")
        id_registrar = input("Ingrese el id del alumno: ").lower()
        if id_registrar not in diccionario_principal:
            print("Error: Ese alumno no esta registrado.")
        else:
            print("Nombre del alumno:", diccionario_principal[id_registrar]["Nombre"])
            print("Materia del alumno:", diccionario_principal[id_registrar]["Materia"])
            print("Calificaciones del alumno:", diccionario_principal[id_registrar]["Calificaciones"])
    elif respuesta_usuario == "promedio":
        # *Promedio
        print("Has decidido ver el promedio un alumno.")
        id_registrar = input("Ingrese el id del alumno: ").lower()
        if id_registrar not in diccionario_principal:
            print("Error: Ese alumno no esta registrado.")
        else:
            notas = diccionario_principal[id_registrar]["Calificaciones"]
            print("Promedio del alumno:", sum(notas)/len(notas))
    elif respuesta_usuario == "ver todos":
        # *Ver todos
        print("Has decidido ver la lista de todos los alumnos.")
        for clave, valor in diccionario_principal.items(): #! Iteramos sobre el diccionario anidado
            print(f"  {clave}: {valor}")
    elif respuesta_usuario == "salir":
        # *Salir
        estado_menu = False
        print("\nCerrando sistema de gestión de alumnos. ¡Hasta pronto!")
    else:
        print("Seleccione una opcion valida por favor.")