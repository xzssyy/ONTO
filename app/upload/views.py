import os
import re
import time

from flask import render_template, request, current_app
from flask_login import login_required, current_user

from app import db
from app.models import Ontology, Tag, OntologyTag
from app.upload import upload

import chardet
import codecs


class Ontology_type:
    pass


@upload.route('/', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        productName = request.form.get('product_name')
        productInfo = request.form.get('product_info')
        productFile = request.files.get('product_file')
        tags = request.form.get('tags')

        ontology = Ontology(name=productName,
                            intro=productInfo,
                            owner=current_user.username,
                            filename=productFile.filename)

        tags_list = []
        tags = tags.split(',')
        for t in tags:
            tag = Tag(title=t)
            tags_list.append(tag)
            db.session.add(tag)


        db.session.add(ontology)
        db.session.commit()

        ontology_id = ontology.id
        for t in tags_list:
            ontologyTag = OntologyTag(ontology_id=ontology_id, tag_id=t.id)
            db.session.add(ontologyTag)

        db.session.commit()

        # file/{ontology_id}/
        url = os.path.join(current_app.config['UPLOAD_FOLDER'], str(ontology.id))
        if not os.path.exists(url):
            os.mkdir(url)
            os.mkdir(os.path.join(url, 'json'))

        productFile.save(os.path.join(url, productFile.filename))
        convert(productFile.filename, os.path.join(url, productFile.filename), str(ontology.id))

        # 初始化版本

        return render_template('upload/complete.html')

    return render_template('upload/upload.html')


def convert(filename, filepath, ontology_id, is_temp=False ):
    out_file_name = re.sub("\..+", ".json", filename)
    tool_path = current_app.config['TOOL_PATH']
    upload_folder = current_app.config['UPLOAD_FOLDER']
    upload_temp_folder = current_app.config['UPLOAD_TEMP_FOLDER']
    if not is_temp:
        val = os.popen(
            r"java -jar {} -file {} -output "
            r"{}\{}\json\{}".format(
                tool_path, filepath, upload_folder, ontology_id, out_file_name, ))
    else:
        val = os.popen(
            r"java -jar {} -file {} -output "
            r"{}\{}\json\{}".format(
                tool_path, filepath, upload_temp_folder, ontology_id, out_file_name, ))

    t = val.readlines()
    for line in t:
        print(line)

    # 文件上传需要延迟
    time.sleep(1)
    change_encoding(ontology_id, out_file_name, is_temp=is_temp)


def change_encoding(ontology_id, filename, is_temp=False):
    upload_folder = current_app.config['UPLOAD_FOLDER']
    upload_temp_folder = current_app.config['UPLOAD_TEMP_FOLDER']

    if not is_temp:
        filename = r"{}\{}\json\{}".format(upload_folder, ontology_id, filename)
    else:
        filename = r"{}\{}\json\{}".format(upload_temp_folder, ontology_id, filename)
    with open(filename, 'rb') as f:
        data = f.read()
        encoding_type = chardet.detect(data)
        # print(encoding_type)

    encoding_in = 'gb2312'
    encoding_out = 'utf-8'

    with codecs.open(filename, mode='r', encoding=encoding_in) as fin:
        data = fin.read()
        with open(filename, mode='w', encoding=encoding_out) as fout:
            fout.write(data)
            fout.close()



