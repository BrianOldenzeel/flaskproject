from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def testpage():
    test = "bob"
    return render_template("main.html", test=test)

@app.route("/kebab")
def kebabpage():
    return "<h1>kebab is lekker</h1>"