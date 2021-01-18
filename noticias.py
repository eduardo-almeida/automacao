import requests
from bs4 import BeautifulSoup


url = 'https://fametro.edu.br/faq-items/portal-digital-da-fametro/?u=noticias&c=197&cam'
req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

classe = 'mk-similiar-title'
lista_noticias = soup.find_all('a', class_=classe)

print(lista_noticias)
