import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def ler_csv(arquivo):
    df = pd.read_csv(arquivo, delimiter=',')
    print(df)

def copiar_arquivo(url):
    for i in range(1,2):
        get_url(url+str(i))

def get_url(url):
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    dados = bs_obj.find_all('div', class_='dataset-content')

    for i in dados:     
        #print("==========================================================")
        link_inicial = url.split('/dataset')
        #print(link_inicial[0] + i.find('a')['href'])
        link = link_inicial[0] + i.find('a')['href']
        #print(i.find('a').text)
        titulo = i.find('a').text
        texto = ""
        if(i.find('div') != None):
            #print(i.find('div').text)
            texto = i.find('div').text
        get_arquivos(link, titulo, texto)
        break
    
def get_arquivos(url, titulo, texto):
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    dados = bs_obj.find_all('li', class_='resource-item')
    #print(pasta)   

    for i in dados:    
        print("=========================================================")
        #print(i)
        target = i.find('a', class_='resource-url-analytics')
        print(target['href'])
        title = i.find('a', class_='heading')
        titles = i.find('span', class_='format-label')
        #clear_button = i.find_element_by_class_name("heading")
        print("!!!!!!!!!!!!!!!!!!!!!!!!")
        print(titles.text)
        print(title.text.strip().replace(titles.text,""))
        print(title.text.strip())
        content = i.find('p', class_='description')        
        print(content.text.strip())

   
    

if __name__ == '__main__':

    #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset'
    #get_url(url)
    #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset?page={}'
    url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset/dados-de-onibus-11-03-2015'
    get_arquivos(url, 'a', 'b')
    
    #teste(url)
    # for i in range(1,2):
    #     get_url(url.format(i))

    #arquivo = "testando.csv"
    #ler_csv(arquivo)
    #url = 'https://dados.fortaleza.ce.gov.br/dataset/f5db028c-002c-4f3d-96b0-ee835a79bcfa/resource/611c97d1-f599-4d7b-9a5f-47d45b287597/download/rededeatencaoecuidadosdefortaleza.pdf'
    #baixar_arquivo(url, 'test.pdf')

    #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset/http-www-fortaleza-ce-gov-br-sites-default-files-rede-de-atencao-e-cuidados-de-fortaleza-pdf'
    #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset/limite-municipal-de-fortaleza'
    #get_arquivos(url, "asdf", "texto")