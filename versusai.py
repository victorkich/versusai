from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/victor")
def victor():
    return render_template('victor.html')

@app.route("/dranaju")
def dranaju():
    return render_template('dranaju.html')

@app.route("/alisson")
def alisson():
    return render_template('alisson.html')

@app.route("/ricardo")
def ricardo():
    return render_template('ricardo.html')

@app.route("/eduardo")
def eduardo():
    return render_template('eduardo.html')

@app.route("/jair")
def jair():
    return render_template('jair.html')

@app.route("/marcelo")
def marcelo():
    return render_template('marcelo.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/icar2019")
def icar2019():
    return render_template('icar2019.html')

@app.route("/icra2021")
def icra2021():
    return render_template('icra2021.html')

@app.route("/jifs2021")
def jifs2021():
    return render_template('jifs2021.html')

@app.route("/jint2021")
def jint2021():
    return render_template('jint2021.html')
