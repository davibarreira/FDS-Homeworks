from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')
    # return '<h1>Hello</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
