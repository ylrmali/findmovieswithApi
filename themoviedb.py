from pydoc import text
from urllib import response
import requests
import json

# themoviedb.org => film ve dizi arsivi
# themoviedn' nin sundugu apiyi uygulamada kullan.
# Anahtar kelimeye gore arama
# En populer film listesi
# vizyondaki film listesi

class Movie:
    def __init__(self):
        self.acces_key = '0f94473a97abfa4b8f140316a8f02e63'
        self.api_popular= 'https://api.themoviedb.org/3/movie/popular?api_key='
        self.api_upcoming = 'https://api.themoviedb.org/3/movie/upcoming?api_key='
        self.api_search = 'https://api.themoviedb.org/3/search/movie?api_key='

    def getpopular(self):
        response = requests.get(self.api_popular+self.acces_key)
        return response.json()
    
    def getUpcoming(self):
        response = requests.get(self.api_upcoming+self.acces_key)
        return response.json()

    def getSearch(self,text):
        response = requests.get(self.api_search+self.acces_key+'&query='+text)
        return response.json()


run = Movie()

while True:
    print('MENÜ'.center(50,'-'))
    ask_activity = input("1- Populer Filmler\n2- Vizyondaki Filmler\n3- Özel Arama\n4- Çıkış\n*Seçiminiz: ")
    if ask_activity == '4':
        break
    else:
        if ask_activity =='1':
           print('-'*50)
           data = run.getpopular()
           for d in data['results']:
               print(d['title'])
            
        elif ask_activity =='2':
            print('-'*50)
            n_data = run.getUpcoming()
            print(f"***{n_data['dates']}***")
            for nd in n_data['results']:
                print(nd['title']) 
        elif ask_activity =='3':
            print('-'*50)
            search = input('Lütfen film ismi veya anahtar kelime giriniz: ')
            print('-'*50)
            s_data = run.getSearch(search)
            for sd in s_data['results']:
                print(sd['title'])
        else:
            print('Missed Choise')





