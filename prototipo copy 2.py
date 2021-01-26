import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select


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
        #break

    
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


def logar():
    driver.find_element_by_name('login').send_keys("adm-ckan")
    driver.find_element_by_name('password').send_keys("1qaz#EDC")
    driver.find_element_by_class_name('btn-primary').click()
    
if __name__ == '__main__':

    url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset'
    #get_url(url)
    
    #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset/dados-de-onibus-11-03-2015'
    #get_dados(url, 'a', 'b')
    url = 'https://hom-beta-dados.fortaleza.ce.gov.br/user/logged_in'
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get(url)
  
    logar()

    url = 'https://hom-beta-dados.fortaleza.ce.gov.br/dataset/new'
    driver.get(url)
    
    #Preenchendo pagina 1
    organizacao = Select(driver.find_element_by_id('field-organizations'))
    organizacao.select_by_visible_text('Etufor')
            

    visibilidade = Select(driver.find_element_by_id('field-private'))
    visibilidade.select_by_visible_text("Pública")


    driver.find_element_by_id('field-title').send_keys("Titulo")
    driver.find_element_by_id('field-notes').send_keys("Descricao")   
    

    valor = ["um", "dois"]
    for i in valor:
        driver.find_element_by_id('s2id_autogen1').send_keys(i)
        driver.find_element_by_id('select2-drop').click()
    
    driver.find_element_by_class_name('btn-primary').click()

