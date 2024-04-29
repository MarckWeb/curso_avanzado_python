import xml.etree.ElementTree as xmlet

# Elegir el documento.xml que vamos a procesar
empleados = xmlet.parse('empleados.xml')

# Nos posicionamos en la raiz del documento
root = empleados.getroot()

# crear un nuevo empleado
nuevo_empleado = xmlet.Element('empleado')

# crear las propiedades o subelementos de empleado
xmlet.SubElement(nuevo_empleado, 'id').text = '00134'
xmlet.SubElement(nuevo_empleado, 'nombre').text = 'Pepito Perez'
xmlet.SubElement(nuevo_empleado, 'email').text = 'pepito@gmail.com'
xmlet.SubElement(nuevo_empleado, 'dpto').text = 'Contabilidad'
xmlet.SubElement(nuevo_empleado, 'sueldo', {"moneda":"libras"}).text = '53000'

# Agregamos el nuevo empleado al root
root.append(nuevo_empleado)

# Escribimos el archivo
empleados.write("empleados_2.xml",method='')