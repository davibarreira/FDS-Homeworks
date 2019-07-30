import sqlite3
import pandas as pd


#Criando base de dados

# Conecta a base de dados "hw1.sqlite", caso não exista, ele cria a base
def Create_DB():
    schema = """
    DROP TABLE IF EXISTS "author";
    DROP TABLE IF EXISTS "paper";
    DROP TABLE IF EXISTS "author_paper";
    CREATE TABLE "author" (
        "id" INTEGER PRIMARY KEY  NOT NULL ,
        "author_name" VARCHAR NOT NULL UNIQUE
    );
    CREATE TABLE "paper" (
        "id" INTEGER PRIMARY KEY  NOT NULL ,
        "paper_name" VARCHAR NOT NULL UNIQUE
    );
    CREATE TABLE "author_paper" (
        paper_id VARCHAR,
        author_id VARCHAR,
        FOREIGN KEY(paper_id) REFERENCES paper(id)
        FOREIGN KEY(author_id) REFERENCES author(id)
    );
    """
    conn = sqlite3.connect('hw1.sqlite',timeout=10)
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

# Função recebe dados de saida da função "scrape"
def Insert_Data(papers):
    # Transforma o dicionario papers em uma lista "flatten" (achatada)
    flat = []
    for i in papers:
        for k in i['authors']:
            flat.append([i['title'],k])
    flat = pd.DataFrame(flat,columns=['paper','author'])

    # Gerar lista de Autores e Artigos unicos para inserir na base de dados
    autores = sorted(set([i for sublist in [i['authors'] for i in papers] for i in sublist]))
    articles= [i['title'] for i in papers] 

    #Inserir autores na tabela author
    ins_author = """
    INSERT OR IGNORE INTO author (author_name) VALUES (?);
    """
    conn = sqlite3.connect('hw1.sqlite',timeout=10)
    for autor in autores:
        conn.execute(ins_author,[autor])
    conn.commit()
    conn.close()

    #Inserir artigos na tabela de paper
    ins_paper = """
    INSERT OR IGNORE INTO paper (paper_name) VALUES (?);
    """
    conn = sqlite3.connect('hw1.sqlite',timeout=10)
    for paper in articles:
        conn.execute(ins_paper,[paper])
    conn.commit()
    conn.close()

    #Gerar relacao dos papers e autores baseados no ir

    ## Montar dataframe de paper x author
    conn = sqlite3.connect('hw1.sqlite',timeout=10)
    paper_ids = []
    for row in conn.execute('SELECT * FROM paper'):
        paper_ids.append(row)
        
    author_ids = []
    for row in conn.execute('SELECT * FROM author'):
        author_ids.append(row)
    conn.close()

    paper_ids = pd.DataFrame(paper_ids,columns=['paper_id','paper'])
    author_ids= pd.DataFrame(author_ids,columns=['author_id','author'])

    paper_author = pd.merge(flat,paper_ids,on='paper')
    paper_author = pd.merge(paper_author,author_ids,on='author')


    ## Inserir na tabela
    ins_paper_author ="""
    INSERT INTO author_paper (paper_id, author_id) \
        VALUES (?,?);
    """

    conn = sqlite3.connect('hw1.sqlite',timeout=10)
    for index,row in paper_author.iterrows():
        conn.execute(ins_paper_author,[row['paper_id'],row['author_id']])
    conn.commit()
    conn.close()