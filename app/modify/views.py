import json
import os
import re
import time
from datetime import datetime

from flask import render_template, request, current_app, redirect
from flask_login import current_user, login_required

from app import db
from app.models import Modify, Ontology, User
from app.moderator.views import update_version, handle_pass_upgrade
from app.modify import modify
from app.upload.views import convert


@modify.route('/', methods=['GET', 'POST'])
@login_required
def index():
    moderator = request.args.get('moderator')
    refer = request.referrer


    if request.method == 'POST':

        timestamp = str(int(time.time()))

        values = json.loads(request.form.get('values'))
        name = values['name']
        moderator = values['moderator']
        refer = request.form.get('refer')

        # 获取更新类型
        update_type = request.form.get('update_type')

        # print(refer)
        ontology_instance = Ontology.query.filter_by(name=name).first()
        # 设为更新中
        ontology_instance.is_editing = True
        ontology_id = ontology_instance.id
        moderator_instance = User.query.filter_by(username=moderator).first()

        # 属于私人本体
        if moderator_instance is None:
            moderator_id = 0
        else:
            moderator_id = moderator_instance.id

        from_id = User.query.filter_by(username=current_user.username).first().id

        update_file = request.files.get('update_file')
        update_info = request.form.get('info')
        url = os.path.join(str(current_app.config['UPLOAD_TEMP_FOLDER']), str(ontology_id))

        if not os.path.exists(url):
            os.mkdir(url)
            os.mkdir(os.path.join(url, 'json'))

        # 加上时间戳
        filename = update_file.filename
        filename = filename.replace('.', '_' + timestamp + '.')

        print(os.path.join(url, filename), 'haha')

        # 储存暂时文件
        update_file.save(os.path.join(url, filename))
        convert(filename, os.path.join(url, filename), str(ontology_id), is_temp=True)

        modify = Modify(ontology_id=ontology_id, comment=update_info, moderator_id=moderator_id, type=update_type,
                        from_id=from_id,
                        filename=filename)

        db.session.add(modify)
        db.session.commit()

        # 私人本体直接更新
        if moderator_id == 0:
            handle_pass_upgrade('私人本体处理', modify_instance=modify)
            # time.sleep(5)

            refer = re.sub('&filename=.+&', '&filename={}&'.format(modify.filename), refer)

        # print(request.referrer)
        return redirect(refer)

    ontology_id = request.args.get('ontology_id')
    ontology_instance = Ontology.query.filter_by(id=ontology_id).first()
    name = ontology_instance.name
    return render_template('modify.html', moderator=moderator, name=name, refer=refer)
