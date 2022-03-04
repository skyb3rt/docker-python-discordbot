from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello_world(name: str = None):
    return render_template("home.html", name=name)
