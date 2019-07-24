from flask import Flask, render_template, redirect,url_for,jsonify
from forms import AuthorForm
import altair as alt
from vega_datasets import data

cars = data.cars()


app = Flask(__name__)

app.config['SECRET_KEY'] = 'iahuq3#%1u982hFA)#($mx'

@app.route('/')
def index():
    return render_template('home.html')
    # return '<h1>Hello</h1>'

@app.route('/scrape/<author>')
def scrape(author=None):
    return render_template('home.html',author=author)

@app.route('/vega-example')
def vega():
    chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
)
    chart.save('./templates/vega.html')
    return render_template('vega.html')


@app.route('/test',methods=['GET','POST'])
def test():
    form = AuthorForm()
    print(form.authorname.data)
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('test.html',form=form)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
