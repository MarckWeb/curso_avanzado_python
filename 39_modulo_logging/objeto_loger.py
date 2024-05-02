import logging

# Obtener el objeto logger
logger = logging.getLogger()
print(logger)

logger = logging.getLogger('Hola')
print(logger)
logger = logging.getLogger('Hola_Mundo')
print(logger)
logger = logging.getLogger(__name__)
print(logger)
