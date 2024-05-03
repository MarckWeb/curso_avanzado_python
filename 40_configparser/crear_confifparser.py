import configparser

# Obtener el objeto config
config = configparser.ConfigParser()

# Crear la configurecion (accesos a las BBDD)
config['DEFAULT'] = {'host': 'localhost'}
config['sqlite'] = {
    'host': 'localhost',
    'database': 'tienda.db'
}
config['mysql'] = {
    'host': "localhost",
    'user': 'root',
    'port': '3307',
    'password': '123456',
    'database': 'cetelem'
}

config['mariadb'] = {
    'host': 'msi.h.filess.io',
    'port': '3305',
    'user': 'Lab_freedomill',
    'database': 'Lab_freedomill',
    'password': '217050b98031c1ee067173e1f38c58727b47623c',
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)
