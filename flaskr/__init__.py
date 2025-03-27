import os

from flask import Flask, render_template, request, redirect, url_for
from flaskr.translator import Translator

translation = "ᚻᚩᚣᛞ"
trans = Translator()


app = Flask(__name__)


@app.route("/home")
def home():
    pass


@app.route("/tranlator", methods=["GET", "POST"])
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
    pass


@app.route("/key")
def key():
    pass


if __name__ == "__main__":
    app.run(debug=True)
