import requests, sqlite3, funcs

if __name__ == "__main__":
    try:
        urls = funcs.urls()
        if requests.get(urls['main']) == 200:
            print('funcionou')
        #main_url = 'https://esi.evetech.net/ui/'
        #conn = requests.get(main_url)
        #if conn.status_code == 200:
            
    except Exception as e:
        print(e)