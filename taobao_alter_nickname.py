import requests
import logging
from bs4 import BeautifulSoup
import random
import re
import time
from hashlib import md5
from Mysql_pool_utils import MyPoolDB
import threading
import redis

logger = logging.getLogger("alter_nickname")
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
file_handler = logging.FileHandler("alter_nickname.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

HUDONG_DB_POOL = MyPoolDB(host="192.168.10.78", user="root", password="5560203@wstSpider!", db_base="taobao_hudong",
                          max_num=5)

NEW_DB_POOL = MyPoolDB(host="192.168.10.78", user="root", password="5560203@wstSpider!",
                       db_base="taobao_product_library",
                       max_num=5)

REDIS_POOL = redis.ConnectionPool(host="192.168.1.115", port=8088, password="5560203@wstSpider!", max_connections=30)
r = redis.Redis(connection_pool=REDIS_POOL)
db = NEW_DB_POOL.get_connect()


def get_nick():
    nick = r.spop("bili_nick").decode()

    return nick.replace(" ", "")


def get1():
    dataone = {"liveId": "245025256023"}
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    }

    ktsts = str(int(time.time() * 1000))
    data = str(dataone)
    sign_p = ('' + '&' + ktsts + '&12574478&' + data)

    sign = md5((sign_p).encode()).hexdigest()

    loginurl = 'https://h5api.m.taobao.com/h5/mtop.mediaplatform.live.encryption/1.0/?jsv=2.4.16&appKey=12574478&t={}&sign={}&api=mtop.mediaplatform.live.encryption&v=1.0&AntiCreep=true&type=jsonp&dataType=jsonp&callback=mtopjsonp7&data={}'.format(
        ktsts, sign, str(dataone))
    r = requests.get(loginurl, headers=headers)
    cookies1 = r.cookies
    return cookies1


def get_mh5():
    cookie_jar = get1()
    _m_h5_tk = cookie_jar['_m_h5_tk']
    _m_h5_tk_enc = cookie_jar['_m_h5_tk_enc']
    return '_m_h5_tk=' + _m_h5_tk + ";_m_h5_tk_enc=" + _m_h5_tk_enc + ";"


def get_cookie():
    db = HUDONG_DB_POOL.get_connect()
    cursor = db.cursor()
    sql = "SELECT cookies,userid from sell_account_password where cookie_status =0 ORDER BY update_time desc limit 10"
    cursor.execute(sql)
    cookie, user_id = random.choice(cursor.fetchall())
    new = cookie + get_mh5()
    return new, user_id


def change_cookie_status(userId):
    db = HUDONG_DB_POOL.get_connect()
    cursor = db.cursor()
    sql = " UPDATE sell_account_password set cookie_status = 1 WHERE userid = {}".format(userId)
    cursor.execute(sql)
    db.commit()
    print("cookie状态更新成功")


def get_profileNick(cookie):
    profile_url = "https://i.taobao.com/my_taobao.htm?spm=0.0.0.0.Zk3FyL&tracelog=mytaobaonavindex&nekot=1470211439696"
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "Cookie": cookie}
    r = requests.get(profile_url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    try:
        nickname = soup.select(
            "#J_Col_Main > div > div.mt-ml-c1 > div > div.m-userinfo > div.s-userbar.s-bar > div > div.s-name > a > em")[
            0].text
        return nickname
    except Exception as e:
        print(e)


def check_nick_vaild():
    while 1:
        try:
            nick = get_nick()
        except:
            break
        data = r'{"force":"false","gender":"0","snsNick":"%s"}' % nick
        cookie, userId = get_cookie()
        header = {
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            'referer': 'https://s.m.taobao.com/h5',
            'cookie': cookie,
        }
        t = str(int(time.time() * 1000))
        str_data = str(data)
        h5_tk = re.findall('_m_h5_tk=(.*?)_', cookie, re.S)[0]
        sign_p = (h5_tk + '&' + t + '&12574478&' + str_data)
        sign = md5((sign_p).encode()).hexdigest()
        url = "https://h5api.m.taobao.com/h5/mtop.taobao.cus.tb.user.update/1.0/?jsv=2.3.16&appKey=12574478&t=" + t + "&sign=" + sign + "&api=mtop.taobao.cus.tb.user.update&v=1.0&H5Request=true&ecode=1&AntiCreep=true&AntiFlool=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data=" + data
        try:
            req = requests.get(url, headers=header)
            cur_nick = get_profileNick(cookie)
            if nick == cur_nick:
                cursor = db.cursor()
                sql = "replace into  live_user_nick VALUES('{}')".format(nick)
                try:
                    cursor.execute(sql)
                    db.commit()
                    logger.info(f"success insert into new nick {nick}")
                    print(f"success insert into new nick {nick}")
                except Exception as e:
                    print(e)
                    continue
            else:
                continue
        except Exception as e:
            print(e)
            print("该cookie已经过期...")
            change_cookie_status(userId)
            continue


def main():
    jobs = [threading.Thread(target=check_nick_vaild) for i in range(5)]
    for i in jobs:
        i.start()
    for j in jobs:
        j.join()


if __name__ == '__main__':
    main()

    # print(nick)
