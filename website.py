from flask import Flask
app = Flask(__name__)

import os
from flask import render_template

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
