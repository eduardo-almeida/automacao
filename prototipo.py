import requests
from bs4 import BeautifulSoup
import pandas as pd

def teste():
    url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset'
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    #bs_obj = BeautifulSoup(html.text, 'lxml')
    a = bs_obj.find_all('ul', class_='dataset-list unstyled')
    links = [ i['href'] for i in a[0].find_all('a', href=True)]
    for link in a[0]:
        print("======================================================================")
        print(link)
    #dataset-heading
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    df = pd.DataFrame()
    print(df)
    

if __name__ == '__main__':
    teste()
