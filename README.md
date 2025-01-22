# Projeto de Python com Scraping de Dados

Este projeto tem como objetivo praticar todos os fundamentos de Python, incluindo web scraping, análise de dados e manipulação de arquivos CSV. Utilizei as bibliotecas beautifulsoup e selenium para capturar dados de livros do site "Books to Scrape".

## Descrição do Projeto

1. Aprendizado de Web Scraping:
    * Aprender a realizar web scraping em websites utilizando as bibliotecas beautifulsoup e selenium.

2. Captura de Dados:
    * Construir um script em Python que realiza a captura dos dados de todos os livros das categorias de livros disponíveis no site.

3. Análise dos Dados:
    * Calcular o preço médio dos livros de cada categoria.
    * Calcular a quantidade de estrelas médias que os livros dessa categoria possuem.
    * Determinar a quantidade total de livros na categoria.

4. Salvamento dos Dados:
    * Salvar todas as informações coletadas em arquivos CSV (um para cada categoria) de forma estruturada, onde cada linha representa um livro e as colunas contêm informações como: ID, Nome (Name), Preço (Price) e Avaliação (Star Rating).

## Tecnologias Utilizadas

Exemplo:
* [Git](https://git-scm.com/downloads)
* [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
* [Python](https://www.python.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Selenium](https://www.selenium.dev/pt-br/documentation/)

## Dependências e Versões Necessárias

* Git - Versão: 2.47.1.windows.2
* Python - Versão: 3.12.5
* Visual Studio Code - Versão 1.96.3

## Como rodar o projeto ✅

Para rodar este projeto, você precisará ter o Git, Python e o VS Code instalados em sua máquina (vale salientar que utilizei o Git Bash como terminal).

## Configuração do Ambiente no VS Code

1. Extensão Python: Instale a extensão Python para o VS Code para fornecer suporte a recursos como linting, debugging e Jupyter Notebooks.
    * Vá para a aba de Extensões no VS Code (Ctrl+Shift+X ou Cmd+Shift+X no macOS).
    * Procure por "Python" e instale a extensão fornecida pela Microsoft.

2. Instale as bibliotecas necessárias usando o pip:

```
pip install beautifulsoup4 selenium
```

## Instruções de uso (Git Bash)
1. Clone o repositório:
    * Abra o Git Bash e execute o comando
```
git clone https://github.com/muller-pereira/projeto_scraping.git
```
2. Navegue até o diretório do projeto:
    * Ainda no Git Bash, navegue até o diretório do projeto:
```
cd projeto_scraping
```
3. Abra o projeto no VS Code:
    * Abra o Visual Studio Code no diretório do projeto:
```
code .
```
4. Execute o script de scraping no terminal do VS Code:
```
python app.py
```

## Estrutura do Projeto
* app.py: Script principal para realizar o web scraping e capturar os dados dos livros.
* requirements.txt: Lista de bibliotecas necessárias para rodar o projeto.
* data/: Diretório onde os arquivos CSV gerados serão salvos.

## Resultados

* Realiza web scraping de uma categoria de livros do site "Books to Scrape".

* Calcula o preço médio dos livros na categoria.

* Calcula a quantidade de estrelas médias dos livros na categoria.

* Determina a quantidade total de livros na categoria.

Ex:

![Image](https://github.com/user-attachments/assets/7267e8c1-069b-405a-9a7c-f83fd5f176da)

* Exibe as categorias com maior e menor quantidade de livros, adotando como critério de desempate a ordem alfabética.

![Image](https://github.com/user-attachments/assets/64f7aa03-02fa-4ba6-8e6b-2fd33e64a451)

* Exibe o livro mais caro e o mais barato

![Image](https://github.com/user-attachments/assets/fe430739-3efc-417f-b809-a3a5b711781a)

* Exibe os livros com maior e menor quantidade de estrelas, também adotando como critério de desempate a ordem affabética.

![Image](https://github.com/user-attachments/assets/70673dcd-d816-4b40-857c-e6f033cdc337)

* Salva os dados coletados em um arquivo CSV.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e correções.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](https://github.com/muller-pereira/projeto_scraping/blob/main/LICENSE) para mais detalhes.

