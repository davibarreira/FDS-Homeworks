# FDS-Homeworks
> Repositórios com Homeworks da matéria de Fundamentos de Data Science do Mestrado de Modelagem Matemática da FGV.

> hw1 - Contém o primeiro Homework.

## Homework 1
### Descrição
Este trabalho consistiu na criação de um aplicativo web para geração de
grafos de coautoria. No aplicativo, o usuário insere um nome, que então é
automaticamente buscado no Google Scholar, e em seguia é feito um scraping
para a coleta dos papers publicados e coautores respectivos.
Esses dados são armazenados em uma base de dados e utilizados para
gerar grafos interativos, implementado na biblioteca Altair
[https://altair-viz.github.io/index.html].


### Requerimentos
As dependências de python para este repositório estão no arquivo
**requeriments.txt**. É recomendado utilizar um ambiente virtual.
Para instalar os pacotes basta rodar:
```sh
pip install -r requirements.txt
```
Além disso, a biblioteca utilizada para realizar o webscraping foi
a _selenium_ com o **Firefox** como browser. Desta forma, é necessário
ter o browser instalado juntamente com o _geckodriver_.

### Estrutura do Repositório
*   app.py              - Contém o aplicativo web em Flask;
*   database_app.py     - Funções para criação e inserção dos dados na
database;
*   grafos.py           - Funções para geração dos grafos interativos;
*   scrape_scholar.py   - Função para realizar o scrape do Google Scholar;
*   forms.py            - Arquivo contendo form criado para receber nome
pesquisado;
*   scrape.ipynb        - Jupyter Notebook com exemplo de scraping do
Google Scholar;
*   templates/          - Pasta com arquivos de _html_ utilizados no
aplicativo.

### Running
Para rodar o aplicativo fazer:
```sh
python app.py
```
Assim, o aplicativo estará rodando no seu _http://localhost:8000/_.

### Instruções de uso
Na barra de pesquisa você deve inserir o nome do pesquisador que está procurando.
O aplicativo irá então buscar no Google Scholar pelo nome inserido, e irá retornar
o primeiro valor encontrado. Caso não seja encontrado o pesquisador ou algum outro erro ocorra,
uma mensagem irá aparecer na tela.


Quando o nome for encontrado, dois grafos interativos irão aparecer na tela.
O grafo da esquerda corresponde a uma rede de coautorias, onde os nós representam autores de papers,
e a aresta indica que publicaram algum artigo em conjunto. Enquanto o grafo da direito relaciona artigos
com autores em comum.


No grafo dá esquerda, é possível clicar nos nós, de forma que no grafo da direita irão filtrar os papers
correspondentes aquele autor.  


Reiniciando o aplicativo a base de dados será deletada e criada novamente ao rodar o aplicativo.
