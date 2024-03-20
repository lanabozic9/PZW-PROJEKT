from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/uvod")
def uvod():
    return render_template("uvod.html")


@app.route("/python")
def python():
    return render_template("python.html")

@app.route("/flask")
def flask():
    return render_template("flask.html")


if __name__== "__main__":
    app.run()