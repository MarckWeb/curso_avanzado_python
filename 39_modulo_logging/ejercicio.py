# Con un alista de numeros en modo texto "1", colocar "tres"
# parsear a numero entero
# manejo de errores, excepciones
# los errores llevarlos a un archivo de log
# import logging

# FORMAT = '[%(asctime)s]%(levelname)s:%(name)s - %(message)s'

# logging.basicConfig(
#     level=logging.CRITICAL, filename="ejercicio.log", filemode="a", format=FORMAT
# )
# # coloca un nombre enves de root
# logger = logging.getLogger("log_critical")

# logging.basicConfig(level=logging.ERROR,
#                     filename="ejercicio2", filemode='a', format=FORMAT)
# logger2 = logging.getLogger('log_error')

# datos = ['1', '2', 'tres', '4', '5']

# suma = 0

# for dato in datos:
#     try:
#         num = int(dato)
#     except Exception as ex:
#         print(ex)
#         # logger.setLevel(logging.CRITICAL)
#         logger.critical(ex)
#         logger.setLevel(logging.ERROR)
#         logger2.error(ex)
#     else:
#         suma *= num

# print('Suma', suma)

import logging

FORMAT = '[%(asctime)s]%(levelname)s:%(name)s - %(message)s'

# Configuración del registro para registrar mensajes críticos en 'ejercicio.log'
logger = logging.getLogger("log_critical")
logger.setLevel(logging.CRITICAL)
file_handler = logging.FileHandler("ejercicio.log")
file_handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_handler)

# Configuración del registro para registrar mensajes de error en 'ejercicio2.log'
logger2 = logging.getLogger('log_error')
logger2.setLevel(logging.ERROR)
error_handler = logging.FileHandler("ejercicio2.log")
error_handler.setFormatter(logging.Formatter(FORMAT))
logger2.addHandler(error_handler)

datos = ['1', '2', 'tres', '4', '5']

suma = 0

for dato in datos:
    try:
        num = int(dato)
    except Exception as ex:
        print(ex)
        # Registra el error en ambos archivos de registro
        logger.critical(ex)
        logger2.error(ex)
    else:
        suma += num

print('Suma:', suma)
