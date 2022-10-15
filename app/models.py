import datetime
import time

from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from . import login_manager
from authlib.jose import jwt
from authlib.jose.errors import JoseError
from flask import current_app


class Permission:
    FOLLOW = 1
    ISSUE = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16


# 本体
class Ontology(db.Model):
    __tablename__ = 'ontologies'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(64))
    intro = db.Column(db.String(255))
    owner = db.Column(db.String(64))
    lastTime = db.Column(db.TIMESTAMP(), default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # 最后更新时间

    filename = db.Column(db.String(64))
    target_id = db.Column(db.Integer, default=-9999)  # ignore
    moderator_id = db.Column(db.Integer, default=0)
    is_editing = db.Column(db.Boolean, default=False)  # 是否有未解决的编辑


# 本体修改记录
class Modify(db.Model):
    __tablename__ = 'modifies'
    id = db.Column(db.Integer, primary_key=True, index=True)
    ontology_id = db.Column(db.Integer)  # 不做外键为了修改，但保存信息
    time_stamp = db.Column(db.TIMESTAMP, index=True, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    handle_time_stamp = db.Column(db.TIMESTAMP, index=True)
    comment = db.Column(db.String(64))
    moderator_id = db.Column(db.Integer, default=0)  # -1未认领, 0私人, >0 众包
    type = db.Column(db.Integer)  # 0 申请众包, 1 修改, 2 增加, 3 删除
    from_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    filename = db.Column(db.String(64))
    status = db.Column(db.Integer, default=0)  # 0 默认, 1 接受, 2 拒绝
    back_info = db.Column(db.String(255))

    def __init__(self, **kwargs):
        super(Modify, self).__init__(**kwargs)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    @staticmethod
    def insert_roles():
        roles = {
            'User': [Permission.FOLLOW, Permission.ISSUE],
            'Moderator': [Permission.FOLLOW, Permission.ISSUE, Permission.WRITE, Permission.MODERATE],
            'Administrator': [Permission.FOLLOW, Permission.ISSUE, Permission.WRITE, Permission.MODERATE,
                              Permission.ADMIN]
        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def add_permission(self, perm):
        if not self.has_permissions(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permissions(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permissions(self, perm):
        return self.permissions & perm == perm

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)

    # posts = db.relationship('Posts', backref='author', lazy='dynamic')
    # 用户资料

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(name='Administrator').first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    # 设置属性
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 确认散列后是否相同
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 获取token,采用authlib
    def generate_confirmation_token(self):
        header = {'alg': 'HS256'}
        key = current_app.config['SECRET_KEY']

        # 有效时间100s
        exp = int(time.time())
        payload = {'confirm': self.id,
                   'exp': exp}

        s = jwt.encode(header, payload, key)
        return s.decode('utf-8')

    # 用户账户是否确认
    def confirm(self, token):

        key = current_app.config['SECRET_KEY']

        try:
            # type(data) is JWTClaims
            data = jwt.decode(token, key)
            # now, delay=300s
            data.validate(int(time.time()), 300)
            # print(data.get('confirm'))
        except JoseError:
            return False

        if data.get('confirm') != self.id:
            return False

        self.confirmed = True
        db.session.add(self)
        return True

    # 返回是否具有行动权限
    def can(self, perm):
        return self.role is not None and self.role.has_permissions(perm)

    def is_administrator(self):
        return self.can(Permission.ADMIN)

    def __repr__(self):
        return '<User %r>' % self.username


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser


# Flask-Login 要求指定一个函数，从数据库中获取制定标识符的用户
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Recommend(db.Model):
    __tablename__ = 'recommends'
    id = db.Column(db.Integer, primary_key=True, index=True)
    ontology_id = db.Column(db.Integer)  # 不做外键
    ontology_name = db.Column(db.String(64))
    ontology_intro = db.Column(db.String(255))

    subscribe_nums = db.Column(db.Integer, index=True, default=0)
    edit_nums = db.Column(db.Integer, index=True, default=0)
    view_count = db.Column(db.Integer, index=True, default=0)
    today_view_count = db.Column(db.Integer, index=True, default=0)

    seven_days_view = db.Column(db.String(64), default='[]')

    __table_args__ = {
        'mysql_charset': 'utf8'
    }


class Subscribe(db.Model):
    __tablename__ = 'subscribes'
    id = db.Column(db.Integer, primary_key=True, index=True)
    ontology_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    is_subscribed = db.Column(db.Boolean, default=True)  # 表示是否取关
    creat_time = db.Column(db.TIMESTAMP, index=True)
    update_time = db.Column(db.TIMESTAMP, index=True)

    __table_args__ = {
        'mysql_charset': 'utf8'
    }


class Contribute(db.Model):
    __tablename__ = 'contributes'
    id = db.Column(db.Integer, primary_key=True, index=True)
    ontology_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    type = db.Column(db.Integer, index=True)

    time = db.Column(db.TIMESTAMP, index=True)
    commit = db.Column(db.String(255))
    back_info = db.Column(db.String(255))
    filename = db.Column(db.String(64))

    __table_args__ = {
        'mysql_charset': 'utf8'
    }


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))


class OntologyTag(db.Model):
    __tablename__ = 'ontologyTags'
    id = db.Column(db.Integer, primary_key=True)
    ontology_id = db.Column(db.Integer, primary_key=True)
    tag_id =  db.Column(db.Integer, primary_key=True)
