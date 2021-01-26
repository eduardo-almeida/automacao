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

    for i in dados:
        link_inicial = url.split('/dataset')
        link = link_inicial[0] + i.find('a')['href']
        titulo = i.find('a').text
        texto = ""
        if(i.find('div') != None):
            texto = i.find('div').text
        get_dados(link, titulo, texto)
        #teste
        break

def get_dados(url, titulo, texto):
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    nome_organizacao = bs_obj.find('section', class_='module-content').find('h1').text
    dados = bs_obj.find_all('li', class_='resource-item')

    #Preenchendo pagina 1
    driver.implicitly_wait(10)
    #try:


    driver.find_element_by_id('select2-chosen-3').click()
    organizacao = driver.find_element_by_id('s2id_autogen3_search')
    organizacao.send_keys(nome_organizacao)
    organizacao.send_keys(u'\ue007')
    #driver.find_element_by_id('select2-chosen-3').click()
    #WebElement.sendKeys(Keys.RETURN)


    #organizacao = Select(driver.find_element_by_id('field-organizations'))
    #nome_organizacao = bs_obj.find('section', class_='module-content').find('h1').text
    #organizacao.select_by_visible_text(nome_organizacao)


    

    visibilidade = Select(driver.find_element_by_id('field-private'))
    visibilidade.select_by_visible_text("Pública")


    driver.find_element_by_id('field-title').send_keys(titulo + "testes")
    driver.find_element_by_id('field-notes').send_keys(texto) 

    etiqueta = []
    try:
        etiquetas = bs_obj.find('ul', class_='tag-list well').find_all('a')
        for i in etiquetas:     
            #etiqueta = i['href']   
            etiqueta.append(i.text) 
        for i in etiqueta:
            driver.find_element_by_id('s2id_autogen1').send_keys(i)
            driver.find_element_by_id('select2-drop').click()
    except:
        print("Não tem etiqueta")
    #except:
     #   print("Erro: ")

    driver.find_element_by_class_name('btn-primary').click()

    #Preenchendo pagina 2
    
#def temporario():   
    for i in dados:         
        driver.find_element_by_link_text('Link').click()
        link = i.find('a', class_='resource-url-analytics')
        driver.find_element_by_id('field-image-url').send_keys(link['href'])  
        nome = i.find('a', class_='heading')
        extensao = i.find('span', class_='format-label')
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(nome)
        driver.find_element_by_id('field-name').send_keys("") 
        driver.find_element_by_id('field-name').clear()
        driver.find_element_by_id('field-name').send_keys(nome.text.strip().replace(extensao.text,""))  
        descricao = i.find('p', class_='description')  
        driver.find_element_by_id('field-description').send_keys(descricao.text.strip())  


        if(dados[-1] == i):
            print("fim")
            driver.find_element(By.XPATH, '//button[text()="Finalizar"]').click()
        else:
            print("outro")
            driver.find_element(By.XPATH, '//button[text()="Salvar & adicionar outro"]').click()
        
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
    #driver.implicitly_wait(10)
    driver.get(url)
  
    logar()

    url = 'https://hom-beta-dados.fortaleza.ce.gov.br/dataset/new'
    driver.get(url)
    
    url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset'
    get_url(url)

    #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset/dados-de-onibus-11-03-2015'
    #get_dados(url, 'a', 'b')

    
    
            
    
    
    

      

    #driver.find_element_by_class_name('nome').click()
