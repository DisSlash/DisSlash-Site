from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/features')
def features():
    return render_template("features.html")

@app.route('/statistics')
def statistics():
    return render_template("statistics.html")

@app.route('/invite')
def invite():
    return render_template("invite.html")

@app.route('/commands')
def commands():
    return render_template("commands.html")

@app.route("/rickroll")
def rickroll():
    return render_template("rickroll.html")
    

@app.errorhandler(404)
def page_no_found(e):
    return render_template("404.html"), 404
