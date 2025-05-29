import requests, os, dotenv, sqlite3
from funcs import create_table_region,urls_origins

if __name__ == '__main__':
    dotenv.load_dotenv('config.env')
    db_route = os.getenv('DB_ROUTE')
    urls = urls_origins()
    if os.path.exists(db_route):
        print('banco de dados existe.')
        update_region = input(str('deseja adicionar/atualizar regiões (y/n?').lower())
        if update_region == 'y':
            print('ok')
            #if requests.get(urls['main']) == 200:
            print(urls['regions'])
    
            regions = requests.get(urls['regions'])
            
            for region_id in regions.json():
                #print(region)
                region_data = requests.get(f'{urls['regions']}{region_id}')
                #print(region_data.json())
                region_data_json = region_data.json()
                #print(region_data_json['constellations'])
                for constellation_id in region_data_json['constellations']:
                    constellation_data = requests.get(f'{urls['constellations']}{constellation_id}')
                    #print(constellation_data.json())
                    for system_id in constellation_data.json()['systems']:
                        system_data = requests.get(f'{urls['systems']}{system_id}')
                        print(system_data.json())
                        break

                    break
                break

    else:
        print('banco não existe')
        create = input(str('deseja criar um banco (y/n)?').lower())
        if create == 'y':
            conn = sqlite3.connect(db_route)
            cursor = conn.cursor()
            cursor.execute(create_table_region())
            conn.commit()
            conn.close()
            print('banco criado com sucesso')
        elif create == 'n':
            print('banco não criado')
            exit()
        else: 
            print('opção inválida')
