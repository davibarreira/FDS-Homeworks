from flask import (Flask, render_template, redirect,
    url_for,jsonify, request)
from forms import AuthorForm
import altair as alt
from vega_datasets import data
from altair import Chart, X, Y, Axis, Data, DataFormat



app = Flask(__name__)

app.config['SECRET_KEY'] = 'iahuq3#%1u982hFA)#($mx'

@app.route('/')
def index():
    return render_template('home.html',author='Teste')
    # return '<h1>Hello</h1>'

@app.route('/scrape', methods=['POST','GET'])
def scrape_author():
    searchword = request.args.get('author', '')
    outro = ""
    try:
        outro = request.form['author']
    except:
        pass
    print(searchword)
    return str(searchword)+str(outro)
    # return redirect(url_for('index'))



# @app.route('/scrape/<author>')
# def scrape(author=None):
#     return render_template('home.html',author=author)

@app.route('/vega-example')
def vega():
    source = data.cars()
    brush = alt.selection(type='interval')

    chart = alt.Chart(source).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.condition(brush, 'Cylinders:O', alt.value('grey')),
    ).add_selection(brush)
    graph = jsonify(chart.to_dict())
    # chart.save('chart_example.json')

    # return render_template('vega-example.html')
    # return graph
    # return render_template('vega-example.html', graph=graph)
    chart.save('./templates/vega.html')
    return render_template('vega.html')


@app.route('/test',methods=['GET','POST'])
def test():
    form = AuthorForm()
    print(form.authorname.data)
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('test.html',form=form)


teste = data.cars()
WIDTH = 600
HEIGHT = 300

@app.route("/cars")
def show_cars():
    return render_template("cars.html")

@app.route("/data/cars")
def cars_demo():

    chart = Chart(
        data=teste, height=200, width=300).mark_point().encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            color='Origin',
        ).interactive()
    return chart.to_json()

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
