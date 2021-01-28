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
        link = link_inicial[0] + i.find('a')['href']
        titulo = i.find('a').text
        texto = ""
        if(i.find('div') != None):
            texto = i.find('div').text
            #Renomear para Polícia
            #Se ja existir renomear        
        
        get_dados(link)
        
        #teste
        #break

def get_dados(url):
    try:
        html = requests.get(url)

        bs_obj = BeautifulSoup(html.text, 'html.parser')
        nome_organizacao = bs_obj.find('section', class_='module-content').find('h1').text
        dados = bs_obj.find_all('li', class_='resource-item')
        titulo = bs_obj.find('div', class_='module-content').find('h1')
        texto = bs_obj.find('div', class_='module-content').find('p')
        print("===============================================================")
        print(titulo.text.strip())
        print(texto.text.strip())
        

        #Etiqueta
        etiqueta = []
        try:
            etiquetas = bs_obj.find('ul', class_='tag-list well').find_all('a')
            for i in etiquetas:     
                #etiqueta = i['href']   
                etiqueta.append(i.text) 
           
        except:
            print("Não tem etiqueta")

        #Preenchendo pagina 2    
        #Preencher Dados
        for i in dados:         
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            link = i.find('a', class_='resource-url-analytics')
            print("link: "+link['href'])
            nome = i.find('a', class_='heading')['title']
            print("nome: "+nome)
            extensao = i.find('span', class_='format-label')
            print("extensao: "+extensao.text.strip())
            descricao = i.find('p', class_='description') 
            print("descricao: "+descricao.text.strip())
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    except:
        print("Erro: " + titulo)
        
  
    
if __name__ == '__main__':
  
    for i in range(1, 16):
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

