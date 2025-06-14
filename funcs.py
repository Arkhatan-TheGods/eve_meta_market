# reduzido tamanho por causa de repetição de código quando há possibilidade de concatenação
import requests

def urls_origins():
    url = {'main':'https://esi.evetech.net/ui/',
     'regions':'https://esi.evetech.net/latest/universe/regions/',
     'constellations':'https://esi.evetech.net/latest/universe/constellations/',
     'systems':'https://esi.evetech.net/latest/universe/systems/',
     'market_groups':'https://esi.evetech.net/markets/groups/'
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

def create_table_market_group() -> str:
     return '''CREATE TABLE IF NOT EXISTS Market_Group (ID INTEGER PRIMARY KEY AUTOINCREMENT,group_id INTEGER, name TEXT);'''


def regions_id(url) -> list:
     data = []
     regions = requests.get(url['regions'])
     for region in regions:
          data.append((region,None))
     return data

def constellations_id(url) -> list:
     data = []
     constellations = requests.get(url['constellations'])
     for constellation in constellations:
          data.append((constellation,None))
     return data

def regions_id(url) -> list:
     data = []
     systems = requests.get(url['systems'])
     for system in systems:
          data.append((system,None))
     return data

def markets_groups(url):
     data = []
     groups = requests.get(['markets_groups'])
     for group in groups:
          data.append((group,None))