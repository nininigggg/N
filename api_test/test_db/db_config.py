import pymysql


def get_connect():
    connect = pymysql.connect(
        host="litemall.hogwarts.ceshiren.com",
        port=13306,
        user="test",
        password="test123456",
        database="litemall",
        charset="utf8mb4"
    )
    return connect


def execute_mysql(sql):
    connect = get_connect()
    cursor = connect.cursor()
    cursor.execute(sql)
    record = cursor.fetchone()
    return record


if __name__ == '__main__':
    execute_mysql("select * from litemall_cart")
