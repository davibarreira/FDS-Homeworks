from flask import (Flask, render_template, redirect,
    url_for,jsonify, request, flash)
from forms import AuthorForm
import altair as alt
from altair import Chart, X, Y, Axis, Data, DataFormat
import scrape_scholar as ss
from database_app import Create_DB, Insert_Data
from grafos import Altair_Grafo


app = Flask(__name__)

# Cria uma db nova sempre que rodar o app
Create_DB()

app.config['SECRET_KEY'] = 'iahuq3#%1u982hFA)#($mx'

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST','GET'])
def scrape_author():

    # Fazer pesqusia via link scrape?author=<author>
    searchword = str(request.args.get('author', ''))
    try:

    # Fazer pesquisa atraves da barra de pesquisa
        searchword = str(request.form['author'])
    except:
        pass

    # Recebe o resultado da pesquisa
    try:
        papers = ss.scrape(searchword)
    except:
        flash('Erro na extração. É possível que Google Scholar tenha bloqueado.')
        return redirect(url_for('index'))
    if papers == 0:
        flash('Pesquisador não encontrado')
        return redirect(url_for('index'))

    #Atualizando a base de dados
    Insert_Data(papers)

    flash('Pesquisador encontrado. Coleta com sucesso!')
    return redirect(url_for('index'))

#Criar o grafo e guardar informacoes em url data/grafo
@app.route("/data/grafo")
def grafo():
    chart = Altair_Grafo()

    return chart.to_json()

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
