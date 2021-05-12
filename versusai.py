from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/victor")
def test_link():
    return render_template('victor.html')
