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


url = 'https://hom-beta-dados.fortaleza.ce.gov.br/organization'
html = requests.get(url)

bs_obj = BeautifulSoup(html.text, 'html.parser')
dados = bs_obj.find_all('a', class_='text-blue')
print("=================================")
for i in dados:
    # teste =i.find_next() 
    complemento = i['href'].split('/organization')
    link = url + "/edit" + complemento[1]
    #print(i['href'])
    print(link)



    if(complemento[1] != '/citinova-fundacao-de-ciencia-e-tecnologia-de-fortaleza'):
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