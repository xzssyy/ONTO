import json
import re

from flask import render_template, send_file, make_response, request, current_app
from app import db
import app
from . import webOWL
from ..models import User, Ontology


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

    if (len(filename) != 0):
        return render_template('webOWL/index.html',
                               ontology_id=ontology_id,
                               ontology=ontology_instance,
                               moderator=moderator_name,
                               filename=filename
                               )  # target_id=target_id)
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
    path = path + '/' + str(filename)
    print(path)
    return send_file(path)


@webOWL.route('/fullscreen/data')
def fullscreen_data():
    filename = request.args.get('filename')
    # owner = request.args.get('owner')
    ontology_id = request.args.get('ontology_id')
    path = current_app.config['UPLOAD_FOLDER'] + r'\{}\json'.format(ontology_id)
    # path = r'C:\Users\panyue\Desktop\platform\file\{}\json'.format(owner)
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
