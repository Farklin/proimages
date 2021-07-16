import requests
from bs4 import BeautifulSoup 



class SearchContentForPost: 
    
    def __init__(self, url): 
        self.url = url
        self.r = requests.get(url, verify=False)
        self.bs = BeautifulSoup(self.r.content, 'html.parser')

    def search_atribyte(self): 
        table = self.bs.select('.table-data-sheet')

        mas_attr = [] 
        attr = {}
        for tr in table[0].select('tr'): 
            attr = tr.select('td')[0].text + ': ' +  tr.select('td')[1].text 
            mas_attr.append(attr)

        return mas_attr

    def search_description(self): 
        description = ''
        desc = self.bs.select('#short_description_content')[0]
        for p in desc.select('p'):
            description+= p.text +'\n\n'
    
        return description 

    def search_name_collection(self): 
        name_coollection = self.bs.select('h1')[0].text.replace('Керамическая плитка', '')
        return name_coollection 

    def search_vendor(self):  
        for attr in self.search_atribyte(): 
            if "Производитель: " in attr:
                return attr.split(': ')[1]

    def create_info_post(self): 
        s = '''\

Коллекция {name_collection} от производителя {vendor}  <br><br>

'''.format(name_collection=self.search_name_collection(), vendor=self.search_vendor())

        for attr in self.search_atribyte():   
            s+= '👉' + attr + '<br>'; 



        s +='''

Купить можно у нас на сайте ➤ Дом Керамики {url} <br><br>

📖{description} <br><br>

#домкерамики #домкерамикивладимир <br><br>

👉У нас в магазине Дом Керамики лучший выбор керамической плитки, керамогранита и мозайки по адресу 📍 адрес - Почаевский овраг дом 1 г. Владимир <br><br>

По всем вопросам звоните в магазин на рабочий телефон 📞 +7 4922 77 82 82 <br> <br>

Режим работы магазина <br><br>

⏰Пн-Суб 09.00-19.00<br>
⏰Вс 09.00 - 17.00.<br>


Лучшая плитка и сантехника тут 👉 https://www.dkv33.ru/<br>
        
'''.format(url = self.url, description= self.search_description() )


        return s 