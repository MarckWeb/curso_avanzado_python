import json
import requests


'''Accedemos a la api de chucknorri
mostramos los chistes '''

try:
    resp = requests.get('https://api.chucknorris.io/jokes/random/')
    dato = resp.json()

except requests.RequestException:
    print('ha ocurrido un error')
else:
    if resp.status_code == requests.codes.ok:
        print(dato['value'])
print('-'*50)


'''Accedemos a la api de pokemon
mostramos los chistes '''
print('--------API POKEMON-------')
try:
    resp = requests.get('https://pokeapi.co/api/v2/pokemon/')
    dato = resp.json()

except requests.RequestException:
    print('ha ocurrido un error')
else:
    if resp.status_code == requests.codes.ok:
        print(dato)
print('-'*50)
