# reduzido tamanho por causa de repetição de código quando há possibilidade de concatenação
import requests

def urls_origins():
    url = {'main':'https://esi.evetech.net/ui/',
     'regions':'https://esi.evetech.net/latest/universe/regions/',
     'constellations':'https://esi.evetech.net/latest/universe/constellations/',
     'systems':'https://esi.evetech.net/latest/universe/systems/',
     }
    return url

def create_table_region() -> str:
     return '''CREATE TABLE IF NOT EXISTS Regions (region_id INTEGER, name TEXT);'''

def create_table_constellation() -> str:
     return '''CREATE TABLE IF NOT EXISTS Constellations 
     (constellation_id INTEGER, region_id INTEGER, name TEXT);'''

def create_table_system() -> str:
     return '''CREATE TABLE IF NOT EXISTS Systems 
     (system_id INTEGER, constellation_id INTEGER, system_id INTEGER, name TEXT);'''

def create_table_item() -> str:
     return '''CREATE TABLE IF NOT EXISTS Itens (item_id INTEGER, name TEXT);'''

def regions_id(url) -> list:
     data = []
     regions = requests.get(url['regions'])
     for region in regions:
          data.append((region,None))
     return data
