# Reto 4
# 16/10/2025

articulos = ["leche", "pan", "jugo", "guayaba", "chocolate"]
print("Tu carrito de compras contiene: ", articulos)
print("\nAñadir(A)")
print("Quitar(Q)")
print("Revisar(R)")
respuesta = input("¿Que desea hacer con su carrito?: ").upper()

if respuesta == "A":
    # Añadir
    print("\nDecidiste agregar productos")
    articulo_agregar = input("¿Que producto desea agregar a su carrito?: ").lower()
    articulos.append(articulo_agregar)
    print("Aqui esta tu carrito actualizado: ", articulos)
elif respuesta == "Q":
    # Quitar
    print("\nDecidiste quitar productos")
    articulo_eliminar = input("¿Que producto desea quitar a su carrito?: ").lower()
    if articulos.count(articulo_eliminar) == 0:
        print("No existe el articulo: ", articulo_eliminar)
    else:
        articulos.remove(articulo_eliminar)
        print("Aqui esta tu carrito actualizado: ", articulos)
elif respuesta == "R":
    # Revisar
    print("\nDecidiste revisar tus productos")
    print("Aqui esta tu carrito actualizado: ", articulos)
else:
    print("Seleccione una opcion valida por favor")