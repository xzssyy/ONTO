from flask import render_template, session, redirect, url_for

from .forms import EnglishForm
from . import english
from ..english.controller import query
from ..english.DB import db_initialize


@english.route('/english', methods=['GET', 'POST'])
def english():
    try:
        connection, cursor = db_initialize()
    except Exception:
        return "数据库连接错误(可能电脑开太久了数据库静默了)"
        pass
    else:
        form = EnglishForm()

        if form.validate_on_submit():
            t = form.query.data
            if session.get('T') is None or session['T'] != t:
                answer = query(t, connection, cursor)
                session['T'] = answer
                return redirect(url_for('.english'))

        return render_template('english/english.html',
                               form=form,
                               translated=session.get('T'))
