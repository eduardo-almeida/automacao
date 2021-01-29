import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def get_unique_values(numbers):

    list_of_unique_numbers = []

    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

def get_url(url):
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    dados = bs_obj.find_all('div', class_='dataset-content')
    link_inicial = url.split('/dataset')

    for i in dados:
        link = link_inicial[0] + i.find('a')['href']
        titulo = i.find('a').text
        texto = ""
        if(i.find('div') != None):
            texto = i.find('div').text
        get_dados(link)
        
        #teste
        #break

def get_dados(url):
    try:
        html = requests.get(url)

        bs_obj = BeautifulSoup(html.text, 'html.parser')
        nome_organizacao = bs_obj.find('section', class_='module-content').find('h1').text.strip()
        dados = bs_obj.find_all('li', class_='resource-item')
        titulo = bs_obj.find('div', class_='module-content').find('h1').text.strip()
        texto = bs_obj.find('div', class_='module-content').find('p').text.strip()
        

        #Etiqueta
        etiqueta = []
        try:
            etiquetas = bs_obj.find('ul', class_='tag-list well').find_all('a')
            for i in etiquetas:    
                etiqueta.append(i.text.strip())
            etiqueta = get_unique_values(etiqueta)
            print(etiqueta)    
            
        except:
            #So para tirar a excessao
            a = 1

       
    except:
        print("!!!!Erro!!!: " + titulo)
        
        

def logar():
    driver.find_element_by_name('login').send_keys("adm-ckan")
    driver.find_element_by_name('password').send_keys("1qaz#EDC")
    driver.find_element_by_class_name('btn-primary').click()
    
if __name__ == '__main__':
    

    #url = 'https://hom-beta-dados.fortaleza.ce.gov.br/dataset/new'
    #driver.get(url)
    
    #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset'

    #15 Paginas
    for i in range(12, 13):
        url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset?page={}'.format(i)
        get_url(url)

    # url = 'https://hom-beta-dados.fortaleza.ce.gov.br/dataset/new'
    # driver.get(url)
    # url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset/realizacoes-da-prefeitura-municipal-entre-2012-2016'
    # #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset/dados-de-onibus-11-03-2015'
    
    # get_dados(url, 'a', 'b')


    #Ultimo arquivo
    #https://dados.fortaleza.ce.gov.br/catalogo/dataset/documentacao-de-controle-sim-ref-09-2015
    #pag 8
    #    Balancetes (SIM) Ref. 08-2014 


