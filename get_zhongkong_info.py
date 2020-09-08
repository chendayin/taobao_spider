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

MY_DB = MyPoolDB(host="192.168.10.78", user="root", password="5560203@wstSpider!", db_base="taobao_product_library")


def get_sign(data, cookie):
    h5_tk = re.findall('_m_h5_tk=(.*?)_', cookie, re.S)[0]
    t = str(int(time.time() * 1000))
    str_data = str(data)
    sign_p = (h5_tk + '&' + t + '&27522521&' + str_data)
    sign = md5((sign_p).encode()).hexdigest()
    return sign, t


def data_time():
    timeStamp = int(time.time())
    timeArray = time.localtime(timeStamp)
    daytime = time.strftime("%Y-%m-%d  %H:%M:%S", timeArray)
    return daytime


def get_name_by_cubeId1(cookie, header, accountId, date, start_time, end_time, liveId, name):
    data = r'{"param":"{\"queryId\":\"5|18058052|undefined\",\"cubeId\":\"tblive_rpt_ind_trend\",\"queryDetail\":false,\"startTime\":\"%s\",\"endTime\":\"%s\",\"timeType\":2,\"sign\":null,\"limit\":2000,\"row\":\"[{\\\"name\\\":\\\"时间精确到分钟\\\",\\\"isMeasure\\\":false}]\",\"measure\":\"[{\\\"name\\\":\\\"%s\\\",\\\"isMeasure\\\":true}]\",\"column\":\"[]\",\"orders\":\"[]\",\"filter\":\"[{\\\"name\\\":\\\"开播日期分区字段yyyymmdd\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"直播间id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"主播id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[%s],\\\"oper\\\":\\\"=\\\"}]\",\"extra\":null}","innerId":""}' % (
        start_time, end_time, name, date, liveId, accountId)
    sign, t = get_sign(data, cookie)
    utf8data = parse.quote(data)
    url = "https://h5api.m.taobao.com/h5/mtop.alibaba.iic.xinsightshop.olap.query/1.0/?jsv=2.5.8&appKey=27522521&t=" + t + "&sign=" + sign + "&api=mtop.alibaba.iic.xinsightshop.olap.query&v=1.0&type=originaljson&dataType=json&timeout=20000&H5Request=true&data=" + utf8data
    result = requests.get(url, headers=header).json()
    print(result)
    return result['data']['data']['cellset'][1:]


def get_name_by_cubeId2(cookie, header, accountId, date, start_time, end_time, liveId):
    data = r'{"param":"{\"queryId\":\"5|18058052|undefined\",\"cubeId\":\"mit_cbot_slr_lime_rpt_ov_trend_deal\",\"queryDetail\":false,\"startTime\":\"%s\",\"endTime\":\"%s\",\"timeType\":2,\"sign\":null,\"limit\":2000,\"row\":\"[{\\\"name\\\":\\\"时间精确到分钟\\\",\\\"isMeasure\\\":false}]\",\"measure\":\"[{\\\"name\\\":\\\"引导成交金额\\\",\\\"isMeasure\\\":true}]\",\"column\":\"[]\",\"orders\":\"[]\",\"filter\":\"[{\\\"name\\\":\\\"开播日期分区字段yyyymmdd\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"直播间id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"主播id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[%s],\\\"oper\\\":\\\"=\\\"}]\",\"extra\":null}","innerId":""}' % (
        start_time, end_time, date, liveId, accountId)
    sign, t = get_sign(data, cookie)
    utf8data = parse.quote(data)
    url = "https://h5api.m.taobao.com/h5/mtop.alibaba.iic.xinsightshop.olap.query/1.0/?jsv=2.5.8&appKey=27522521&t=" + t + "&sign=" + sign + "&api=mtop.alibaba.iic.xinsightshop.olap.query&v=1.0&type=originaljson&dataType=json&timeout=20000&H5Request=true&data=" + utf8data
    result = requests.get(url, headers=header).json()
    return result['data']['data']['cellset'][1:]


def save_data_2_mysql(cur_time, value, name, date, accountId, liveId, db):
    cursor = db.cursor()
    sql = "replace into zhibo_flow_trend values ('{}','{}','{}','{}','{}','{}')".format(accountId, liveId, cur_time,
                                                                                        name, value, date)
    cursor.execute(sql)
    db.commit()
    print(f"success into table {cur_time}---{value}---{name}")


def root():
    cookie = 'thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; cookie2=1e98c048d560e1f47da4e6d679f239b0; t=f2d2588bb07ac5b6a2e1f5c9c79147a9; _samesite_flag_=true; linezing_session=VXyVvJeec5lPLikh176xX3yN_1599028418847qmXd_1; UM_distinctid=17452e2e804900-0ff70c0ea00a0e-3323766-1fa400-17452e2e8059eb; enc=BbkroIkovss866XEqxgr%2BC2DRsaWqXGWCrEidwhCtQdV1hdYyyos0hZZFr7vmIu0AurpGzyswqb%2BTe%2FCFdyf7A%3D%3D; _tb_token_=e8a93e61515a0; xlly_s=1; mt=ci=0_0; cna=59bAF7vHb3gCAWp645dO/RM8; sgcookie=E100eQTaG5JzsbsazedSY%2BafqZGW%2FHDhBLYTYnZPOfxudPWoiVqBAyR%2BrILuEK3w7gJPRzJ7jmcbkfjv1S%2FkS7cbRw%3D%3D; unb=2648620207; uc1=cookie21=VT5L2FSpdeCjwGS%2FFqZpWg%3D%3D&pas=0&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D&cookie14=UoTV5YhjXEfBCw%3D%3D&existShop=true; uc3=nk2=s3G%2BATwk&lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dCufbF5TfEymSzfag%3D&id2=UU6lRfPf%2FqNipg%3D%3D; csg=5d49091b; lgc=%5Cu8F69%5Cu7231%5Cu6210; cookie17=UU6lRfPf%2FqNipg%3D%3D; dnk=%5Cu8F69%5Cu7231%5Cu6210; skt=1e46576b59fa55b8; existShop=MTU5OTQ3NjAxOQ%3D%3D; uc4=nk4=0%40sQ60wgv5W1rQrqOsECJRafQ%3D&id4=0%40U2xo9bKGI5Kp%2F%2Bd0qfN6S9Hirzul; tracknick=%5Cu8F69%5Cu7231%5Cu6210; _cc_=UIHiLt3xSw%3D%3D; _l_g_=Ug%3D%3D; sg=%E6%88%907d; _nk_=%5Cu8F69%5Cu7231%5Cu6210; cookie1=BvaDpQTlGQxVp1JRlFSnURgPtQvRknYOp%2FmKO7OWHhc%3D; _m_h5_tk=de9c4070cf1da745a41f8d5a866d62c6_1599534213149; _m_h5_tk_enc=aae16a1a18f7aab06b94ce5b9cfb1f38; tfstk=cMnRBP4SPIAlxG2xQ4L0dB3c4ToRw0OLGTNhvdFi1wDYGS1DOcmt5PY7d_EvH; l=eBaWDcRmOisPl28FBOfwourza77OSIRAguPzaNbMiOCPOxCe54I5WZyPzV8wC3GNh65yR3-WSGYuBeYBqI2MuMQVSJsmJ2Hmn; isg=BHd3GS-m5Bj192CXfhP3jUauBmvBPEuevQ5H9skkk8ateJe60Qzb7jVeWtAmkCMW'
    header = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        'cookie': cookie,
    }
    accountId = "2648620207"
    date = "20200906"
    start_time = "2020-09-06 20:02:00"
    end_time = "2020-09-06 23:50:41"
    liveId = "278213045150"
    name = ['引导进店次数', '新增粉丝数', 'PM在线人数', 'PM观看次数', '观看次数', '引导进店次数']
    db = MY_DB.get_connect()
    for i in name:
        result = get_name_by_cubeId1(cookie, header, accountId, date, start_time, end_time, liveId, i)
        for r in result:
            cur_time = r[0]['value']
            value = r[1]['raw']
            print(cur_time, value, i)
            save_data_2_mysql(cur_time, value, i, date, accountId, liveId, db)
        # save_data_2_mysql(result, i, date)
    # result = get_current_browse(cookie, header, accountId, date, start_time, end_time, liveId)
    # result = get_current_browse(cookie, header, accountId, date, start_time, end_time, liveId)
    # print(result)


def main():
    root()
    # cubeId: tblive_rpt_ind_trend 对应name：新增粉丝数、PM在线人数、浏览次数、PM观看次数、引导进店次数
    # cubeId: mit_cbot_slr_lime_rpt_ov_trend_deal 引导成交金额
    # cubeId: tblive_rpt_source_trend 直播来源


if __name__ == '__main__':
    main()
