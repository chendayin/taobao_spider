# coding:utf-8
import json
import time
import requests
from hashlib import md5
import re
from urllib import parse
import multiprocessing
from Mysql_pool_utils import MyPoolDB
from send_email import send_email

MY_DB = MyPoolDB(host="192.168.1.114", user="wst_cfg", password="5560203@Wst", db_base='taobao_live')
MY_DB_COOKIE = MyPoolDB(host="192.168.10.78", user="wst_cfg", password="5560203@Wst", db_base='taobao_cj_backlist')


def get_sign(data, cookie):
    h5_tk = re.findall('_m_h5_tk=(.*?)_', cookie, re.S)[0]
    t = str(int(time.time() * 1000))
    str_data = str(data)
    sign_p = (h5_tk + '&' + t + '&27522521&' + str_data)
    sign = md5((sign_p).encode()).hexdigest()
    return sign, t


def getUrl(startTime, endTime, liveId, date_str, cookie, accountId):
    data = r'{"param":"{\"queryId\":\"11|85653411|undefined\",\"cubeId\":\"tblive_rpt_item_indicator\",\"queryDetail\":false,\"startTime\":\"%s\",\"endTime\":\"%s\",\"timeType\":2,\"sign\":null,\"limit\":2000,\"row\":\"[{\\\"name\\\":\\\"商品id\\\",\\\"isMeasure\\\":false},{\\\"name\\\":\\\"主图地址\\\",\\\"isMeasure\\\":false},{\\\"name\\\":\\\"商品标题\\\",\\\"isMeasure\\\":false}]\",\"measure\":\"[{\\\"name\\\":\\\"商品点击次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"商品点击人数\\\",\\\"isMeasure\\\":true}]\",\"column\":\"[]\",\"orders\":\"[]\",\"filter\":\"[{\\\"name\\\":\\\"开播日期分区字段yyyymmdd\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"直播间id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"主播id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[%s],\\\"oper\\\":\\\"=\\\"}]\",\"extra\":null}","innerId":""}' % (
        startTime, endTime, date_str, liveId, accountId)

    header = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        'referer': 'https://databot.taobao.com/tb/tblive?spm=a1z9u.8142865.0.0.2b3034edkwOoPt&liveId={}'.format(liveId),
        'cookie': cookie,
        'bx-ua': '125#c1Eca3tIcWBdesKzP6vX2PdaUxDZjOE8UEG4fmzs+Y7qoZsiwJ3yQZOX/Hy90Tlf08aj+DSbhuu13SZTRqZd/+U0ZAsER6GpsYl4YLFP7VCGfHaXraFaSm61Kkhvz5yuThSEBlOW8h2LY+OvJxCdX7m6wc5KVNcGcUiccgapEgscUXoScvsO6g/XtVjfJmwTBW/B4psqnVaRRLaCRc5IfAzCRPjJUnbn6F0aS+Eeg4I6TmoonyH9JQ+n/epdEFXPU8jG3qjk+WDIHEvBfGaB1HIgGiJzLQalWe31tOLCurFtEyvxZnuK1FFMEXaZS4xcz88IDUnQMrraXk6hzimJ1lJbQMhZ4MXD+Tsq6w1zqEKm42reefAni8Hdqk0pKXOpnws3IbYrkCaQLdzo1aU8cg9tVIfBibDh27OE7p82YLARRzsFEhkANSC8Oh84IugvePION231ig632BrLWBsIqB+rPW/rgFURRh3xI+O72dT2fL3pC2TRO8pyiU/puf9iK49/37fQWtKo8vRELo7ISVMaO97YLflBhF/PZH2tfjRV+RtCk2VX9O3ZcfmOJoLiy+XQ1YRCTxqmX7mSf6dz0ZjnVkR0RdYpOjkyVypBA/ed9F/0LcaAFNGoEgoYGSgpeb50nfMt8KFl7ghLROErPsqxVf0+KEfI1WFoTZXpgmk0/8KR9GwKgsGfvWwbhaBpJ41lLOEwdMiBAAl/Vx8BJiqTl9678GPav/+aSA35q5hT/MAf++pl9V6VIeOHYiwDZlZkJ/7uREx0DYa+fnTw',
        'bx-umidtoken': 'T3273AF52D716EF6E358109CA5A9C41E19FFCA596FFBF0FB65B2DF9C847'
    }

    sign, t = get_sign(data, cookie)
    utf8data = parse.quote(data)
    url = "https://h5api.m.taobao.com/h5/mtop.alibaba.iic.xinsightshop.olap.query/1.0/?jsv=2.5.8&appKey=27522521&t=" + t + "&sign=" + sign + "&api=mtop.alibaba.iic.xinsightshop.olap.query&v=1.0&type=originaljson&dataType=json&timeout=20000&H5Request=true&data=" + utf8data
    result = requests.get(url, headers=header).json()
    try:
        print(result['data']['data']['cellset'][0])
        return result['data']['data']['cellset'][1:]
    except KeyError as e:
        print(e, "页面无数据")
        pass


def get_start_end_time_get(cookie):
    # "https://liveplatform.taobao.com/live/action.do?currentPage=2&pagesize=20&api=get_live_list"
    urls = ["https://liveplatform.taobao.com/live/action.do?currentPage=1&pagesize=20&api=get_live_list",
            "https://liveplatform.taobao.com/live/action.do?currentPage=2&pagesize=20&api=get_live_list"
            ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'cookie': cookie,
        'referer': 'https://liveplatform.taobao.com/live/liveList.htm?spm=a1z9u.data.0.0.1043799fkHu3v4'
    }
    lst = []
    for url in urls:
        r = requests.get(url, headers=headers)
        json_data = r.json()
        data = json_data['model']['data']
        try:
            for obj in data:
                liveId = obj['id']
                startTime = obj['startTime']
                endTime = obj['endTime']
                lst.append([liveId, startTime, endTime])
        except:
            print("时间为获取到")
            continue
    return lst


def data_time():
    timeStamp = int(time.time())
    timeArray = time.localtime(timeStamp)
    daytime = time.strftime("%Y-%m-%d  %H:%M:%S", timeArray)
    return daytime


def connect_db(s):
    conn = MY_DB.get_connect()
    cursor = conn.cursor()
    cursor.execute(s)
    return cursor.fetchall()


def convent_time(st, fmt="%Y-%m-%d %X"):
    time_str = time.localtime(int(st))
    return time.strftime(fmt, time_str)


def insert_table(accountId, liveId, itemId, click_num, click_person_num, startTime, endTime, stm):
    db = MY_DB.get_connect()
    cursor = db.cursor()
    sql = """
            replace into liveId_goods_click_rate values('{}','{}','{}','{}','{}','{}','{}','{}')
            """.format(accountId, liveId, itemId, click_num, click_person_num, startTime, endTime, stm)
    cursor.execute(sql)
    db.commit()
    print(f"成功插入 商品 {itemId},商品点击次数 {click_num}  商品点击人数 {click_person_num} ,时间 {stm} ")


def process_cookie(accountId):
    db = MY_DB_COOKIE.get_connect()
    sql = """ select cookie  from taobao_chajian_cookie where  accountId='{}' order by date desc limit 1 """.format(
        accountId)
    cursor = db.cursor()
    cursor.execute(sql)

    cookie_list = cursor.fetchall()[0][0]
    cookies = json.loads(cookie_list)
    cookie_str = ''
    for c in cookies:
        name = c['name']
        value = c['value']
        name_value = name + "=" + value + ";"
        cookie_str = cookie_str + name_value
    cookie_str = cookie_str.strip("; ")
    return cookie_str


def get_accountIds():
    db = MY_DB_COOKIE.get_connect()
    sql = """   SELECT accountId from taobao_chajian_cookie GROUP BY accountId"""
    cursor = db.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def root(accountLst):
    while True:
        try:
            try:
                accountId = accountLst.pop()[0]
            except IndexError:
                break
            print("---" * 20)
            print("current accountId:", accountId)
            print("---" * 20)
            cookie = process_cookie(accountId)
            content = get_start_end_time_get(cookie)

            if content is None:
                continue
            for c in content:
                liveId, startTime, endTime = c
                stm = convent_time(str(startTime)[:10], fmt="%Y%m%d")
                startTime = str(startTime)[:10]
                endTime = str(endTime)[:10]
                result = getUrl(convent_time(startTime), convent_time(endTime), liveId, stm, cookie, accountId)
                for r in result:
                    insert_table(accountId, liveId, r[0]['raw'], r[3]['raw'], r[4]['raw'], convent_time(startTime),
                                 convent_time(endTime), stm)
        except:
            print("未知错误")
            continue


def main():
    mg = multiprocessing.Manager()
    accountLst = mg.list((get_accountIds()))
    jobs = [multiprocessing.Process(target=root, args=(accountLst,)) for i in range(10)]
    for i in jobs:
        i.start()
    for j in jobs:
        j.join()


if __name__ == '__main__':
    t = time.time()
    main()
    send_email(f"主播商品点击量 更新完毕 花费 {time.time() - t}s", "直播商品点击量")
