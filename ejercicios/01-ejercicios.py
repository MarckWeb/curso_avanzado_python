'''1.- Escribe un programa que pida primero un número par y luego un número impar (positivos o negativos). En caso de que uno o los dos valores no sea correcto, se mostrará un único aviso.'''

'''2.- Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o negativo) y si el valor no es correcto, mostrará un aviso.'''

'''3.- Escribe un programa que pida primero un número par y a continuación un numero impar (positivos o negativos). En caso de que uno o los dos valores no sean correctos, se mostrarán uno o dos avisos.'''

'''4.- Escribe un programa que pida primero un número par y a continuación un numero impar (positivos o negativos). En cada petición, si el valor no es correcto se mostrará un aviso.'''


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


'''5. - Escribe un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí(en minúsculas y con tilde).'''


def main():
    print("DIGA 'sí' PARA CONTINUAR")

    respuesta = input("¿Desea continuar el programa?: ")

    while respuesta.lower() == "sí":
        respuesta = input("¿Desea continuar el programa?: ")

    print("¡Hasta la vista!")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
