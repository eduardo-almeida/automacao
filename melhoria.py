import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def get_url(url):
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    dados = bs_obj.find_all('div', class_='dataset-content')
    link_inicial = url.split('/dataset')

    for i in dados:
        global vai
        link = link_inicial[0] + i.find('a')['href']
        titulo = i.find('a').text
        texto = ""
        #novo = 'https://hom-beta-dados.fortaleza.ce.gov.br/dataset/new'
        #driver.get(novo)
        if(i.find('div') != None):
            texto = i.find('div').text
            #Renomear para Polícia
            #Se ja existir renomear
        
        vai = True
            
        if(vai):
            print("=====================================================")
            print("Ok: " + titulo)
            print(link)
            get_dados(link, titulo, texto)
        else:
            print("Não: " + titulo)
        #teste
        #break

def get_dados(url, titulo, texto):
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    nome_organizacao = bs_obj.find('section', class_='module-content').find('h1').text
    dados = bs_obj.find_all('li', class_='resource-item')

    #Preencher Dados
    for i in dados:         
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        link = i.find('a', class_='resource-url-analytics')
        nome = i.find('a', class_='heading')
        extensao = i.find('a')['title']
        descricao = i.find('p', class_='description')  
        print("extensao: "+extensao)
        print("descricao: "+descricao.text.strip())
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        

def logar():
    driver.find_element_by_name('login').send_keys("adm-ckan")
    driver.find_element_by_name('password').send_keys("1qaz#EDC")
    driver.find_element_by_class_name('btn-primary').click()
    
if __name__ == '__main__':
    # url = 'https://hom-beta-dados.fortaleza.ce.gov.br/user/logged_in'
    # driver = webdriver.Chrome(executable_path="./chromedriver")
    # #Esperar 10 segundos
    # driver.implicitly_wait(10)
    # driver.get(url)
  
    # logar()
    # df = pd.DataFrame(columns=('titulo', 'texto'))

    #url = 'https://hom-beta-dados.fortaleza.ce.gov.br/dataset/new'
    #driver.get(url)
    
    #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset'


    vai = False
    for i in range(2, 3):
        url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset?page={}'.format(i)
        get_url(url)

    # url = 'https://hom-beta-dados.fortaleza.ce.gov.br/dataset/new'
    # driver.get(url)
    # url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset/realizacoes-da-prefeitura-municipal-entre-2012-2016'
    # #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset/dados-de-onibus-11-03-2015'
    
    # get_dados(url, 'a', 'b')


    #Ultimo arquivo
    #https://dados.fortaleza.ce.gov.br/catalogo/dataset/documentacao-de-controle-sim-ref-09-2015

    #Olhar com calma
    #Rede de Atenção e Cuidado de Fortaleza
    #puxar dados 
    #Documentação de Controle (SIM) - Ref. 04-2014
