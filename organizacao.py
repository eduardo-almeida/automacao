import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def logar():
    driver.find_element_by_name('login').send_keys("adm-ckan")
    driver.find_element_by_name('password').send_keys("1qaz#EDC")
    driver.find_element_by_class_name('btn-primary').click()
    

url = 'https://hom-beta-dados.fortaleza.ce.gov.br/user/logged_in'
driver = webdriver.Chrome(executable_path="./chromedriver")
#Esperar 10 segundos
driver.implicitly_wait(10)
driver.get(url)

logar()



print("=================================")
for j in range(1,3):
    url = 'https://dados.fortaleza.ce.gov.br/catalogo/organization?page={}'.format(j)
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    dados = bs_obj.find_all('li', class_='media-item')
    for i in dados:
        nome = i.find('h3').text.strip()
        if(nome != 'Etufor' and nome != 'SEFIN' and nome != 'Citinova' and nome != 'AMC' and nome != 'CEPS'):
            url = 'https://hom-beta-dados.fortaleza.ce.gov.br/organization/new'
            driver.get(url)
            print(nome)
            descricao = i.find('p').text.strip()
            driver.find_element_by_id('field-name').send_keys(nome) 
            driver.find_element_by_id('field-description').send_keys(descricao) 
            driver.find_element_by_class_name('btn-primary').click()
        
        
        else:
            print("Não")

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")