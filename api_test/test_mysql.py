import sys

from api_test.conn import get_conn


def test_demo():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    version = cursor.fetchone()
    print(f"数据库的版本是：{version}")
    conn.close()


def test_creat():
    conn = get_conn()
    cursor = conn.cursor()

    sql = """"
    CREATE TABLE `testcase` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `title` varchar(255) COLLATE utf8_bin NOT NULL,
    `expect` varchar(255) COLLATE utf8_bin NOT NULL,
    `owner` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
    """

    cursor.execute(sql)
    conn.close()


def test_insert():
    conn = get_conn()  # 获取连接
    cursor = conn.cursor()  # 获取游标

    sql = """INSERT INTO testcase
    (id, title, expect, owner)
    values (1, 'S11总决赛', '冠军', 'EDG');
    """

    cursor.execute(sql)  # 执行SQL
    conn.commit()  # 提交


def test_insert1():
    conn = get_conn()  # 获取连接
    cursor = conn.cursor()  # 获取游标

    sql = """INSERT INTO testcase
    (id, title, expect, owner)
    values (2, 'S11全球总决赛', '冠军', 'EDG');
    """
    try:
        cursor.execute(sql)  # 执行SQL
        conn.commit()  # 提交事务
    except:
        conn.rollback()  # 回滚事务
    finally:
        conn.close()  # 关闭连接


def test_retrieve():
    conn = get_conn()  # 获取连接
    cursor = conn.cursor()  # 获取游标
    sql = "SELECT * FROM testcase;"
    # 捕获异常
    try:
        cursor.execute(sql)  # 执行SQL
        record = cursor.fetchone()  # 查询记录
        print(record)
    except Exception as e:
        print(sys.exc_info())  # 打印错误信息
    finally:
        conn.close()  # 关闭连接


def test_update():
    conn = get_conn()
    cursor = conn.cursor()
    sql = "UPDATE testcase SET owner='hogwarts' WHERE id=2;"
    try:
        cursor.execute(sql)  # 执行SQL
        conn.commit()  # 提交事务
    except:
        conn.rollback()  # 回滚事务
    finally:
        conn.close()  # 关闭连接


def test_delete():
    conn = get_conn()  # 获取连接
    cursor = conn.cursor()  # 获取游标
    sql = "DELETE FROM testcase WHERE id=3;"
    try:
        cursor.execute(sql)  # 执行SQL
        conn.commit()  # 提交事务
    except:
        conn.rollback()  # 回滚事务
    finally:
        conn.close()  # 关闭连接
