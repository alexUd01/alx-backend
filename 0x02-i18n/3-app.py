#!/usr/bin/env python3
""" A simple flask app with internationalization support """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ Language configuration class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ A function that will be invoked to select language translation
    for each request that a user will make
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ Landing page """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
