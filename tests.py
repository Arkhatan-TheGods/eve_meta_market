import requests
from time import sleep
base_url = 'https://esi.evetech.net/markets/groups/'
conn = requests.get(base_url)
data = []

for groups in conn.json():
    data.append(groups)
    #print(data)
    #sleep(2)

for id in range(len(data)):
    position = data[id]
    print(position)
    conn2 = requests.get(f'{base_url}{position}').json()
    print(conn2)
    sleep(5)
    exit()
"""IMPORTANTE: o id do Ship Equipment é 9
arrumado o problema de que ele mandava o request já com id 5
novo foco: pegar os nomes desse request"""
