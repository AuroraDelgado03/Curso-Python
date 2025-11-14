# Reto 9

TIPOS_ENTRADA_VALIDOS = ("observacion", "prueba", "error", "mantenimiento")
ARCHIVO_LOG = "laboratorio.txt"

# *Registrar
def registrar():
    print("\nHas decidido registrar una nueva nota.")
    print("Tipos válidos:", ", ".join(TIPOS_ENTRADA_VALIDOS))
    tipo_de_entrada = input("Ingrese el tipo de entrada: ").lower()
    if tipo_de_entrada not in TIPOS_ENTRADA_VALIDOS:
        print("Error: No es un tipo de entrada valido.")
        return
    else: 
        descripcion = input("Ingrese la descripción de la nota: ").strip()
        if descripcion == "":
            print("La descripción no puede estar vacía.")
            return

    with open(ARCHIVO_LOG, "a") as archivo:
        archivo.write(f"TIPO: {tipo_de_entrada} - DESCRIPCIÓN: {descripcion}\n")
    print("Entrada registrada correctamente.")

# *Ver log
def ver_log():
    print("\nHas decidido ver el contenido del log.")
    try:
        with open(ARCHIVO_LOG, "r") as archivo:
            contenido = archivo.read()
        if contenido.strip() == "":
            print("El log está vacío.\n")
        else:
            print(contenido)
    except FileNotFoundError:
        print("El log está vacío o no se ha creado todavía.\n")

# *Salir
def salir():
    print("\nCerrando sistema. ¡Hasta pronto!")

def main():
    estado_menu = True
    while estado_menu:
        print("\nMenú de opciones")
        print("1. Registrar")
        print("2. Ver log")
        print("3. Salir")
        respuesta_usuario = input("¿Qué desea hacer?: ").lower()

        if respuesta_usuario == "registrar":
            registrar()
        elif respuesta_usuario == "ver log":
            ver_log()
        elif respuesta_usuario == "salir":
            salir()
            estado_menu = False
        else:
            print("Seleccione una opcion valida por favor.")

main()