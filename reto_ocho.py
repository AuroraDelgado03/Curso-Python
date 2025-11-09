# Reto 8

base_de_partes = {}
componentes_validos = ("motor", "sensor", "bateria", "chasis")

# *Registrar
def registrar():
    print("\nHas decidido registrar una nueva pieza.")
    num_serie = input("Ingrese el numero de serie de la pieza: ").lower()
    
    if num_serie in base_de_partes:
        print("Error: Ya existe una pieza con ese número de serie.")
    elif num_serie == "": # *Verifica que no ingrese una pieza vacía
        print("Error: No se puede agregar una pieza sin S/N.")
    else:
        tipo_componente = input("Ingresa el tipo de componente de la pieza: ").lower()
        if tipo_componente not in componentes_validos:
            print("Error: No es un componente valido.")
        else:
            resultados_pruebas = []
            while True:
                entrada = input("Ingresa los tres resultados de las pruebas realizadas separadas por comas: ")
                elementos = entrada.split(",")
                try:
                    resultados_pruebas = [float(cal.strip()) for cal in elementos]
                    if len(resultados_pruebas) == 3:
                        break
                    else:
                        print(f"Error: Debes ingresar exactamente 3 resultados.")
                except ValueError: #! Error por si no todo es un número
                    print("Error: Una de las calificaciones no es un número. Intenta de nuevo.")           
            nueva_parte = {"Tipo de componente": tipo_componente, "Resultado de las pruebas": resultados_pruebas, "Estado": "Pendiente"}
            base_de_partes[num_serie] = nueva_parte
            print(f"Pieza registrada correctamente")

# *Buscar
def buscar():
    print("\nHas decidido buscar una pieza.")
    num_serie = input("Ingrese el S/N de la pieza: ").lower()
    if num_serie not in base_de_partes:
        print("Error: Esa pieza no esta registrada.")
    else:
        print("Tipo de componente:", base_de_partes[num_serie]["Tipo de componente"])
        print("Resultado de las pruebas:", base_de_partes[num_serie]["Resultado de las pruebas"])
        print("Estado", base_de_partes[num_serie]["Estado"])

# *Evaluar
def evaluar():
    print("\nHas decidido evaluar una pieza.")
    num_serie = input("Ingrese el S/N de la pieza: ").lower()
    if num_serie not in base_de_partes:
        print("Error: Esa pieza no esta registrada.")
    else:
        notas = base_de_partes[num_serie]["Resultado de las pruebas"]
        promedio = sum(notas)/len(notas)
        print("Promedio: ", promedio)
        if promedio >= 90.0:
            print("La pieza ha sido aprobada")
            base_de_partes[num_serie]["Estado"] = "Aprobado"
        else:
            print("La pieza ha sido rechazada")
            base_de_partes[num_serie]["Estado"] = "Rechazado"

# *Ver inventario
def ver_inventario():
    print("\nHas decidido ver las piezas en el inventario.")
    for clave, valor in base_de_partes.items(): #! Iteramos sobre el diccionario anidado
        print(f"  {clave}: {valor}")

# *Conteo
def conteo():
    print("\nHas decidido contar la cantidad de productos de una pieza")
    tipo_componente = input("Ingresa el tipo de componente de la pieza: ").lower()
    if tipo_componente not in componentes_validos:
        print("Error: No es un componente valido.")
    else:
        contador = 0
        for pieza in base_de_partes.values(): #! Devuelve una vista de los valores del diccionario
            if pieza["Tipo de componente"] == tipo_componente:
                contador += 1
        
        print(f"Hay {contador} piezas del tipo '{tipo_componente}'.")

# *Salir
def salir():
    print("\nCerrando sistema. ¡Hasta pronto!")

estado_menu = True
while estado_menu:
    print("\nMenú de opciones")
    print("1. Registrar")
    print("2. Buscar")
    print("3. Evaluar")
    print("4. Ver inventario")
    print("5. Conteo")
    print("6. Salir")
    respuesta_usuario = input("¿Qué desea hacer?: ").lower()

    if respuesta_usuario == "registrar":
        registrar()
    elif respuesta_usuario == "buscar":
        buscar()
    elif respuesta_usuario == "evaluar":
        evaluar()
    elif respuesta_usuario == "ver inventario":
        ver_inventario()
    elif respuesta_usuario == "conteo":
        conteo()
    elif respuesta_usuario == "salir":
        salir()
        estado_menu = False
    else:
        print("Seleccione una opcion valida por favor.")