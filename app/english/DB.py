import datetime
import mysql.connector
from mysql.connector import Error


def db_initialize():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='eh',
                                             user='root',
                                             password='py20021023')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            return connection, cursor
        else:
            raise Exception
    except Error as e:
        print(e + db_Info)


# 首先查询数据库，返回一条记录
def db_search(text, cursor, connection):
    sql = 'select * from t where word = %s;'
    value = [text]
    cursor.execute(sql, value)
    result = cursor.fetchone()

    # 若查询存在次数加一,更改最新时间
    print(result)
    if result is not None:
        sql = "update t set count = count +1 where ID = %s;"
        values = [str(result[0])]
        print(values)
        cursor.execute(sql, values)
        connection.commit()

        sql = "update t set time = %s where ID = %s;"
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        values = [now, str(result[0])]
        cursor.execute(sql, values)
        connection.commit()

    return result


def db_insert(text, translate, cursor, connection):
    sql = "insert into t(word, time, count, translate) values(%s,%s,%s,%s)"
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    values = (text, now, '1', translate)
    cursor.execute(sql, values)
    connection.commit()
