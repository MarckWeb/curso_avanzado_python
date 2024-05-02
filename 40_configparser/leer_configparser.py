import configparser

# Obtener el objeto config
config = configparser.ConfigParser()

# Leer el archivo
# config.read_dict({'mariadb': {'host': 'localhost'}})
config.read(filenames='config.ini')

# Mostrar secciones
print(config.sections())  # ['sqlite', 'mysql', 'mariadb']


# mostrar los datos de mariadb
print(config['mariadb']['host'])
print(config['mariadb']['puerto'])
print(config['mariadb']['usuario'])
print(config['mariadb']['password'])
print(config['mariadb']['database'])
