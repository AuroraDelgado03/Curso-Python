# Reto 2 - Calculadora
# 14/10/2025
a = int(input("Ingresa un numero por favor: "))
b = int(input("Ingresa otro numero por favor: "))

print(f"La suma de {a} + {b} es: {a + b}")
print(f"La resta de {a} - {b} es: {a - b}")
print(f"La multiplicacion de {a} * {b} es: {a * b}")
print(f"La division de {a} / {b} es: {a / b}")
print(f"El modulo 2 de {a} y {b} es: {a % 2} y {b % 2}")
print(f"La potencia cubica de {a} y {b} es: {a ** 3} y {b ** 3}")

x = int(input("\nIngresa un numero por favor: "))
y = int(input("Ingresa otro numero por favor: "))

x += 2
y += 2
print(f"La asignacion suma (2) es: {x} y {y}")
x -= 13 
y -= 13
print(f"La asignacion resta (13) es: {x} y {y}")
print(f"{x} es igual a {y}: {x == y}")
print(f"{x} es diferente de {y}: {x != y}")
print(f"{x} es mayor que {y}: {x > y}")
print(f"{x} es menor que {y}: {x < y}")

# Tabla de verdad
p = True
q = False

print("\nTABLA DE VERDAD - AND")
print("p\tq\tp AND q")
print(p, "\t", p, "\t", p and p)
print(p, "\t", q, "\t", p and q)
print(q, "\t", p, "\t", q and p)
print(q, "\t", q, "\t", q and q)

print("\nTABLA DE VERDAD - OR")
print("p\tq\tp OR q")
print(p, "\t", p, "\t", p or p)
print(p, "\t", q, "\t", p or q)
print(q, "\t", p, "\t", q or p)
print(q, "\t", q, "\t", q or q)

print("\nTABLA DE VERDAD - NOT")
print("p\tNOT p")
print(p, "\t", not p)
print(q, "\t", not q)
