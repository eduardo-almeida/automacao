import requests
from bs4 import BeautifulSoup


url = 'https://dados.fortaleza.ce.gov.br/catalogo/organization?page=1'
html = requests.get(url)

bs_obj = BeautifulSoup(html.text, 'html.parser')
dados = bs_obj.find_all('p', class_='mb-1')
for i in dados:
    print("=================================")
    teste =i.find_next() 
    complemento = teste['href'].split('/dataset')
    link = url + "/edit" + complemento[1]
    print(link)

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")