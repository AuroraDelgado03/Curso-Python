# Reto 3
# 15/10/2025

nombre = input("Ingresa tu nombre por favor: ")
anio = int(input("Ingresa tu año de nacimiento por favor: "))
juegos = input("Ingresa tus 3 videojuegos favoritos separados por comas: ").split(",")
perfil = [nombre] # *Lista de Perfil sin cambios
edad = int(2025 - anio)
perfil.append(edad) # *Lista de Perfil con año al final
perfil.extend(juegos) # *Lista de Perfil con videojuegos
perfil.insert(0, True) # *Lista de Perfil con True
juego_favorito = perfil.pop(3)
es_mayor_de_edad = edad >= 18
nombre_largo = len(nombre) > 10
es_gamer_retro = perfil.count("pacman") > 0
print("Perfil: ", perfil)
print("Videojuego favorito: ", juego_favorito)
print("Mayor de edad: ", es_mayor_de_edad)
print("Nombre largo: ", nombre_largo)
print("Gamer retro: ", es_gamer_retro)