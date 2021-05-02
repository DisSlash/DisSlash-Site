from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("redirect.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/features')
def features():
    return render_template("features.html")

@app.route('/statistics')
def statistics():
    return render_template("statistics.html")