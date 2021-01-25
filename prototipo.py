import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


def get_url(url):
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    dados = bs_obj.find_all('div', class_='dataset-content')

    for i in dados:
        link_inicial = url.split('/dataset')
        link = link_inicial[0] + i.find('a')['href']
        titulo = i.find('a').text
        texto = ""
        if(i.find('div') != None):
            texto = i.find('div').text
        get_dados(link, titulo, texto)
        #teste

    
def get_dados(url, titulo, texto):
#def get_dados(url):
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    dados = bs_obj.find_all('a', class_='resource-url-analytics')

    organizacao = bs_obj.find('section', class_='module-content').find('h1').text
    print("===========================================")
    print(organizacao)

    etiqueta = []
    try:
        etiquetas = bs_obj.find('ul', class_='tag-list well').find_all('a')
        for i in etiquetas:     
            #etiqueta = i['href']   
            etiqueta.append(i.text) 

        print(etiqueta)
    except:
        print("Não tem etiqueta")
    print("=========== links =============")
    print(len(dados))
    for i in dados:            
        url = i['href']
        print(url)
        if(dados[-1] == i):
            print("fim")
    print("============================================")

    
if __name__ == '__main__':

    #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset'
    #get_url(url)
    url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset/dados-de-onibus-11-03-2015'
    get_dados(url, 'a', 'b')
    