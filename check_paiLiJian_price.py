from get_item_real_price import get_price
from Mysql_pool_utils import MyPoolDB
from utlis import *

DB = MyPoolDB(host="192.168.10.76", user="", password="", db_base="zbzs_cj_basic")


def get_pai_li():
    sql = " select itemId,livePrice from wst_center_warehous_item_info where discountype = 1"
    db = DB.get_connect()
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


def save_2_mysql(item_id, real_price, reason, type_):
    cur_time = process_time(time.time())
    sql = "replace into wst_center_warehous_check(itemId,realPrice,tbReason,discounType,updateTime) values('{}','{}','{}','{}','{}')".format(
        item_id, real_price, reason, type_, cur_time)
    db = DB.get_connect()
    cursor = db.cursor()
    cursor.execute(sql)
    print(f'success insert into {sql}')
    db.commit()


def main():
    data = get_pai_li()
    for item_id, price in data:
        try:
            price = float(price.strip())
            real_price = float(get_price(item_id))
            if real_price is None:
                continue
            if price != real_price:
                # 原因
                reason = 1
                # 类型 1表示拍立减
                type_ = 1
                save_2_mysql(item_id, real_price, reason, type_)
            time.sleep(2)
        except:
            continue


if __name__ == '__main__':
    main()
