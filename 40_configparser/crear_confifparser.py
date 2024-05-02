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


# Mariadb v10.7.4

#   public static void main(String[] args) {
# 37        String hostname = "msi.h.filess.io";
# 38        String database = "Lab_freedomill";
# 39        String port = "3305";
# 40        String username = "Lab_freedomill";
# 41        String password = "217050b98031c1ee067173e1f38c58727b47623c";
# 4243        MySQL mysql = new MySQL(hostname, database, port, username, password);
# 44        try {
# 45            Connection conn = mysql.connect();

# Escribir esa configuracion en un fichero "config.ini"

with open('config.ini', 'w') as configfile:
    config.write(configfile)
