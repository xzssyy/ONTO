from .DB import db_search, db_insert
from .api import api_search


def query(text, connection, cursor):
    # 首先对数据库查询
    result = db_search(text, cursor, connection)
    print('第一次数据库查询完成！')

    if result is not None:
        showResult: str = '{} {} time:{}    lsat:{}'.format(str(result[1]),
                                                            str(result[4]),
                                                            str(result[3]),
                                                            str(result[2]))
    else:
        transResult = api_search(text)
        db_insert(text, transResult, cursor, connection)
        result = db_search(text, cursor, connection)
        showResult: str = '{} {} time:{}    last:{}'.format(str(result[1]),
                                                            str(result[4]),
                                                            str(result[3]),
                                                            str(result[2]))

    return showResult
