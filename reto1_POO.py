#* RETO 1 - POO

#  *TODO: Definir la Clase
class Componente:
    #* El Constructor
    def __init__(self, numero_serie, tipo_componente, costo):

        #* --- ATRIBUTOS ---
        # !Guardamos los datos DENTRO del objeto (self)
        self.numero_serie = numero_serie
        self.tipo = tipo_componente
        self.costo = costo

        # !Atributos por defecto
        self.historial_revisiones = []
        self.esta_activo = True

# *TODO: Crear los Objetos
c1 = Componente("MTR-1001", "Motor", 550.75)
c2 = Componente("SNR-2050", "Sensor", 80.20)

c1.historial_revisiones.append("2025-11-04")
c2.esta_activo = False

# *TODO: Imprimir un Reporte
print("\n--- REPORTE DE COMPONENTES ---")

print("\nComponente 1:")
print(f"Tipo: {c1.tipo}")
print(f"Número de Serie: {c1.numero_serie}")
print(f"Costo: ${c1.costo}")
print(f"Historial de Revisiones: {c1.historial_revisiones}")
print(f"¿Está Activo?: {c1.esta_activo}")

print("\nComponente 2:")
print(f"Tipo: {c2.tipo}")
print(f"Número de Serie: {c2.numero_serie}")
print(f"Costo: ${c2.costo}")
print(f"Historial de Revisiones: {c2.historial_revisiones}")
print(f"¿Está Activo?: {c2.esta_activo}")