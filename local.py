import requests,os,sqlite3
from dotenv import load_dotenv
load_dotenv('config.env')

if requests.get('https://esi.evetech.net/ui/').status_code == 200:
    regions = requests.get('https://esi.evetech.net/latest/universe/regions/')
    data = []
    for region in regions.json():
        data.append((region,None))
    #print(data)
    db_route = os.getenv('DB_ROUTE')
    #if os.path.exists(db_route):
    conn = sqlite3.connect(db_route)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Regions (region_id INTEGER, name text)')
    #cursor.executemany('INSERT INTO Regions(region_id, name) VALUES (:region_id ,:name)',data)
    cursor.executemany('INSERT INTO Regions(region_id, name) VALUES (?,?)',data)
    conn.commit()
    conn.close()
        #elif not os.path.exists(db_route):
            #pass