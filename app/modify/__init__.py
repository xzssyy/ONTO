from flask import Blueprint

modify = Blueprint('modify', __name__)

# 在views和errors中也在导入，写在结尾防止循环导入
from . import views
