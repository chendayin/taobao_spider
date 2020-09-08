import pymysql
from DBUtils.PooledDB import PooledDB


class MyPoolDB(object):
    def __init__(self, host, user, password, db_base, max_num=30):
        # 配置
        self.__config = {
            "host": host,
            "user": user,
            "password": password,
            "db": db_base
        }
        self.Pool = PooledDB(pymysql, max_num, **self.__config)

    def get_connect(self):
        return self.Pool.connection()


if __name__ == '__main__':
    host = "192.168.1.114"
    user = "wst_cfg"
    password = "5560203@Wst"
    db = "taobao_live"
    m = MyPoolDB(host, user, password, db)
    db = m.get_connect()
    cursor = db.cursor()
    sql = "select * from data_danmu_QA limit 0,100"
    cursor.execute(sql)
    print(cursor.fetchall())
