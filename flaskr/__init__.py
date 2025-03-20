import os

from flask import Flask, render_template, request
from translator import Translator


# source https://flask.palletsprojects.com/en/stable/tutorial/factory/
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",  # CHANGE LATTER
    )

    trans = Translator

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/", methods=["GET"])
    def hello():
        if request.method == "POST":
            trans.set_instr(request.form["input"])
            return render_template("base.html")
        else:
            return render_template("base.html")

    return app
