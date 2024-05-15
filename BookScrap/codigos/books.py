"""
Nós queremos acessar a pagina, pegar todos os links dos livros,
acessar cada link em busca da quantidade em estoque, guardar tudo em listas
e por fim gerar um dataframe

"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://books.toscrape.com/index.html"

driver.get(url)
time.sleep(2)

links = driver.find_elements(By.TAG_NAME, "a")
print(links)
print(len(links))

# os livros começam no 54 e terminam no 92 de 2 em 2

x = driver.find_elements(By.TAG_NAME, "a")[54].text
print(x)

y = driver.find_elements(By.TAG_NAME, "a")[54].get_attribute("title")
print(y)

print(driver.find_elements(By.TAG_NAME,"a")[54:94:2])

elementostitulo = driver.find_elements(By.TAG_NAME,"a")[54:94:2]

listatitulos = [title.get_attribute("title") for title in elementostitulo]
print(listatitulos)

elementostitulo[1].click()
time.sleep(2)
stok = driver.find_element(By.CLASS_NAME, "instock").text
time.sleep(2)
print(stok)
estoque = int(stok.replace("In stock (", "").replace(" available)",""))
print(estoque)
driver.back()

listaestoque = []

for titulo in elementostitulo:
    titulo.click()
    time.sleep(1)
    qtd = int(driver.find_element(By.CLASS_NAME, "instock").text.replace("In stock (", "").replace(" available)",""))
    listaestoque.append(qtd)
    driver.back()
    time.sleep(1)

print(listaestoque)

data = {"Titulo": listatitulos, "Estoque": listaestoque}
print(pd.DataFrame(data))
dados = pd.DataFrame(data)
dados.to_excel("dados.xlsx")