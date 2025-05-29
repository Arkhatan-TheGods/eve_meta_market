import requests, os, dotenv, sqlite3
from funcs import create_table_region,urls_origins

if __name__ == '__main__':
    dotenv.load_dotenv('config.env')
    db_route = os.getenv('DB_ROUTE')
    urls = urls_origins()
    if os.path.exists(db_route):
        print('banco de dados existe.')
        add_data = input(str('deseja adicionar/atualizar regiões (y/n?').lower())
        if add_data == 'y':
            if requests.get(urls['main']) == 200:
                
                pass

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
