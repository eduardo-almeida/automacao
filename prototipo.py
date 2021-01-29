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
        novo = 'https://hom-beta-dados.fortaleza.ce.gov.br/dataset/new'
        driver.get(novo)
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
        #Preenchendo pagina 1
        driver.implicitly_wait(10)

        #Organização
        driver.find_element_by_id('select2-chosen-3').click()
        organizacao = driver.find_element_by_id('s2id_autogen3_search')
        organizacao.send_keys(nome_organizacao)
        #Clicar Enter
        organizacao.send_keys(u'\ue007')    

        #Visibilidade
        visibilidade = Select(driver.find_element_by_id('field-private'))
        visibilidade.select_by_visible_text("Pública")

        #Titulo e Texto
        driver.find_element_by_id('field-title').send_keys(titulo+" rpg")
        driver.find_element_by_id('field-notes').send_keys(texto) 

        #Etiqueta
        etiqueta = []
        try:
            etiquetas = bs_obj.find('ul', class_='tag-list well').find_all('a')
            for i in etiquetas:    
                etiqueta.append(i.text.strip())
            etiqueta = get_unique_values(etiqueta)

            for i in etiqueta:    
                    driver.find_element_by_id('s2id_autogen1').send_keys(i)
                    driver.find_element_by_id('select2-drop').click()
        except:
            #Só para tirar a excessao
            a = 1

        #Passar Página
        driver.find_element_by_class_name('btn-primary').click()

        #Preenchendo pagina 2    
        for i in dados:         
            driver.find_element_by_link_text('Link').click()
            link = i.find('a', class_='resource-url-analytics')['href']
            if(link.find("://prod.") >= 0):
                links = link.split('://prod.')
                link = "https://"+links[1]
            driver.find_element_by_id('field-image-url').send_keys(link)  
            nome = i.find('a', class_='heading')['title']
            driver.find_element_by_id('field-name').send_keys("") 
            driver.find_element_by_id('field-name').clear()
            driver.find_element_by_id('field-name').send_keys(nome)  
            descricao = i.find('p', class_='description') 
            driver.find_element_by_id('field-description').send_keys(descricao.text.strip())  

            #Novos dados
            if(dados[-1] == i):
                #print("fim")
                driver.find_element(By.XPATH, '//button[text()="Finalizar"]').click()
                print("Ok: "+titulo)
            else:
                #print("outro")
                driver.find_element(By.XPATH, '//button[text()="Salvar & adicionar outro"]').click()
    except:
        print("!!!!Erro!!!: " + titulo)
        
        

def logar():
    driver.find_element_by_name('login').send_keys("adm-ckan")
    driver.find_element_by_name('password').send_keys("1qaz#EDC")
    driver.find_element_by_class_name('btn-primary').click()
    
if __name__ == '__main__':
    url = 'https://hom-beta-dados.fortaleza.ce.gov.br/user/logged_in'
    driver = webdriver.Chrome(executable_path="./chromedriver")
    #Esperar 10 segundos
    driver.implicitly_wait(10)
    driver.get(url)
  
    logar()
    df = pd.DataFrame(columns=('titulo', 'texto'))

    
    #15 Páginas
    for i in range(1, 16):
        url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset?page={}'.format(i)
        get_url(url)

    
    # Licensa?


