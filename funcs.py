# reduzido tamanho por causa de repetição de código quando há possibilidade de concatenação
def urls():
    url = {'main':'https://esi.evetech.net/ui/',
     'regions':'https://esi.evetech.net/latest/universe/regions/',
     'constellations':'https://esi.evetech.net/latest/universe/constellations/',
     'systems':'https://esi.evetech.net/latest/universe/systems/',
     }
    return url

def create_table_region():
     return '''CREATE TABLE IF NOT EXISTS Regions (region_id INTEGER, name TEXT, description TEXT);'''