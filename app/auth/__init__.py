# 身份验证


from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import view
