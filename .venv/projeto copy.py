import os
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Inicializar o navegador
driver = webdriver.Chrome()
driver.get('https://books.toscrape.com/index.html')
driver.maximize_window()
time.sleep(3)

# Definir o caminho da pasta do ambiente virtual (venv)
caminho_venv = os.path.join(os.getcwd(), '.venv')
if not os.path.exists(caminho_venv):
    os.makedirs(caminho_venv)

# Diretório de saída no venv
output_dir = os.path.join(caminho_venv, 'data')
os.makedirs(output_dir, exist_ok=True)

# Encontrar todas as categorias
site = BeautifulSoup(driver.page_source, 'html.parser')
categorias = site.find('ul', class_='nav-list').find('ul').find_all('a')

# Dicionários para armazenar informações
categoria_stats = {}
livros_global = []

# Iterar sobre cada categoria
for categoria in categorias:
    nome_categoria = categoria.text.strip().replace(' ', '_')
    link_categoria = 'https://books.toscrape.com/' + categoria['href']
    
    driver.get(link_categoria)
    time.sleep(3)
    
    # Lista para armazenar os dados temporariamente
    livros = []
    id = 1
    total_preco = 0
    total_estrelas = 0
    proxima_pagina_existente = True
    
    while proxima_pagina_existente:
        site = BeautifulSoup(driver.page_source, 'html.parser')
        todos_elementos = site.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
        
        for elemento in todos_elementos:
            name = elemento.find('a', title=True)['title']
            price = float(elemento.find('p', class_='price_color').text[1:])
            
            star_mapping = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
            star_rating = star_mapping.get(elemento.p['class'][1], 0)
            
            total_preco += price
            total_estrelas += star_rating
            
            livros.append([id, name, price, star_rating])
            livros_global.append({'categoria': nome_categoria, 'name': name, 'price': price, 'star_rating': star_rating})
            id += 1
        
        # Verificar próxima página
        try:
            next_pag = driver.find_element(By.XPATH, "//li[@class='next']/a")
            next_pag.click()
            time.sleep(3)
        except NoSuchElementException:
            proxima_pagina_existente = False
    
    # Calcular média e outras estatísticas
    numero_livros = len(livros)
    preco_medio = total_preco / numero_livros if numero_livros > 0 else 0
    media_estrelas = total_estrelas / numero_livros if numero_livros > 0 else 0
    
    # Armazenar estatísticas
    categoria_stats[nome_categoria] = {
        'numero_livros': numero_livros,
        'preco_medio': preco_medio,
        'media_estrelas': media_estrelas,
    }
    
    # Gravar no CSV
    csv_path = os.path.join(output_dir, f'{nome_categoria}.csv')
    with open(csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['id', 'Name', 'Price', 'Star Rating'])
        csv_writer.writerows(livros)
    
    print(f'Categoria: {nome_categoria}')
    print(f'Quantidade de livros: {numero_livros}')
    print(f'Preço médio da Categoria: {preco_medio:.2f}')
    print(f'Média de estrelas da Categoria: {media_estrelas:.2f}')
    print('-' * 50)

# Finalizar navegador
driver.quit()

# Identificar categorias com maior/menor número de livros
max_livros = max(categoria_stats.values(), key=lambda x: x['numero_livros'])['numero_livros']
min_livros = min(categoria_stats.values(), key=lambda x: x['numero_livros'])['numero_livros']

categorias_mais_livros = [cat for cat, stats in categoria_stats.items() if stats['numero_livros'] == max_livros]
categorias_menos_livros = [cat for cat, stats in categoria_stats.items() if stats['numero_livros'] == min_livros]

print(f"Categoria com o maior número de livros: {sorted(categorias_mais_livros)[0]} ({max_livros} livros)")
print(f"Categoria com o menor número de livros: {sorted(categorias_menos_livros)[0]} ({min_livros} livros)")

# Identificar livros com maior/menor preço
max_preco = max(livros_global, key=lambda x: x['price'])['price']
min_preco = min(livros_global, key=lambda x: x['price'])['price']

livros_mais_caro = [livro for livro in livros_global if livro['price'] == max_preco]
livros_mais_barato = [livro for livro in livros_global if livro['price'] == min_preco]

print(f"Livro mais caro: {sorted(livros_mais_caro, key=lambda x: x['name'])[0]['name']} ({max_preco})")
print(f"Livro mais barato: {sorted(livros_mais_barato, key=lambda x: x['name'])[0]['name']} ({min_preco})")

# Identificar livros com maior/menor estrelas
max_estrelas = max(livros_global, key=lambda x: x['star_rating'])['star_rating']
min_estrelas = min(livros_global, key=lambda x: x['star_rating'])['star_rating']

livros_mais_estrelas = [livro for livro in livros_global if livro['star_rating'] == max_estrelas]
livros_menos_estrelas = [livro for livro in livros_global if livro['star_rating'] == min_estrelas]

print(f"Livro com maior número de estrelas: {sorted(livros_mais_estrelas, key=lambda x: x['name'])[0]['name']} ({max_estrelas})")
print(f"Livro com menor número de estrelas: {sorted(livros_menos_estrelas, key=lambda x: x['name'])[0]['name']} ({min_estrelas})")



