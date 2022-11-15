from flask import render_template
from sqlalchemy import desc

from app import db

from app.models import Subscribe, Recommend, Contribute, Ontology
from app.recommend import recommend


@recommend.route('/all', methods=['GET', 'POST'])
def recommend():
    ans = db.session.query(Ontology).all()
    ontologies_1 = to_list(ans, 1)
    ontologies_2 = to_list(ans, 2)
    ontologies_3 = to_list(ans, 3)
    #print(ontologies_1)

    print(ontologies_1)

    return render_template('recommend/baselist.html', col1=ontologies_1, col2=ontologies_2, col3=ontologies_3)


#id, name, intro, owner, filename
def to_list(ontologies, col):
    list = []
    size = len(ontologies)
    begin = int((col-1)*(size+2)/3)
    end = int(begin+(size+2)/3)
    if end > size :
        end = size

    ontologies = ontologies[begin:end]

    for ontology in ontologies:
        t_list = []
        t_list.append(ontology.id)
        t_list.append(ontology.name)
        t_list.append(ontology.intro)
        t_list.append(ontology.moderator_id)

        list.append(t_list)
    return list
# 获得全部实例, 按照subscribe_nums降序
def get_all_recommends():
    results = db.session.query(
        Recommend,
    ).order_by(desc(Recommend.subscribe_nums)).all()

    return results


# 获得目前火热的8个实例, 按照subscribe_nums降序
def get_8_recommends():
    results = db.session.query(
        Recommend,
    ).order_by(desc(Recommend.subscribe_nums)).limit(8).all()

    return results


# 获得全部用户关注的实例
def get_all_subscribes(user_id):
    results = db.session.query(
        Subscribe, Recommend,
    ).filter(
        Subscribe.user_id == user_id
    ).filter(
        Subscribe.ontology_id == Recommend.ontology_id
    ).all()

    return results


# 获得八个用户关注的实例
def get_8_subscribes(user_id):
    results = db.session.query(
        Subscribe, Recommend,
    ).filter(
        Subscribe.user_id == user_id
    ).filter(
        Subscribe.ontology_id == Recommend.ontology_id
    ).order_by(
        desc(Recommend.subscribe_nums)
    ).limit(8).all()

    return results


# 获得全部用户参与的实例
def get_all_contribute(user_id):
    results = db.session.query(
        Contribute, Recommend,
    ).filter(
        Contribute.user_id == user_id
    ).filter(
        Contribute.ontology_id == Recommend.ontology_id
    ).all()

    return results


# 获得八个用户参与的实例
def get_8_contribute(user_id):
    results = db.session.query(
        Contribute, Recommend,
    ).filter(
        Contribute.user_id == user_id
    ).filter(
        Contribute.ontology_id == Recommend.ontology_id
    ).limit(8).all()

    return results
