import time
import requests
from hashlib import md5
import re
from urllib import parse
from Mysql_pool_utils import MyPoolDB
from send_email import send_email
import pandas as pd
import threading
import logging

logger = logging.getLogger("zhongkong")
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
file_handler = logging.FileHandler("zhongkong.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

MY_DB = MyPoolDB(host="192.168.10.78", user="root", password="5560203@wstSpider!", db_base="taobao_product_library")
MY_DB2 = MyPoolDB(host="192.168.10.106", user="root", password="5560203@wstSpider!", db_base="wst_cc")


# db2 = MY_DB2.get_connect()


def get_sign(data, cookie):
    h5_tk = re.findall('_m_h5_tk=(.*?)_', cookie, re.S)[0]
    t = str(int(time.time() * 1000))
    str_data = str(data)
    sign_p = (h5_tk + '&' + t + '&12574478&' + str_data)
    sign = md5((sign_p).encode()).hexdigest()
    return sign, t


def cur_time():
    timeStamp = int(time.time())
    timeArray = time.localtime(timeStamp)
    daytime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return daytime


def save_2_mysql(tradeId, itemId, itemName, create_time, pay_time, recv_time, buyer_nick_mark, confirm_paid_amt, db,
                 cursor, db2,
                 cursor2, tk_status):
    cursor2 = db2.cursor()
    daytime = str(cur_time())
    if recv_time is None:
        recv_time = "0000-00-00 00:00:00"
    sql = f" replace into taobao_union_order_state values('{tradeId}', '{itemId}', '{itemName}', '{create_time}', '{pay_time}', '{recv_time}', '{buyer_nick_mark}', '{confirm_paid_amt}', '{tk_status}','{daytime}')"
    cursor.execute(sql)
    cursor2.execute(sql)
    db.commit()
    db2.commit()
    status = {'14': '确认收货', '12': '支付订单'}
    print(
        f"success insert into taobao_union_order_state {tradeId}----{itemName}---- {confirm_paid_amt}  ----- {buyer_nick_mark} ---- {recv_time} --- {status[tk_status]} ")
    logger.info(
        f"success insert into taobao_union_order_state {tradeId}----{itemName}---- {confirm_paid_amt}  ----- {buyer_nick_mark} ---- {recv_time} --- {status[tk_status]} ")


# 保存当天 订单为确认收货状态的数据
def save_order_state_14(accountId, header, day, cookie, order_type):
    data = r'{"accountId":"%s","beginDate":"%s 00:00:00","endDate":"%s 23:59:59","orderDateType":4,"query":"","hit":5000,"start":0,"orderColumn":"pay_time","orderType":%s}' % (
        accountId, day, day, order_type)
    sign, t = get_sign(data, cookie)
    utf8data = parse.quote(data)
    url = "https://h5api.m.taobao.com/h5/mtop.dreamweb.anchor.board.queryanchororder/1.0/?jsv=2.6.0&appKey=12574478&t=" + t + "&sign=" + sign + "&api=mtop.dreamweb.anchor.board.queryAnchorOrder&v=1.0&type=originaljson&dataType=json&timeout=20000&H5Request=true&data=" + utf8data
    result = requests.get(url, headers=header).json()['data']
    if len(result) == 0:
        print("cookie过期，请及时更新")
        send_email(content="中控台cookie过期", subject='直播中控台商品订单状态信息')
        exit()
    db2 = MY_DB2.get_connect()
    db = MY_DB.get_connect()
    cursor2 = db2.cursor()
    cursor = db.cursor()
    for r in result['model']:
        tradeId = r['order_id']
        itemId = r['item_id']
        itemName = r['item_title']
        create_time = r['create_time']
        pay_time = r['pay_time']
        recv_time = r['confirm_paid_time']
        confirm_paid_amt = r['confirm_paid_amt']
        buyer_nick_mark = r['buyer_nick_mark']
        if confirm_paid_amt is None:
            confirm_paid_amt = r['div_pay_amt']
        save_2_mysql(tradeId, itemId, itemName, create_time, pay_time, recv_time, buyer_nick_mark, confirm_paid_amt, db,
                     cursor,
                     db2,
                     cursor2, "14")


# 保存当天 订单为下单时间的数据
def save_order_state_12(accountId, header, day, cookie, order_type):
    data = r'{"accountId":"%s","beginDate":"%s 00:00:00","endDate":"%s 23:59:59","orderDateType":%s,"query":"","hit":5000,"start":0,"orderColumn":"pay_time","orderType":1}' % (
        accountId, day, day, order_type)
    sign, t = get_sign(data, cookie)
    utf8data = parse.quote(data)
    url = "https://h5api.m.taobao.com/h5/mtop.dreamweb.anchor.board.queryanchororder/1.0/?jsv=2.6.0&appKey=12574478&t=" + t + "&sign=" + sign + "&api=mtop.dreamweb.anchor.board.queryAnchorOrder&v=1.0&type=originaljson&dataType=json&timeout=20000&H5Request=true&data=" + utf8data
    result = requests.get(url, headers=header).json()['data']
    if len(result) == 0:
        print("cookie过期，请及时更新")
        send_email(content="中控台cookie过期", subject='直播中控台商品订单状态信息')
        exit()
    db2 = MY_DB2.get_connect()
    db = MY_DB.get_connect()
    cursor2 = db2.cursor()
    cursor = db.cursor()
    for r in result['model']:
        tradeId = r['order_id']
        itemId = r['item_id']
        itemName = r['item_title']
        create_time = r['create_time']
        pay_time = r['pay_time']
        recv_time = r['confirm_paid_time']
        confirm_paid_amt = r['confirm_paid_amt']
        if confirm_paid_amt is None:
            confirm_paid_amt = r['div_pay_amt']
        buyer_nick_mark = r['buyer_nick_mark']
        save_2_mysql(tradeId, itemId, itemName, create_time, pay_time, recv_time, buyer_nick_mark, confirm_paid_amt, db,
                     cursor,
                     db2,
                     cursor2, "12")


def root():
    try:
        url = "http://192.168.79.39:2778/queryCookie"
        r = requests.get(url)
        result = r.json()
        cookie = result['result']
        header = {
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            'cookie': cookie,
            'referer': 'https://liveplatform.taobao.com/live/home/live-Analysis'
        }
        # 主播ID
        accountId = "2648620207"
        day = time.strftime("%Y-%m-%d", time.localtime(int(time.time()) - 60 * 60 * 24))
        t1 = threading.Thread(target=save_order_state_12, args=(accountId, header, day, cookie, 2))
        t2 = threading.Thread(target=save_order_state_14, args=(accountId, header, day, cookie, 4))
        t1.start()
        t2.start()
    except:
        send_email("中控台云手机异常", "云手机")

    # order_type 返回的订单状态： 1 表示订单所有状态时间 ， 2 表示订单下单时间 ，3 表示订单 支付时间  4 表示订单确认收货时间


def main():
    root()


if __name__ == '__main__':
    main()
