from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/victor")
def victor():
    return render_template('victor.html')

@app.route("/home")
def home():
    return render_template('index.html')
