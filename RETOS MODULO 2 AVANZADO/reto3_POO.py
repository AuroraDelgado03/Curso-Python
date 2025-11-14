# Reto 3 - POO

#! Clase padre
class Vehiculo:
    #* Constructor
    def __init__(self, marca, modelo, anio):
        #* Atributos
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        #* Atributos por defecto
        self.kilometraje = 0
        self._encendido = False    #! Atributo protegido

    #? Métodos públicos
    def arrancar(self):
        if self._encendido == False:
            self._encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado.")
        else:
            print("El vehículo ya estaba en marcha.")

    def apagar(self):
        if self._encendido == True:
            self._encendido = False
            print(f"El {self.marca} {self.modelo} se ha apagado.")
        else:
            print("El vehículo ya estaba apagado.")

    #* Getter
    def get_kilometraje(self):
        return self.kilometraje
    
    def mostrar_info_base(self):
        print(f"Marca del vehículo {self.marca}")
        print(f"Modelo del vehículo {self.modelo}")
        print(f"Año del vehículo {self.anio}")

#! Clase hija Coche
class Coche(Vehiculo):
    #* Constructor hija
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)     #? Constructor del padre
        self.num_puertas = num_puertas      #! Atributo propio

    #? Métodos propios
    def conducir(self, km):
        if self._encendido == True:
            self.kilometraje += km
            print(f"Conduciendo {km} km...")
        else:
            print("Error: El coche debe estar arrancado para conducir.")

#! Clase hija Camión
class Camion(Vehiculo):
    #* Constructor hija
    def __init__(self, marca, modelo, anio, capacidad_carga_kg):
        super().__init__(marca, modelo, anio)      #? Constructor del padre
        self.capacidad_carga_kg = capacidad_carga_kg      #! Atributo propio
        self.__carga_actual_kg = 0     #!Atributo privado 

    #? Métodos propios
    def cargar(self, kilos):
        if self.__carga_actual_kg + kilos <= self.capacidad_carga_kg:
            self.__carga_actual_kg += kilos
            print("Carga exitosa.")
        else:
            print("Error: Sobrecarga.")

    def descargar(self, kilos):
        if kilos <= self.__carga_actual_kg:
            self.__carga_actual_kg -= kilos
            print("Descarga exitosa.")
        else:
            print("Error: Descarga una mayor cantidad a la almacenada")

    #* Getter
    def get_carga_actual(self):
        return self.__carga_actual_kg
    
#* --- USO ---
mi_coche = Coche("Toyota", "Corolla", 2020, 4)
mi_camion = Camion("Volvo", "FH16", 2018, 5000)

mi_coche.conducir(50)
mi_coche.arrancar()
mi_coche.conducir(100)
mi_coche.apagar()

mi_camion.cargar(3000)
mi_camion.cargar(3000)
mi_camion.descargar(1000)
print(f"Carga actual {mi_camion.get_carga_actual()} kg")