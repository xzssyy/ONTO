import json
import re

from flask import render_template, send_file, make_response, request, current_app
from app import db
import app
from . import webOWL
from ..models import User, Ontology, OntologyTag, Tag, Modify


@webOWL.route('/blockOWL')
def blockOWL():
    filename = request.args['filename']
    # target_id = request.args['target_id']
    owner = request.args['owner']
    ontology_id = request.args['ontology_id']
    data = ['filename', filename, 'owner', owner, 'ontology_id', ontology_id]  # 'target_id', target_id]
    response = make_response(render_template('webOWL/block.html', data=json.dumps(data)))
    return response


@webOWL.route('/ontology')
def ontology():
    ontology_id = request.args['ontology_id']

    ontology_instance = db.session.query(Ontology).filter(Ontology.id == ontology_id).first()

    owner = ontology_instance.owner
    moderator_id = ontology_instance.moderator_id
    name = ontology_instance.name
    # target_id = request.args['target_id']
    # print(moderator_id)
    tag_instance = db.session.query(OntologyTag).filter(ontology_instance.id == OntologyTag.ontology_id).all()
    tags = []
    for instance in tag_instance:
        tags.append(db.session.query(Tag).filter(Tag.id == instance.tag_id).first().title)

    if int(moderator_id) == -1:
        moderator_name = '等待认领中'
    elif int(moderator_id) == 0:
        moderator_name = '无'
    else:
        moderator_user = User.query.filter_by(id=moderator_id).first()
        moderator_name = moderator_user.username
        print(moderator_name)

    # filename 需要转化为json filename
    filename = ontology_instance.filename
    if filename:
        filename = re.sub('\..+', '', filename)
        # print(filename)

    # version_list
    version_list = get_version_list(ontology_id, owner)
    if (len(filename) != 0):
        return render_template('webOWL/index.html',
                               ontology_id=ontology_id,
                               ontology=ontology_instance,
                               moderator=moderator_name,
                               filename=filename,
                               tags=tags,
                               version_list=version_list)
    else:
        return '<h1>该本体还未上传</>'


# 未找到用户
@webOWL.route('/data')
def data():
    filename = request.args.get('filename')
    # owner = request.args.get('owner')
    ontology_id = request.args.get('ontology_id')
    path = current_app.config['UPLOAD_FOLDER'] + r'\{}\json'.format(ontology_id)
    # path = r'C:\Users\panyue\Desktop\platform\file\{}\json'.format(owner)
    path = path + '\\' + str(filename)
    print(path)
    return send_file(path)


@webOWL.route('/fullscreen/data')
def fullscreen_data():
    filename = request.args.get('filename')
    # owner = request.args.get('owner')
    ontology_id = request.args.get('ontology_id')
    path = current_app.config['UPLOAD_FOLDER'] + r'\{}\json'.format(ontology_id)
    path = path + '/' + str(filename)
    # print(path)
    return send_file(path)


@webOWL.route('/fullscreen/')
def full_screen():
    filename = request.args['filename']
    owner = request.args.get('owner')
    # target_id = request.args['target_id']
    ontology_id = request.args.get('ontology_id')
    refer = request.referrer
    data = ['filename', filename, 'owner', owner, 'ontology_id',
            ontology_id]  # , 'reffer', refer]  # 'target_id', target_id]

    response = make_response(render_template('webOWL/fullscreen.html', data=json.dumps(data)))
    return response


def get_version_list(ontology_id, owner):
    type_mp = {0: '申请众包', 1: '修改', 2: '增加', 3: '删除'}
    status_mp = {0: '处理中', 1: '接受', 2: '拒绝'}
    version_list = []
    modify_instances = db.session.query(Modify).filter(ontology_id == Modify.ontology_id).all()
    for m in modify_instances:
        if m.status == 1:
            # 私人本体信息
            if m.moderator_id == 0:
                from_user = db.session.query(User).filter(User.id == m.from_id).first()
                version_list.append({'operator': from_user.username, 'operate_type': type_mp[m.type],
                                     'status': '成功', 'comment': '私人本体处理',
                                     'time': m.handle_time_stamp})
            elif m.moderator_id > 0:
                from_user = db.session.query(User).filter(User.id == m.from_id).first()
                version_list.append({'operator': from_user.username, 'operate_type': type_mp[m.type],
                                     'status': status_mp[m.status], 'comment': m.comment,
                                     'time': m.handle_time_stamp})
            else:
                from_user = db.session.query(User).filter(User.id == m.from_id).first()
                version_list.append({'operator': from_user.username, 'operate_type': type_mp[m.type],
                                     'status': '成功', 'comment': '申请众包',
                                     'time': m.handle_time_stamp})
    return version_list
