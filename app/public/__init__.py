from flask import Blueprint

public_Blueprint = Blueprint('public',__name__, template_folder = 'templates')

from . import routes