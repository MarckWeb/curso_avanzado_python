import logging

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'
print(type(FORMAT))

logger = logging.getLogger()


# Los mensajes de los vayan a un archivo de log

fichero = logging.FileHandler('archivo.log', mode='w')
formato = logging.Formatter(FORMAT)
fichero.setFormatter(formato)

logger.addHandler(fichero)

logger.critical('Mensaje critico')
logger.error('Mensaje error')
logger.warning('Mensaje warning')
