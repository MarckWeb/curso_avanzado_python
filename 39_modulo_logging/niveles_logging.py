import logging

# logging.basicConfig()

# logging.basicConfig(filename='mi_archivo.log', level=logging.DEBUG, format='[%(asctime)s] %(levelname)s - %(message)s')
# logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(levelname)s - %(message)s')
# logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


logger = logging.getLogger()
# Establece el nivel de registro a DEBUG o superior
logger.setLevel(logging.DEBUG)

logger.critical('Mensaje critico')
logger.error('Mensaje error')
logger.warning('Mensaje warning')
logger.info('Mensaje informacion')
logger.debug('Mensaje debug')
