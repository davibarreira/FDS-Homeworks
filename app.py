from flask import Flask, render_template, redirect, url_for
from forms import AuthorForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'iahuq3#%1u982hFA)#($mx'

@app.route('/')
def index():
    return render_template('home.html')
    # return '<h1>Hello</h1>'



@app.route('/test',methods=['GET','POST'])
def test():
    form = AuthorForm()
    print(form.authorname.data)
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('test.html',form=form)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
