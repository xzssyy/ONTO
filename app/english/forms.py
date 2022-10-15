from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EnglishForm(FlaskForm):
    query = StringField('请输入单词', validators=[DataRequired()], render_kw={"autocomplete": "off"})
    submit = SubmitField('查询', )
