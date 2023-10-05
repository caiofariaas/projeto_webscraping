import pandas as pd
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# Seleciona o chrome como navegador padrão para abrir 
driver = webdriver.Chrome()

# URL da pagina que deseja recolher os dados

driver.get("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/")

# Caminho referente a tabela com os dados desejados

elemento = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[1]/div[2]/div[1]/div[2]/table')

# transforma a string "PATH" em um objeto HTML, abrindo a possibilidade de acessar os atributos desse elemento.

table = BeautifulSoup(elemento.get_attribute('outerHTML'), 'html.parser')

table_headers = []

# O looping a seguir procura todos as tag's "th" presentes na tabela criada acima, depois adiciona o mesmo em uma lista "table_headers".

for th in table.find_all('th'):
    table_headers.append(th.text)


table_data =[]

# Aqui ele tem a mesma função, porem, esta buscando a tag "tr" que vem de table row
# Dentro de uma 'tr' existem varias tag's 'td' que são os elementos presentes nessa linhas

for row in table.find_all('tr'):
    sleep(0.5)
    colunas = row.find_all('td')
    output_row = []

    # aqui é aonde ele adiciona os elementos 'td' a uma lista, criando uma linha completa nessa lista e assim vai acontecendo sucessivamente com o loop.

    for coluna in colunas:
        output_row.append(coluna.text)

    # Ao encontrar a linha completa ele apenas adiciona a uma lista de conteúdo "final".

    table_data.append(output_row)    

# Cria um data frame com esses dados e os transforma em uma tabela

data_frame = pd.DataFrame(table_data, columns=table_headers)

# Manda essa tabela para um arquivo EXCEL

data_frame.to("arquivo.xlsx")

print("Tabela criada com sucesso!")

#encerrar o codigo

driver.quit()
