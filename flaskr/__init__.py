import os

from flask import Flask, render_template, request
from flaskr.translator import Translator

translation = ""


# source https://flask.palletsprojects.com/en/stable/tutorial/factory/
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    trans = translator.Translator
    translation = trans.get_outstr()
    app.config.from_mapping(
        SECRET_KEY="dev",  # CHANGE LATTER
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/", methods=["GET"])
    def base():
        translation = ""
        if request.method == "POST":
            trans.set_instr(request.form["input"])
            translation = trans.get_outstr()
        return render_template("base.html", translation=translation)

    return app
