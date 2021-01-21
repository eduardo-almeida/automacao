import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def ler_csv(arquivo):
    df = pd.read_csv(arquivo, delimiter=',')
    print(df)

def copiar_arquivo(url):
    for i in range(1,2):
        get_url(url+str(i))

def get_url(url):
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    dados = bs_obj.find_all('div', class_='dataset-content')

    for i in dados:     
        #print("==========================================================")
        link_inicial = url.split('/dataset')
        #print(link_inicial[0] + i.find('a')['href'])
        link = link_inicial[0] + i.find('a')['href']
        #print(i.find('a').text)
        titulo = i.find('a').text
        texto = ""
        if(i.find('div') != None):
            #print(i.find('div').text)
            texto = i.find('div').text
        get_arquivos(link, titulo, texto)
    

def get_url_old(url):
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    dados = bs_obj.find_all('h3', class_='dataset-heading')

    for i in dados:     
        print("==========================================================")
        #print(i.find('a')['href'])
        print(i.find_next().text)
        print("@@@   "+i.find_next().find_next().text + " #####")

def get_arquivos(url, titulo, texto):
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    dados = bs_obj.find_all('a', class_='resource-url-analytics')
    pasta = "teste/" + titulo + "/"
    #print(pasta)
    df = pd.DataFrame(columns=('titulo', 'texto', 'arquivo'))
    try:
        os.makedirs(pasta)
    except FileExistsError as e:
        print(f'Pasta {pasta} já existe')

    for i in dados:    
        arquivo = i['href'].split('download/')
        
        endereco = pasta + arquivo[1]
        url = i['href']
        extensao = arquivo[1].split('.')
        print("=========================================================")
        print(url)
        try:
            baixar_arquivo(url, endereco)
            new_row = {'titulo':titulo, 'texto':texto, 'arquivo':arquivo[1]}
            #df = pd.concat([df, new_row])
            df = df.append(new_row, ignore_index=True)
            #df.to_csv("testando.csv")
            #df.close()

            # with open('nome.txt', 'a') as f:
            #     writer = csv.writer(f)
            #     writer.writerow(new_row)
            #     f.close()

        except:
            print("Arquivo não foi encontrado")

    df.to_csv('testando.csv', mode='a', header=False)
    


def baixar_arquivo(url, endereco):
    resposta = requests.get(url)
    with open(endereco, 'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)
    



def teste_old():
    url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset'
    html = requests.get(url)

    bs_obj = BeautifulSoup(html.text, 'html.parser')
    #bs_obj = BeautifulSoup(html.text, 'lxml')
    a = bs_obj.find_all('ul', class_='dataset-list unstyled')
    b = bs_obj.find_all('h3', class_='dataset-heading')
    
    links = [ i['href'] for i in a[0].find_all('a', href=True)]
    #b = a[0].find_all('a', href=True)
    #links = [ i['href'] for i in a[0].find_all('a', href=True)]
    #print(b)
    #print(type(links))
    #for link in a[0].find_all('h3', class_='dataset-heading'):
    for link in links:
        print("======================================================================")
        print(link)
        #print(link['href'])
    #dataset-heading
    #df = pd.DataFrame()
    #print(df)
    

if __name__ == '__main__':

    #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset'
    url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset?page={}'
    #get_url(url)

    for i in range(1,2):
        get_url(url.format(i))

    #arquivo = "testando.csv"
    #ler_csv(arquivo)
    #url = 'https://dados.fortaleza.ce.gov.br/dataset/f5db028c-002c-4f3d-96b0-ee835a79bcfa/resource/611c97d1-f599-4d7b-9a5f-47d45b287597/download/rededeatencaoecuidadosdefortaleza.pdf'
    #baixar_arquivo(url, 'test.pdf')

    #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset/http-www-fortaleza-ce-gov-br-sites-default-files-rede-de-atencao-e-cuidados-de-fortaleza-pdf'
    #url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset/limite-municipal-de-fortaleza'
    #get_arquivos(url, "asdf", "texto")