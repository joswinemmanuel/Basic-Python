from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    p_name = "Joswin Woo"
    return render_template("index.html", name=p_name)

@app.route("/french")
def bonjour_world():
    return "Bonjour, World/"

@app.route("/name/<name>")
def hello_name(name):
    return f"Hello, {name}"