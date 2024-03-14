# 1.Pregunta 1
# Escribe una función que reciba dos strings (de largo > 2) como parámetros, y retorne un string de largo 4 que consista de las dos primeras letras del primer string y las últimas dos letras del segundo.

# Por ejemplo, si los strings son "familia" y "abrigarse", entonces tu función debe retornar "fase".

def mezclador(string_a, string_b):
    a = string_a[0:2]
    b = string_b[len(string_b) - 2] + string_b[len(string_b) - 1]
    return a + b


print(mezclador("familia", "abrigarse"))

# Pregunta 2
# Escriba una función que reciba dos strings como parámetros y retorne un nuevo string que consista del primero, pero con el segundo string intercalado entre cada letra del primero.

# Por ejemplo si los strings son "paz" y "so", entonces tu función debe retornar "psoasozso"


def intercalar(string_a, string_b):
    result = ''
    for i in range(len(string_a)):
        result += string_a[i] + string_b

    return result


print(intercalar("paz", "so"))

# Pregunta 3
# Escriba una función que reciba un string consistente de unos y ceros y retorne la cantidad de ocurrencias de unos menos la cantidad de ocurrencias de ceros.

# Por ejemplo, si el string es "11000110101", entonces tu función debe retornar 1 (ya que hay 6 unos y 5 ceros)


def ocurrencias(string):
    result = 0
    for i in range(len(string)):
        if string[i] == '1':
            result += 1
        else:
            result -= 1
    return result


print(ocurrencias("1011011110"))


# Escriba una función que reciba un string s y un número n como parámetros y retorne el mismo string s pero sin el elemento en el índice n.

# Por ejemplo, si s es "Hasta luego" y n es 3, entonces tu función debe retornar "Hasa luego".

# Hint: cuidado con aquellos casos en los que se tenga que eliminar un elemento de los bordes.

def remover_enesimo(s, n):
    new_s = s.strip()
    result = ''
    for i in range(len(new_s)):
        if i != n:
            result += new_s[i]
    return result


print(remover_enesimo("Hasta luego", 3))

# Pregunta 5
# Escriba una función que reciba un string como parámetro y retorne el string, pero con cada elemento que estuviese en mayúsculas reemplazado por "$". Asuma que el string consistirá solamente de letras.

# Por ejemplo si el string es "Viva la Vida", entonces tu función debe retornar "$iva la $ida".


def reemplazo(string):
    result = string
    i = 0
    while i < len(string):
        if string[i] == string[i].upper() and string[i] != ' ':
            result = result.replace(string[i], '$')
        i += 1
    return result


print(reemplazo("Viva la Vida"))
