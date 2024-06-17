'''1.- Escribe un programa que pida primero un número par y luego un número impar (positivos o negativos). En caso de que uno o los dos valores no sea correcto, se mostrará un único aviso.'''

'''2.- Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o negativo) y si el valor no es correcto, mostrará un aviso.'''

def obtener_numero_par():
    while True:
        try:
            numero_par = int(input('Introduce un numero par: '))
            if numero_par % 2 != 0:
                print("El número no es par. Por favor, introduce un número par.")
            else:
                return numero_par

        except ValueError:
            print("Entrada inválida. Por favor, introduce un número par.")


def obtener_numero_impar():
    while True:
        try:
            numero_impar = int(input('Introduce un número impar:  '))
            if numero_impar % 2 == 0:
                print("El número no es impar. Por favor, introduce un número impar.")
            else:
                return numero_impar
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número impar.")


numero_par = obtener_numero_par()
numero_impar = obtener_numero_impar()

print("Número par:", numero_par)
print("Número impar:", numero_impar)


'''3. - Escribe un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí(en minúsculas y con tilde).'''


def main():
    print("DIGA 'sí' PARA CONTINUAR")

    respuesta = input("¿Desea continuar el programa?: ")

    while respuesta.lower() == "sí":
        respuesta = input("¿Desea continuar el programa?: ")

    print("¡Hasta la vista!")


# Punto de entrada del programa
if __name__ == "__main__":
    main()

'''Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+2/2-5 ^2).'''
resultado = (3+2/2-5)**2
print(resultado)


'''Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.'''

def sueldo_usuario():
    while True:
        try:
            # Pedir al usuario el número de horas trabajadas
            horas = float(input('Ingresa las horas trabajadas: '))
            if horas < 0:
                raise ValueError("Las horas trabajadas no pueden ser negativas.")
            
            # Pedir al usuario el coste por hora
            coste_hora = float(input('Ingresa el coste por hora: '))
            if coste_hora < 0:
                raise ValueError("El coste por hora no puede ser negativo.")
            
            # Calcular el sueldo
            sueldo = horas * coste_hora
            return sueldo

        except ValueError as e:
            # Manejo de excepción si hay un error de valor
            print(f"Entrada inválida: {e}. Por favor, introduce un valor válido.")
        except Exception as e:
            # Manejo de cualquier otra excepción no anticipada
            print(f"Ha ocurrido un error: {e}")

# Llamar a la función para calcular el sueldo y mostrar el resultado
sueldo_a_pagar = sueldo_usuario()
print(f'El sueldo a pagar es: {sueldo_a_pagar}')

'''Ejercicio 6
Escribir un programa que lea un entero positivo, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n
. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:'''

n = int(input('Intriduce un numero entero: '))

if n > 0:
    suma = n * (n+1)//2
    print(f"La suma de todos los enteros desde 1 hasta {n} es: {suma}")

else:
    print("El número introducido no es un entero positivo.")


'''Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.'''

def calcularIMC(peso, estatura):
    if estatura == 0 or peso == 0:
        return "La estatura no puede ser cero. Por favor, ingrese valores válidos."
    else:
        imc = peso / (estatura ** 2)
        return imc

def interpretarIMC(imc):
    if imc < 18.5:
        return "Categoría: Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Categoría: Peso normal"
    elif 25 <= imc < 29.9:
        return "Categoría: Sobrepeso"
    else:
        return "Categoría: Obesidad"

peso = float(input('Introduce tu peso en kilogramos: '))
estatura = float(input('Introduce tu estatura en metros: '))
imc = calcularIMC(peso, estatura)

# objeto que verifica el tipo de salida de imc si number o string
if isinstance(imc, str):
    print(imc) 
else:
    print(f"Tu IMC es: {imc:.2f}")
    print(interpretarIMC(imc))


'''Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.'''


'''Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.'''


'''Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.'''


'''Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.'''


'''Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.'''

'''mas ejercicios'''
#https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/
# https://www.mclibre.org/consultar/python/
