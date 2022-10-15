from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..models import User
from .form import LoginForm, RegistrationForm
from .. import db
from ..email import send_email


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            # 是否记住
            login_user(user, form.remember_me.data)
            # next用户原来要访问的保护页面
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('用户名密码出现错误')
    # render_template 优先搜索template目录,在搜索蓝本目录
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("已经登出")
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data.lower(),
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, '确认您的账户', 'auth/email/confirm', user=user, token=token)
        flash('一个验证邮件已经发送')
        return redirect(url_for('main.index'))
    else:
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                print(err)

    return render_template('auth/register.html', form=form)


# 用户确认后重定向到confirm界面，由于保护先登录
@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    # current_user :instance of User model
    if current_user.confirmed:
        print(current_user.confirmed)
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        # 验证函数中add过
        db.session.commit()
        flash('您的账户已经确认了')
    else:
        flash('token无效或超时')
    return redirect(url_for('main.index'))


# 处理过滤未确认的账户
@auth.before_app_request
def before_request():
    # User 继承 UserMixin 方法
    # 1.用户已登录, 匿名用户返回True 2.未确认 3.蓝本路由不在auth即并不是在正常的确认账户流程 4.且访问的端点不是static
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.blueprint != 'auth' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, '确认您的账户', 'auth/email/confirm', user=current_user, token=token)
    flash('一个新的确认邮件已发送')
    return redirect(url_for('main.index'))
