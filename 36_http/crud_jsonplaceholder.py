import json
import requests


# fetch('https://jsonplaceholder.typicode.com/todos/1')
#       .then(response => response.json())
#       .then(json => console.log(json))
# Peticiones get

# OBTENER UN USUARIO
try:
    resp = requests.get('https://jsonplaceholder.typicode.com/users/1')
    print(resp)
except:
    print('erro')
else:
    print(resp.json())

# ACTUALIZAR UN USUARIO
print('--------ACTUALIZAR UN USUARIO-----')
new_user = {
    'id': 1,
    'name': 'David Marckk',
    'username': 'Bret',
    'email': 'Sincere@april.biz',
            'address':
                {'street': 'Kulas Light',
                 'suite': 'Apt. 556',
                 'city': 'Gwenborough',
                 'zipcode': '92998-3874',
                 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org',
            'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}
}
cabecera = {'Content-type': 'aplication/json'}
try:
    resp = requests.put('https://jsonplaceholder.typicode.com/users/1',
                        headers=cabecera, data=json.dumps(new_user))
    new_user = requests.get('https://jsonplaceholder.typicode.com/users/1')
except:
    print('error al actualizar')
else:
    print('Datos actualizados de ', resp.json())
    print('nuevo user')
    print(new_user.json())
print('-'*50)
