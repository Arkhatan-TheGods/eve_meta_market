import requests, sqlite3, funcs, os
from dotenv import load_dotenv
#o que fazer? verificar se existe um arquivo db, se deseja atualizar, 
if __name__ == "__main__":
    try:
        urls = funcs.urls()
        #colocar a função que verifica se existe um db e se caso não existir criar um, baixar as ids
        if requests.get(urls['main']) == 200:
            pass
            
    except Exception as e:
        print(e)