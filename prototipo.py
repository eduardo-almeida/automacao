import requests
from bs4 import BeautifulSoup
import pandas as pd

def teste():
    url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset'
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    #bs_obj = BeautifulSoup(html.text, 'lxml')
    a = bs_obj.find('ul', class_='dataset-list unstyled')
    b = bs_obj.find_all('h3', class_='dataset-heading')

    print("=================================================")
    print(type(bs_obj))    
    print(type(a))
    print(b[0].find('a', href=True))
    for i in b:
        #x['href'] = j.find('a', href=True)        
        print(i.find('a')['href'])
     

def teste_old():
    url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset'
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    #bs_obj = BeautifulSoup(html.text, 'lxml')
    a = bs_obj.find_all('ul', class_='dataset-list unstyled')
    b = bs_obj.find_all('h3', class_='dataset-heading')
    
    links = [ i['href'] for i in a[0].find_all('a', href=True)]
    #b = a[0].find_all('a', href=True)
    #links = [ i['href'] for i in a[0].find_all('a', href=True)]
    #print(b)
    #print(type(links))
    #for link in a[0].find_all('h3', class_='dataset-heading'):
    for link in links:
        print("======================================================================")
        print(link)
        #print(link['href'])
    #dataset-heading
    #df = pd.DataFrame()
    #print(df)
    

if __name__ == '__main__':
    teste()
