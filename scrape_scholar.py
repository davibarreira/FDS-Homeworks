from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests


def scrape(author_name):
    url    = 'https://scholar.google.com.br' 
    autor   = author_name

    # Acessar via browser o site do Google Scholar
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    # Inserir nome do autor a ser buscado e clicar na busca
    inputElement = driver.find_element_by_id("gs_hdr_tsi")
    inputElement.send_keys(autor)
    driver.find_element_by_id('gs_hdr_tsb').click()

    # Buscar a url com o endereço para a página do autor pesquisado
    soup = BeautifulSoup(driver.page_source,  features='lxml')
    try:
        link = soup.find('h4',class_='gs_rt2').contents[0].get('href')
        autor_url = url+link
    except:
        print('Autor não encontrado')
        driver.quit()
        return 0

    # Acessar a página do autor
    driver.get(autor_url)

    # Clicar no botão de "More" para exibir a página completa
    # btn_More = driver.find_element_by_id('gsc_bpf_more')
    btn_More   = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "gsc_bpf_more")))
    for i in range(100):
        time.sleep(0.1)
        if btn_More.get_attribute('disabled')=='true':
            break
        else:
            driver.find_element_by_id('gsc_bpf_more').click()
            
    # Coletar html da página
    soup = BeautifulSoup(driver.page_source,features='lxml')

    # Criar lista com papers contendo artigos e autores
    table = soup.find('table',attrs={"id":'gsc_a_t'})
    papers = []
    for article in table.find_all('td',attrs={"class":'gsc_a_t'}):
        autores = article.find('div',attrs={'class':'gs_gray'}).contents[0].split(',')
        
        # retira o espaço branco no início e final dos nomes, e remove o '...'
        autores = [autor.strip() for autor in autores]
        if autores[-1]=='...': autores.pop()
        
        title   = article.find('a').contents[0]
        papers.append({'title':title,'authors':autores})

        
    # Fechar browser
    driver.quit()
    return papers

def scrape_bypass(url_author):
    # Já passa direto a url do autor
    url = url_author

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    btn_More = driver.find_element_by_id('gsc_bpf_more')
    for i in range(100):
        time.sleep(0.1)
        if btn_More.get_attribute('disabled')=='true':
            break
        else:
            driver.find_element_by_id('gsc_bpf_more').click()
            
    # Coletar html da página
    soup = BeautifulSoup(driver.page_source,features='lxml')

    
    # Criar lista com papers contendo artigos e autores
    table = soup.find('table',attrs={"id":'gsc_a_t'})
    papers = []
    for article in table.find_all('td',attrs={"class":'gsc_a_t'}):
        autores = article.find('div',attrs={'class':'gs_gray'}).contents[0].split(',')
        
        # retira o espaço branco no início e final dos nomes, e remove o '...'
        autores = [autor.strip() for autor in autores]
        if autores[-1]=='...': autores.pop()
        
        title   = article.find('a').contents[0]
        papers.append({'title':title,'authors':autores})

    return papers