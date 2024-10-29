# Programa calculadora
## Pedir dos números al usuario
## Pedir un operador
## mostrar el resultado de la operación por pantalla


def operacion():
    return input('introduce el signo de opracion: ')
    

def resultado (signo, numero1, numero2):
    
    if signo == '+':
        return(numero1 + numero2)
    if signo == '-':
        return(numero1 - numero2)
    if signo == '*':
        return(numero1 * numero2)
    if signo == '/':
        return(numero1 / numero2)

def calcular():
    print('======Calculadora=====\n -----Nota:----\n ingresa un numero seguido\n de la operacion a realizar\n y despues el otro numero')

    numero1 = float(input('introduce un numero: '))
    if numero1: 
        signo = operacion()
        print(signo)
    
    if numero1 and signo:
        numero2 = float(input(f'Introduce el numero a {signo}: '))
        result = resultado(signo, numero1, numero2)
        return result
    
print(calcular())




