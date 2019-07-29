from flask import (Flask, render_template, redirect,
    url_for,jsonify, request)
from forms import AuthorForm
import altair as alt
from vega_datasets import data
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
    return render_template('home.html',author='Teste')
    # return '<h1>Hello</h1>'

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
    papers = ss.scrape(searchword)
    if papers == 0:
        return redirect(url_for('index'))

    Insert_Data(papers)

    return redirect(url_for('index'))
    # return str(papers)
    # return redirect(url_for('index'))


teste = data.cars()
WIDTH = 600
HEIGHT = 300

@app.route("/cars")
def show_cars():
    return render_template("cars.html")

@app.route("/data/cars")
def cars_demo():

    chart = Altair_Grafo()

    return chart.to_json()

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
