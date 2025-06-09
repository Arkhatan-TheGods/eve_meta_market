import requests
from time import sleep
base_url = 'https://esi.evetech.net/markets/groups/'
conn = requests.get(base_url)
data = []

for groups in conn.json():
    data.append(groups)
    #print(data)
    #sleep(2)

for id in data:
    position = data[id]
    conn2 = requests.get(f'{base_url}{position}').json()
    print(conn2)
    sleep(5)

"""IMPORTANTE: o id do Ship Equipment é 9"""