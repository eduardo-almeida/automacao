import requests
from bs4 import BeautifulSoup

def baixar_arquivo(url, endereco):
    resposta = requests.get(url)
    with open(endereco, 'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)



if __name__ == '__main__':
    url = 'https://math.mit.edu/classes/18.745/Notes/Lecture_1_Notes.pdf'
    baixar_arquivo(url, 'test.pdf')