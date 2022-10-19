import pymysql


def get_conn():
    conn = pymysql.connect(host='106.53.104.31',
                           user='root',
                           password='123456',
                           database='demo',
                           charset='utf8mb4')
    return conn
