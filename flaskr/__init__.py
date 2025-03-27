import os

from flask import Flask, render_template, request, redirect, url_for
from flaskr.translator import Translator

translation = "ᚻᚩᚣᛞ"
trans = Translator()


app = Flask(__name__, static_url_path="/static")


@app.route("/")
def base():  # there is an easier way but I can't get the right google terms
    return redirect(url_for("home"))


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return redirect(url_for(request.form["move"]))
    return render_template("home.html")


@app.route("/translator", methods=["GET", "POST"])
def translator():
    translation = "ᚻᚩᚣᛞ"
    trans = Translator()
    if request.method == "POST":
        trans.set_instr(request.form["input"])
        translation = trans.get_outstr()
        return redirect(url_for(staticmethod))
    return render_template("trans.html", translation=translation)


@app.route("/explanation")
def explanation():
    return render_template("expl.html")


@app.route("/key")
def key():
    return render_template("key.html")


if __name__ == "__main__":
    app.run(debug=True)
