# reduzido tamanho por causa de repetição de código quando há possibilidade de concatenação
def urls_origins():
    url = {'main':'https://esi.evetech.net/ui/',
     'regions':'https://esi.evetech.net/latest/universe/regions/',
     'constellations':'https://esi.evetech.net/latest/universe/constellations/',
     'systems':'https://esi.evetech.net/latest/universe/systems/',
     }
    return url

def create_table_region():
     return '''CREATE TABLE IF NOT EXISTS Regions (region_id INTEGER, name TEXT);'''

def create_table_constellation():
     return '''CREATE TABLE IF NOT EXISTS Constellations 
     (constellation_id INTEGER, region_id INTEGER, name TEXT);'''

def create_table_system():
     return '''CREATE TABLE IF NOT EXISTS Systems 
     (system_id INTEGER, constellation_id INTEGER, system_id INTEGER, name TEXT);'''

def create_table_item():
     return '''CREATE TABLE IF NOT EXISTS Itens (item_id INTEGER, name TEXT);'''