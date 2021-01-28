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

for i in range(1, 9):
    url = 'https://hom-beta-dados.fortaleza.ce.gov.br/dataset?page={}'.format(i)
    #url = 'https://hom-beta-dados.fortaleza.ce.gov.br/dataset'
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    dados = bs_obj.find_all('p', class_='mb-1')
    link_inicial = url.split('/dataset')
    print("=================================")
    for i in dados:
        teste =i.find_next() 
        complemento = teste['href'].split('/dataset')
        link = url + "/edit" + complemento[1]
        #print(link)
        if(complemento[1] != '/sie-sistema-de-informacoes-educacionais'):
            print("OK")
            driver.get(link)

            dados =driver.find_element_by_link_text('Excluir')
            #print(dados.get_attribute('href'))
            driver.get(dados.get_attribute('href'))
            driver.find_element_by_class_name('btn.btn-primary').click()
        else:
            print("Nao")
        #break
    #apagar organizacao
    #https://hom-beta-dados.fortaleza.ce.gov.br/organization/edit/sefin
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")