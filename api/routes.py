from flask import render_template
from api import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', answer = 42)

@app.route('/test')
def test():
    return 'test'