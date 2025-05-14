import requests

def status_server():

    site = 'https://esi.evetech.net/'
    conn = requests.get(site)
    if conn.status_code == 200:
        print('Tudo certo!')
        return site, conn
    else:
        print(f"Erro: {conn.status_code} - {conn.reason}")
        return None

def get_regions_id(site, conn):

    if site and conn:  # Ensure valid values
        url = f"{site}latest/universe/regions/"
        response = requests.get(url)

        if response.status_code == 200:
            regions_id = response.json()
            print(f"Regiões encontradas: {regions_id}")
            return regions_id
        else:
            print(f"Erro ao obter regiões: {response.status_code}")
            return None

if __name__ == "__main__":
    result = status_server()
    if result:
        site, conn = result
        get_regions_id(site, conn)
