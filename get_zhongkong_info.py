# coding:utf-8
import time
import requests
from hashlib import md5
import re
from urllib import parse
from Mysql_pool_utils import MyPoolDB

MY_DB = MyPoolDB(host="192.168.10.78", user="root", password="5560203@wstSpider!", db_base="taobao_product_library")


def get_sign(data, cookie):
    h5_tk = re.findall('_m_h5_tk=(.*?)_', cookie, re.S)[0]
    t = str(int(time.time() * 1000))
    t = "1599540136463"
    str_data = str(data)
    sign_p = (h5_tk + '&' + t + '&27522521&' + str_data)
    sign = md5((sign_p).encode()).hexdigest()
    return sign, t



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
    data = r'{"param":"{\"queryId\":\"5|18058052|undefined\",\"cubeId\":\"mit_cbot_slr_lime_rpt_ov_trend_deal\",\"queryDetail\":false,\"startTime\":\"%s\",\"endTime\":\"%s\",\"timeType\":2,\"sign\":null,\"limit\":2000,\"row\":\"[{\\\"name\\\":\\\"时间精确到分钟\\\",\\\"isMeasure\\\":false}]\",\"measure\":\"[{\\\"name\\\":\\\"引导成交金额\\\",\\\"isMeasure\\\":true}]\",\"column\":\"[]\",\"orders\":\"[]\",\"filter\":\"[{\\\"name\\\":\\\"开播日期分区字段yyyymmdd\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"直播间id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"主播id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[%s],\\\"oper\\\":\\\"=\\\"}]\",\"extra\":null}","innerId":""}' % (start_time, end_time, date, liveId, accountId)
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


def save_data_2_mysql_flow_source(cur_time, value, name, date, accountId, liveId, db):
    cursor = db.cursor()
    sql = "replace into zhibo_flow_source values ('{}','{}','{}','{}','{}','{}')".format(accountId, liveId, cur_time,
                                                                                         name, value, date)
    cursor.execute(sql)
    db.commit()
    print(f"success into table {cur_time}---{value}---{name}")


def root():
    cookie = 'thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; cookie2=1e98c048d560e1f47da4e6d679f239b0; t=f2d2588bb07ac5b6a2e1f5c9c79147a9; _samesite_flag_=true; linezing_session=VXyVvJeec5lPLikh176xX3yN_1599028418847qmXd_1; UM_distinctid=17452e2e804900-0ff70c0ea00a0e-3323766-1fa400-17452e2e8059eb; enc=BbkroIkovss866XEqxgr%2BC2DRsaWqXGWCrEidwhCtQdV1hdYyyos0hZZFr7vmIu0AurpGzyswqb%2BTe%2FCFdyf7A%3D%3D; _tb_token_=6330a03eeb99; xlly_s=1; mt=ci=0_0; cna=59bAF7vHb3gCAWp645dO/RM8; sgcookie=E100CBlOyRnSIMPr9OlFw1qT5aPzCmyIYU0NqmVztlft1dZocEs6bCbuvPQTi3bDObn0XQoUZAZ21D4iO3IQgI7R9A%3D%3D; unb=2648620207; uc1=cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&pas=0&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie21=WqG3DMC9EdFp7qHvqFD7pg%3D%3D&existShop=true&cookie14=UoTV5YqamRuWqA%3D%3D; uc3=nk2=s3G%2BATwk&lg2=V32FPkk%2Fw0dUvg%3D%3D&vt3=F8dCufbH4o5inWeokio%3D&id2=UU6lRfPf%2FqNipg%3D%3D; csg=7c41b087; lgc=%5Cu8F69%5Cu7231%5Cu6210; cookie17=UU6lRfPf%2FqNipg%3D%3D; dnk=%5Cu8F69%5Cu7231%5Cu6210; skt=1a79eb4f632dc9aa; existShop=MTU5OTY2MDgzOQ%3D%3D; uc4=nk4=0%40sQ60wgv5W1rQrqOu2gRA0II%3D&id4=0%40U2xo9bKGI5Kp%2F%2Bd0qfN6SUoXHqNy; tracknick=%5Cu8F69%5Cu7231%5Cu6210; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; sg=%E6%88%907d; _nk_=%5Cu8F69%5Cu7231%5Cu6210; cookie1=BvaDpQTlGQxVp1JRlFSnURgPtQvRknYOp%2FmKO7OWHhc%3D; _m_h5_tk=3ab718cb23f60e808b3cd62455b76f45_1599704453341; _m_h5_tk_enc=07c6b8c08d39903c02f5e647d485a739; tfstk=cFufBFNxMtXboHKNujOzQS86MVaGwxfQ1nwmGmOC2BlmEJ1m9wyQasmGBaELN; l=eBQq-VGIOhNWPi6jKOfwourza77OSIRAguPzaNbMiOCP9wCH5RwFWZysbwYMC3GNh6rMR3SxXm94BeYBq3xonxv9go7Q9WHmn; isg=BHt7Bm63oNsKJpxuvkvcm6I4Cl_l0I_SVGxdR204V3qRzJuu9aAfIpkK5mSCbOfK'
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
    # for i in name:
    #     result = get_name_by_cubeId1(cookie, header, accountId, date, start_time, end_time, liveId, i)
    #     for r in result:
    #         cur_time = r[0]['value']
    #         value = r[1]['raw']
    #         print(cur_time, value, i)
    #         save_data_2_mysql(cur_time, value, i, date, accountId, liveId, db)

    result = get_name_by_cubeId2(cookie, header, accountId, date, start_time, end_time, liveId)
    for r in result:
        cur_time = r[0]['value']
        value = r[1]['raw']
        save_data_2_mysql(cur_time, value, "引导成交金额", date, accountId, liveId, db)


def get_source_by_cubeId3(cookie, header, accountId, date, start_time, end_time, liveId):
    data = r'{"param":"{\"queryId\":\"10|45092588|undefined\",\"cubeId\":\"tblive_rpt_source_trend\",\"queryDetail\":false,\"startTime\":\"%s\",\"endTime\":\"%s\",\"timeType\":2,\"sign\":null,\"limit\":2000,\"row\":\"[{\\\"name\\\":\\\"时间精确到分钟\\\",\\\"isMeasure\\\":false},{\\\"name\\\":\\\"直播间来源\\\",\\\"isMeasure\\\":false}]\",\"measure\":\"[{\\\"name\\\":\\\"观看次数\\\",\\\"isMeasure\\\":true}]\",\"column\":\"[]\",\"orders\":\"[]\",\"filter\":\"[{\\\"name\\\":\\\"开播日期分区字段yyyymmdd\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"直播间id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"主播id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[%s],\\\"oper\\\":\\\"=\\\"}]\",\"extra\":null}","innerId":""}' % (
        start_time, end_time, date, liveId, accountId)
    sign, t = get_sign(data, cookie)
    utf8data = parse.quote(data)
    url = "https://h5api.m.taobao.com/h5/mtop.alibaba.iic.xinsightshop.olap.query/1.0/?jsv=2.5.8&appKey=27522521&t=" + t + "&sign=" + sign + "&api=mtop.alibaba.iic.xinsightshop.olap.query&v=1.0&type=originaljson&dataType=json&timeout=20000&H5Request=true&data=" + utf8data
    result = requests.get(url, headers=header).json()
    return result['data']['data']['cellset'][1:]

    # cubeId: tblive_rpt_ind_trend 对应name：新增粉丝数、PM在线人数、浏览次数、PM观看次数、引导进店次数
    # cubeId: mit_cbot_slr_lime_rpt_ov_trend_deal 引导成交金额
    # cubeId: tblive_rpt_source_trend 直播来源
    # cubeId: tblive_rpt_item_indicator


def main():
    cookie = "thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; cookie2=1e98c048d560e1f47da4e6d679f239b0; t=f2d2588bb07ac5b6a2e1f5c9c79147a9; _samesite_flag_=true; linezing_session=VXyVvJeec5lPLikh176xX3yN_1599028418847qmXd_1; UM_distinctid=17452e2e804900-0ff70c0ea00a0e-3323766-1fa400-17452e2e8059eb; enc=BbkroIkovss866XEqxgr%2BC2DRsaWqXGWCrEidwhCtQdV1hdYyyos0hZZFr7vmIu0AurpGzyswqb%2BTe%2FCFdyf7A%3D%3D; _tb_token_=e8a93e61515a0; v=0; cna=59bAF7vHb3gCAWp645dO/RM8; _l_g_=Ug%3D%3D; mt=ci=12_1; unb=2648620207; lgc=%5Cu8F69%5Cu7231%5Cu6210; cookie17=UU6lRfPf%2FqNipg%3D%3D; dnk=%5Cu8F69%5Cu7231%5Cu6210; tracknick=%5Cu8F69%5Cu7231%5Cu6210; sg=%E6%88%907d; _nk_=%5Cu8F69%5Cu7231%5Cu6210; cookie1=BvaDpQTlGQxVp1JRlFSnURgPtQvRknYOp%2FmKO7OWHhc%3D; sgcookie=EB0luVFBCNPNwZYAp4Ffe; uc3=vt3=F8dCufbE77jxkyzKVXM%3D&id2=UU6lRfPf%2FqNipg%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&nk2=s3G%2BATwk; csg=6cb17ab0; skt=0bf8fd6adb91c0ce; existShop=MTU5OTU1NjI3Mg%3D%3D; uc4=nk4=0%40sQ60wgv5W1rQrqOt%2Bc0GwLs%3D&id4=0%40U2xo9bKGI5Kp%2F%2Bd0qfN6StpAjPFf; _cc_=VFC%2FuZ9ajQ%3D%3D; uc1=cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&pas=0&existShop=true&cookie21=VFC%2FuZ9ajC0YedpiVNvreA%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D&cookie14=UoTV5YnIAzkgEw%3D%3D; xlly_s=1; _m_h5_tk=d848c0adfc7ae804b426257a35388db5_1599575690300; _m_h5_tk_enc=9331a84838ad6901dd8a69b86430a086; tfstk=ck3cBNayrmrfLrEoAEajOYV71k4cZ5_aKVuSz4cFt-dS3AuPixjPYn1vZ-DmWG1..; l=eBaWDcRmOisPlgFBXOfwourza77tSIRAguPzaNbMiOCP9i1v5SPhWZykUKLJCnGNh6Y2R3-WSGYuBeYBqImy9nFqmGiJiIDmn; isg=BKenha-GtOlEbTBnrgPHHZaeNttxLHsOTR53ZnkUyzZZaMcqgfzxXj1qimB2gFOG"
    header = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        'cookie': cookie,
    }
    accountId = "2648620207"
    date = "20200906"
    start_time = "2020-09-06 20:02:00"
    end_time = "2020-09-06 23:50:41"
    liveId = "278213045150"
    db = MY_DB.get_connect()
    result = get_source_by_cubeId3(cookie, header, accountId, date, start_time, end_time, liveId)
    for r in result:
        # print(r)
        cur_time = r[0]['value']
        type_ = r[1]['value']
        value = r[2]['raw']
        # print(r)
        save_data_2_mysql_flow_source(cur_time, value, type_, date, accountId, liveId, db)


if __name__ == '__main__':
    main()
