'''
Crear un script que gestione el inventario de licencias de herramientas de ciberseguridad, utilizando bucles for para iterar a través de las herramientas almacenadas y simular una adquisición de herramientas del inventario.
'''

inventario = [
    (50, 'Nmap', 0.5), 
    (30, 'Wireshark', 0.3), 
    (20, 'Metasploit', 0.4), 
    (15, 'Burp Suite', 0.45)
]

valor_total = 0
mayor_cantidad = {
    'herramienta':'',
    'cantidad': 0,
    'precio': 0
}

for items in inventario:
    cantidad, nombre, precio = items
    valor_total += cantidad * precio
    if cantidad > mayor_cantidad['cantidad']:
        mayor_cantidad['cantidad'] = cantidad
        mayor_cantidad['herramienta'] = nombre
        mayor_cantidad['precio'] = precio
  
print(f'Valor total del inventario: {valor_total} eur')
print(f'Herramienta con mayor cantidad de licencias: {mayor_cantidad["herramienta"]} ({mayor_cantidad["cantidad"]} unidades)')


'''SEGUNDA PARTE'''
compra = {
    "Nmap": 5,
    "Wireshark": 3
}
precio_total=0

for items in inventario:
    cantidad, nombre, precio = items
    if nombre in compra:
        precio_total += precio * compra[nombre]

print(f'Precio de la adquisicion: {precio_total} eur')