import requests, os, dotenv, sqlite3
from funcs import create_table_region

if __name__ == '__main__':
    dotenv.load_dotenv('config.env')
    db_route = os.getenv('DB_ROUTE')
    if os.path.exists(db_route):
        print('banco de dados existe.')

    else:
        print('banco não existe')
        create = input(str('deseja criar um banco (y/n)?').lower())
        if create == 'y':
            conn = sqlite3.connect(db_route)
            cursor = conn.cursor()
            cursor.execute(create_table_region())
            conn.close()
            print('banco criado com sucesso')
        elif create == 'n':
            print('banco não criado')
            exit()
        else: 
            print('opção inválida')