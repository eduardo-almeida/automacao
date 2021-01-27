import requests
from bs4 import BeautifulSoup

print("=================================")
for j in range(1,3):
    url = 'https://dados.fortaleza.ce.gov.br/catalogo/organization?page={}'.format(j)
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    dados = bs_obj.find_all('li', class_='media-item')
    for i in dados:
        nome = i.find('h3').text.strip()
        descricao = i.find('p').text.strip()
        print(nome)
        print(descricao)
        
        if(nome != 'Etufor' and nome != 'SEFIN'and nome != 'Citinova'):
            print("OK")
        else:
            print("Não")

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")