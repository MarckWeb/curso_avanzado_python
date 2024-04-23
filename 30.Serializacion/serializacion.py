import shelve

# Abrir el fichero en modo escritura
fichero = "fichero.shlv"
stream = shelve.open(fichero, flag='n')

# Escribir
stream['Juan'] = {'Matematicas': 7.5, 'Lengua': 4.2}
stream['Maria'] = {'Matematicas': 3.7, 'Lengua': 7.9, 'Arte': 5.5}
stream.close()

'''
r => dbm.error: db file doesn't exist; use 'c' or 'n' flag to create a new db
w => dbm.error: db file doesn't exist; use 'c' or 'n' flag to create a new db
c => si existe lo abre en lectura/escritura y sino la crea
n => siempre lo crea nuevo y lo abre en modo lectura/escritura
'''

# Lectura
stream = shelve.open(fichero)
print('Notas de Maria', stream['Maria'])
stream.close()
