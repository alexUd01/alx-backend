#!/usr/bin/env python3
""" Docstring here """
from flask import Flask, render_template, request
from flask_babel import Babel
from pytz import country_names

app = Flask(__name__)
babel = Babel(app)


class Config():
    """ Language configuration class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ A function that will be invoked to select language translation
    for each request that a user will make
    """
    query_string = request.query_string.decode(encoding='utf-8')
    if 'locale' in query_string:
        query_list = query_string.split('&')
        for item in query_list:
            if item.startswith('locale'):
                locale = item.split('=')[1]
                # Validate country code
                if locale.upper() in country_names.keys() \
                   and locale.lower() in app.config['LANGUAGES']:
                    return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Landing page """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
