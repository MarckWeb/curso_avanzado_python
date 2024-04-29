import xml.etree.ElementTree as xmlet

# Elegir el documento.xml que vamos a procesar
empleados = xmlet.parse('empleados.xml')

# Nos posicionamos en la raiz del documento
root = empleados.getroot()

# mostrar la etiqueta raiz
print(root.tag)   # empleados

# Recorrer los empleados que tenemos en el documento xml
for empl in empleados.findall('empleado'):
    print(empl.tag)
    for propiedad in empl:
        if propiedad.tag == 'sueldo':
            print(propiedad.tag, ":", propiedad.text, propiedad.attrib['moneda'])
        else:
            print(propiedad.tag, ":", propiedad.text)