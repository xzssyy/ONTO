import datetime

from flask import render_template, session, redirect, url_for, current_app, request, make_response, jsonify, flash
from flask_login import current_user, login_required

from .. import db
from ..models import User, Ontology, Modify, Subscribe
from . import main
from ..recommend.views import get_8_subscribes, get_all_recommends, get_8_contribute, get_8_recommends


@main.route('/', methods=['GET', 'POST'])
def index():
    # 4个展示box
    boxes = None

    # rank表，全部， 订阅， 参与贡献
    rank_lists = {'all': get_8_recommends(), 'subscribe': None, 'contribute': None}

    if current_user.is_authenticated:
        user_id = current_user._get_current_object().id
        subscribe_instance = get_8_subscribes(user_id)
        boxes = subscribe_instance[:4]
        rank_lists['subscribe'] = subscribe_instance
        rank_lists['contribute'] = get_8_contribute(user_id)

    else:
        boxes = get_8_recommends()[:4]

    return render_template('index.html', boxes=boxes, rank_lists=rank_lists)


# 用户中心展示
@login_required
@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    ans = Ontology.query.filter_by(owner=username).all()
    return render_template('user.html', user=user, ontologies=ans)


# 本体删除
@main.route('/delete')
def delete():
    ontology_id = request.args.get('ontology_id')
    # print(ontology_id)
    ontology = Ontology.query.get(ontology_id)
    db.session.delete(ontology)
    db.session.commit()
    # return render_template('user.html', user=user, ontologies=ans)
    return 'ok'


# 本体关注
@main.route('/subscribe')
def subscribe():
    user_id = request.args.get('user_id')
    ontology_id = request.args.get('ontology_id')

    subscribe_instance = db.session.query(Subscribe).filter(
        Subscribe.user_id == user_id,
        Subscribe.ontology_id == ontology_id
    ).first()

    if subscribe_instance:
        if not subscribe_instance.is_subscribed:
            subscribe_instance.is_subscribed = True
            subscribe_instance.creat_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            return '你已经关注过了'
    else:
        new_subscribe_instance = Subscribe(ontology_id=ontology_id,
                                           user_id=user_id,
                                           creat_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                           update_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        db.session.add(new_subscribe_instance)

    db.session.commit()

    return '已关注'


# 本体取消关注
@main.route('/un_subscribe')
def un_subscribe(user_id, ontology_id):
    subscribe_instance = db.session.query(Subscribe).filter(
        Subscribe.user_id == user_id,
        Subscribe.ontology_id == ontology_id
    ).first()

    subscribe_instance.is_subscribed = False

    db.session.commit()

    return '已取消关注'


# 本体申请众包, 提交申请记录
@main.route('/crowdsources')
def crowdsources():
    # 修改版本体属性
    ontology_id = request.args.get('ontology_id')
    ontology = Ontology.query.get(ontology_id)
    # print(ontology_id)
    ontology.moderator_id = -1;
    # 申请众包期间不得修改
    ontology.is_editing = True
    db.session.commit()

    from_id = db.session.query(User).filter_by(username=ontology.owner).first().id
    # 提交申请记录
    message_apply_crowdsources(ontology, from_id)

    # return render_template('user.html', user=user, ontologies=ans)
    return 'ok'


def message_apply_crowdsources(ontology, from_id):
    crowdsources_message = Modify(ontology_id=ontology.id,
                                  time_stamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                  moderator_id=ontology.moderator_id,
                                  type=0,  # 申请类型
                                  from_id=from_id,
                                  filename=ontology.filename,
                                  status=0,
                                  back_info=None
                                  )
    db.session.add(crowdsources_message)
    db.session.commit()
