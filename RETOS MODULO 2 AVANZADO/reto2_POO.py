#* Reto 2 - Ejercicio tipo entrevista

#? para importar una constante predefinida que contiene los signos de puntuación
from string import punctuation

palabras_a_buscar = ["dostoievski", "sinónimos", "horiki", "humanos", "miedo", "palabras"]
diccionario_palabras = {}

try:
    with open("Fragmento_Indigno_de_ser_humano.txt", "r") as f:
        for linea in f:
            #! .strip() para limpiar el \n y espacios
            #! .lower() para pasar todo a minúsculas
            linea_limpia = linea.strip().lower()
            
            #! .replace() para quitar los signos de puntuación
            for signo in punctuation:
                linea_limpia = linea_limpia.replace(signo, "")
            lista_palabras = linea_limpia.split() #! para dividir la línea en palabras
            
            for palabra in lista_palabras:
                if palabra in palabras_a_buscar:
                    if palabra in diccionario_palabras:
                        diccionario_palabras[palabra] += 1
                    else:
                        diccionario_palabras[palabra] = 1
except FileNotFoundError:
    print("❌ ERROR: No se encontró 'Fragmento_Indigno_de_ser_humano.txt'. Ejecuta el script de escritura primero.")

#? w crea el archivo automáticamente si no existe
with open("resultado_conteo.txt", "w") as f:
        f.write(str(diccionario_palabras))  
print("Conteo guardado en 'resultado_conteo.txt'")