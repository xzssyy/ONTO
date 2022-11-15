import datetime
import json
import os
import re
import sys
from shutil import copyfile

from flask import render_template, make_response, send_from_directory, current_app, request, redirect, url_for
from flask_login import current_user
from sqlalchemy import or_

from . import moderator
from .. import db
from ..models import Modify, User, Ontology


@moderator.route('/', methods=['GET', 'POST'])
def index():
    user = User.query.filter_by(username=current_user.username).first()
    if user.role_id == 1:
        return "你没有权限,请向管理员申请"
    lists = Modify.query.filter(or_(Modify.moderator_id == user.id, Modify.moderator_id == -1)).order_by(
        'time_stamp').all()

    list_dict = [{}, {}, {}]  # default, pass, refuse

    for list in lists:
        # 本体被删除, 本体修改记录还在
        try:
            # print(recommend.ontology_id)
            name = Ontology.query.filter_by(id=list.ontology_id).first().name
            list.name = name
            status = list.status

            from_user = User.query.filter_by(id=list.from_id).first().username
            list.from_user = from_user

            if list_dict[status].get(list.name) is None:
                list_dict[status][list.name] = [list]
            else:
                list_dict[status][list.name].append(list)
        except:
            continue

    return render_template('moderator.html', list_dict=list_dict)


@moderator.route("/download_file", methods=['GET'])
def download_file():
    filename = request.args['filename']
    ontology_id = request.args['ontology_id']
    isTemp = eval(request.args['isTemp'])

    if isTemp:
        url = os.path.join(str(current_app.config['UPLOAD_TEMP_FOLDER']), ontology_id)
        url = str(url).replace("/", "\\")
        print(url)
    else:
        url = os.path.join(str(current_app.config['UPLOAD_FOLDER']), ontology_id)
        url = str(url).replace("/", "\\")
        print(url)

    response = make_response(
        send_from_directory(url, filename.encode('utf-8').decode('utf-8'), as_attachment=True))

    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    print(filename)
    return response


@moderator.route("/pass", methods=['POST'])
def decision_pass():
    pass_info = request.form.get('pass_info')
    modify_id = request.form.get('modify_id')

    modify_instance = db.session.query(Modify).filter(Modify.id == modify_id).first()

    if modify_instance.type == 0:
        # 处理众包
        handle_crowdsource_upgrade(pass_info, modify_instance)
    else:
        # 处理更新
        handle_pass_upgrade(pass_info, modify_instance)

    return redirect(url_for('moderator.index'));


def handle_crowdsource_upgrade(pass_info, modify_instance):
    moderator_id = current_user._get_current_object().id

    # 处理申请记录
    modify_instance.status = 1  # 1 是通过， 0 用来测试
    modify_instance.handle_time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    modify_instance.back_info = pass_info

    # 处理本体
    ontology_instance = db.session.query(Ontology).filter_by(id=modify_instance.ontology_id).first()
    ontology_instance.is_editing = False
    ontology_instance.last_time = modify_instance.handle_time_stamp
    ontology_instance.moderator_id = moderator_id

    db.session.commit()

    # 更新version
    update_version(modify_instance=modify_instance)


def handle_pass_upgrade(pass_info, modify_instance):
    # 处理申请记录
    modify_instance.status = 1  # 1 是通过， 0 用来测试
    modify_instance.handle_time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    modify_instance.back_info = pass_info

    # 处理本体
    ontology_instance = db.session.query(Ontology).filter_by(id=modify_instance.ontology_id).first()
    ontology_instance.filename = modify_instance.filename
    ontology_instance.is_editing = False
    ontology_instance.last_time = modify_instance.handle_time_stamp

    # copy 文件
    move_temp_file(modify_instance.ontology_id, modify_instance.filename)

    db.session.commit()

    # 更新version
    update_version(modify_instance=modify_instance)


def move_temp_file(ontology_id, filename):
    json_filename = re.sub("\..+", ".json", filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']
    upload_temp_folder = current_app.config['UPLOAD_TEMP_FOLDER']

    source = upload_temp_folder + r"\{}\{}".format(ontology_id, filename)
    source_json = upload_temp_folder + r"\{}\json\{}".format(ontology_id, json_filename)

    target = upload_folder + r"\{}\{}".format(ontology_id, filename)
    target_json = upload_folder + r"\{}\json\{}".format(ontology_id, json_filename)

    try:
        copyfile(source, target)
        copyfile(source_json, target_json)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        # exit(1)
    except:
        print("Unexpected error:", sys.exc_info())
        # exit(1)
    finally:
        print('COPY DONE')


# 通过后更新version版本, 同时更新ontology
def update_version(modify_instance=None):
    pass



def dict_crowdsource_message(modify):
    json_dict = {'info': '开启众包', 'type': '0', 'filename': modify.filename}
    return json_dict


# 拒绝
@moderator.route("/reject", methods=['POST'])
def decision_reject():
    reject_info = request.form.get('reject_info')
    modify_id = request.form.get('modify_id')

    # 处理modify
    modify_instance = db.session.query(Modify).filter(Modify.id == modify_id).first()
    modify_instance.status = 2
    modify_instance.handle_time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    modify_instance.back_info = reject_info

    #处理本体状态
    ontology_instance = db.session.query(Ontology).filter_by(id=modify_instance.ontology_id).first()
    ontology_instance.is_editing = False
    ontology_instance.moderator_id = 0

    db.session.commit()

    return redirect(url_for('moderator.index'));
