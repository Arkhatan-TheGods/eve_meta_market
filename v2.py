import requests, sqlite3, funcs, dotenv

#o que fazer? verificar se existe um arquivo db, se deseja atualizar, 
if __name__ == "__main__":
    try:
        urls = funcs.urls()
        
        if requests.get(urls['main']) == 200:
            pass
            
    except Exception as e:
        print(e)