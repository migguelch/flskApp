from flask import render_template

from . import public_Blueprint

@public_Blueprint.route("/")
def index():
    return 'this is an index page'