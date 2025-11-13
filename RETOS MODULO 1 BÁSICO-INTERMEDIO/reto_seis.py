# Reto 6
# 20/10/2025

# *TODO: El programa debe empezar con una lista que ya contenga algunos artículos
inventario_estacion_espacial = ["agua", "oxigeno", "trajes espaciales", "herramientas", "medicamentos", "baterías"]
print("\nEl inventario contiene: ", inventario_estacion_espacial)

# *Bucle principal 
estado_menu = True
while estado_menu:

    # *TODO: Menú de opciones
    print("\nAñadir")
    print("Quitar")
    print("Ver")
    print("Inspeccionar")
    print("Salir")
    respuesta = input("¿Que desea hacer con el inventario?: ").lower()

    if respuesta == "añadir":
        # *Añadir
        print("\nDecidiste agregar productos.")
        articulo_agregar = input("¿Que producto desea agregar al inventario?: ").lower()
        if articulo_agregar: # Esta línea checa si el string 'articulo_agregar' no está vacío
            inventario_estacion_espacial.append(articulo_agregar)
            print("Aqui esta tu inventario actualizado: ", inventario_estacion_espacial)
        else:
            print("Error: No se puede agregar un artículo sin nombre.")

    elif respuesta == "quitar":
        # *Quitar
        print("\nDecidiste quitar productos.")
        articulo_eliminar = input("¿Que producto desea quitar del inventario?: ").lower()
        if inventario_estacion_espacial.count(articulo_eliminar) == 0:
            print("Error: Ese ítem no existe en el inventario.")
        else:
            inventario_estacion_espacial.remove(articulo_eliminar)
            print("Aqui esta tu inventario actualizado: ", inventario_estacion_espacial)
    elif respuesta == "ver":
        # *Ver
        print("\nDecidiste revisar los productos.")
        if len(inventario_estacion_espacial) == 0:
            print("Error: El inventario esta vacio.")
        else:
            inventario_estacion_espacial.sort()
            print("Aqui esta el inventario: ", inventario_estacion_espacial)
    elif respuesta == "inspeccionar":
        # *Inspeccionar
        print("\nDecidiste inspeccionar los productos.")
        while True:
            try:
                num_item = int(input("¿Que numero de item quieres inspeccionar?: "))
                print("El articulo con ese numero de item es: ", inventario_estacion_espacial[num_item])
                break
            # !Error por no ingresar un número
            except ValueError:
                print("Error: Debes introducir un NÚMERO.")
            # !Error exceder el número de índice
            except IndexError:
                print(f"Error: ¡Ese índice no existe! Solo tienes {len(inventario_estacion_espacial)} ítems.")
    elif respuesta == "salir":
        # *Salir
        estado_menu = False
        print("\nCerrando sistema de inventario. ¡Hasta pronto!")
    else:
        print("Seleccione una opcion valida por favor.")