#!/usr/bin/env python3
""" Docstring here """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import country_names, all_timezones
from pytz.exceptions import UnknownTimeZoneError
from typing import Dict, Any, List, Union

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """ Language configuration class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_param_value(substring: str, query_string: str) -> Any:
    """ A helper function that retrieves the paramater values from a url
    query
    """
    if substring in query_string:
        query_list = query_string.split('&')
        for item in query_list:
            if item.startswith(substring + '='):
                param_value = item.split('=')[1]
                return param_value


@babel.localeselector
def get_locale():
    """ A function that will be invoked to select language translation
    for each request that a user will make
    """
    query_string = request.query_string.decode(encoding='utf-8')

    locale = get_param_value('locale', query_string)
    # 1. Check locale from url
    if locale is not None:
        if locale.upper() in country_names.keys() \
           and locale.lower() in app.config['LANGUAGES']:
            return locale
    # 2. Check locale from user setting
    if locale is None:
        pass
    # 3. Check locale from request header
    if locale is None:
        local = request.headers['Accept-Language']
        return local.split(',')[0][:2]
    # 4. Use default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ Retrieve timezone info """
    query_string = request.query_string.decode(encoding='utf-8')
    print('hello')

    timezone = get_param_value('timezone', query_string)
    print(dir(request.headers))
    try:
        # 1. Check locale from url
        if timezone is not None:
            tzone = pytz.timezone(timezone)
            return tzone.zone
        # 2. Check locale from user setting
        if timezone is None:
            pass
        # 3. Check locale from request header
        if timezone is None:
            timezone = request.headers['The-Time-Zone-IANA']
            tzone = pytz.timezone(timezone)
            return tzone.zone
    except UnknownTimeZoneError:
        # 4. Use default locale
        return request.accept_languages.best_match(
            app.config['BABEL_DEFAULT_TIMEZONE']
        )


def get_user(user_id) -> Dict:
    """ Helper function that mocks database connection """
    if user_id is not None:
        return users.get(int(user_id))


@app.before_request
def before_request() -> None:
    """ A function to be executed before other functions """
    query_string = request.query_string.decode(encoding='utf-8')
    user_id = get_param_value('login_as', query_string)
    g.user = get_user(user_id)


@app.route('/')
def index() -> str:
    """ Landing page """
    return render_template('7-index.html', user=g.user)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
