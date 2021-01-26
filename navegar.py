from selenium import webdriver


url = 'https://dados.fortaleza.ce.gov.br/catalogo/dataset'
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(url)