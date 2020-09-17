import random
import time
import requests
from hashlib import md5
import re
from urllib import parse
from Mysql_pool_utils import MyPoolDB
from fake_useragent import UserAgent
import json

ua = UserAgent()

bx_umidtoken = r'T2gA0qJaT-o8Vc1zft0S2z5BiwtYJeyBh8qxZh3TudtbRe1rC5T7XJygDLEmxGBNDthmF-dHfnxN7boqYXDqOKro'
bx_ua = r'134#RWJ4G6XwXGEPx8JIZgu6eX0D3QROwKO9sE/w4/PLr3cYhIG/9r0aGRaFQApsbmfFUHNDOlR7Foy1h6B3K5w9qf9zyNVOcro/tOnt+Tq6IgL7oJJqqH8uiNv1QWLFCqpAZtXt+Tp8Aq77I6JtqTpqqygFgGHQCAh+47IIN1PwrnlCVZGKUq3JIYjkHskHafHmBe6C9f1ajxdEoZYV3XTlhb2tBQ93TLNriPH+ApUDJ8o8mE3ZFSPdbCxBMizBFBHtxsR362ccYggViTvASIZH4AP3AOXEnduNSC+/xepafJsVpyZVsHv6di/quvaZ+hfonmCQMAturmQz2hQOCfXANkczKFX6Gv3BcrfkdBZY5DhOV1SsysERgrc1d9JPYxipA0xcHzOF5xi3PNBgMfyRaZGkKzxrsmm91kpjWeqmfZewffTNM4otaAZvM9TO9uam0UDeJgzrLnSqRL7f99HWygWQ4+NXXT/SHDQotHwlWMpOJfNDyVyFCr9Cy4IbdDP10+iP3YXFyNICmFSkX6tFZmSJDx//rZgKTD+jIpTd5Kk6iR04JBvXMoiy2FCi2k0KhC71QJ5hm8BQwpCZiUedOIjsvjKc6xr9PgOZGMHVnK/MVc48H0CGu24VyQt35IWs6nSIUko87GjXj2cRn7hz1h57X5QkptejVp9PjoLwhhqueiTJPFmycdO6HGdyoys2BV83uUMOeySRzuDiGzp7i9phIzPKNljdRc7FeQ04ERwTl0foWDUhzA1CW5usKPCEyrDAe2ymnhJ0fi1tTV5Zdrmrf6QVQuRdC3XMdErAOAm3mvGmIILd0wJaOGnj66FHWNTyfouw83RswYopnldPZMyNtR54yUnwmSsiIAzCfMOTs/P8ptt2NWbXVXJT1xvk7mEC8xPHrPOliCU5D8Of1T/YeOlN1BXXIvz3zDmC0XeNq5C5kKa4XQlkH40JLw7G43CohExpXFs+WDvgWmMnxLHfiB0Cu7OcMVkaA/npFUGaMs1UW2KyFoIbKthHbKk8cR82oPs/VG+RtwuBaqej0xCzY6YlEnEG8CwTWMLfC9hcD7MxrYMuWtLULVr0s7o='
HEADERS = {
    'user-agent': ua['ff'],
    'cookie': '',
    # 'bx-ua': 'T2gAjFhoQO0qL6RMaVPCV9Zxy_fov2ZiPGLmIv2lKJnBOmEahxQoZOM4MDRgRCuU8ELUdgg6qpgkY8ybbN0zLX5K'
}

MY_DB = MyPoolDB(host="192.168.10.78", user="root", password="5560203@wstSpider!", db_base="taobao_product_library")


def get_proxy():
    return requests.get("http://192.168.1.115:5000/get/").json()['proxy']


PROXY = get_proxy()


def get_sign(data, cookie):
    h5_tk = re.findall('_m_h5_tk=(.*?)_', cookie, re.S)[0]
    t = str(int(time.time() * 1000))
    str_data = str(data)
    sign_p = (h5_tk + '&' + t + '&27522521&' + str_data)
    sign = md5((sign_p).encode()).hexdigest()
    return sign, t


def process_time(t, fmt="%Y-%m-%d %X"):
    t = str(t)[:10]
    return time.strftime(fmt, time.localtime(int(t)))


def get_cookie():
    url = "http://192.168.79.38:2778/queryCookie"
    r = requests.get(url)
    result = r.json()
    cookie = result['result']
    return cookie


def save_2_mysql(accountId, liveId, start_time, click_num, click_person_nums, sell_num, sell_price, browser_num,
                 extra_num, mean_second, add_fansNum, pv, online_num,
                 cur_time):
    db = MY_DB.get_connect()
    cursor = db.cursor()
    sql = "replace into taobao_zhongkong_info_realTime values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
        accountId, liveId, start_time, click_num, click_person_nums, sell_num, sell_price, browser_num, extra_num,
        mean_second, add_fansNum, pv, online_num, cur_time)
    cursor.execute(sql)
    db.commit()
    print(f"success insert into taobao_zhongkong_info {sql}")


def get_liveId_info(liveId):
    data = r'{"liveIdList":"[%s]","source":"dbot","fillType":"[1]"}' % (liveId)
    cookie = get_cookie()
    HEADERS['cookie'] = cookie
    sign, t = get_sign(data, cookie)
    utf8data = parse.quote(data)
    url = "https://h5api.m.taobao.com/h5/mtop.mediaplatform.live.batchGetByIdTypeList/1.0/?jsv=2.5.8&appKey=27522521&t=" + \
          t + "&sign=" + sign + \
          "&api=mtop.mediaplatform.live.batchGetByIdTypeList&v=1.0&type=originaljson&dataType=json&timeout=20000&H5Request=true&data=" + utf8data
    req = requests.get(url, headers=HEADERS, proxies={"http": "http://{}".format(PROXY)})
    result = req.json()
    start_time = result['data']['model'][0]['startTime']
    end_time = result['data']['model'][0]['endTime']
    accountId = result['data']['model'][0]['accountId']
    date = process_time(start_time, fmt="%Y%m%d")
    start_time = process_time(start_time)
    end_time = process_time(end_time)
    info = {
        'startTime': start_time,
        'endTime': end_time,
        'accountId': accountId,
        'date': date
    }
    return info


def get_liveId_info_product(liveId):
    liveId_info = get_liveId_info(liveId)
    start_time = liveId_info['startTime']
    end_time = liveId_info['endTime']
    date = liveId_info['date']
    accountId = liveId_info['accountId']
    data = r'{"param":"{\"queryId\":\"2|39819700|undefined\",\"cubeId\":\"dws_mit_cbot_slr_lime_rpt_ov_deal\",\"queryDetail\":false,\"startTime\":\"%s\",\"endTime\":\"%s\",\"timeType\":2,\"sign\":null,\"limit\":1,\"row\":\"[]\",\"measure\":\"[{\\\"name\\\":\\\"引导成交笔数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导成交笔数_粉丝占比\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导成交金额\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导成交金额_粉丝占比\\\",\\\"isMeasure\\\":true}]\",\"column\":\"[]\",\"orders\":\"[]\",\"filter\":\"[{\\\"name\\\":\\\"开播日期分区字段yyyymmdd\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"直播间id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"主播id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[%s],\\\"oper\\\":\\\"=\\\"}]\",\"extra\":null}","innerId":""}' % (
        start_time, end_time, date, liveId, accountId)
    cookie = get_cookie()
    sign, t = get_sign(data, cookie)
    utf8data = parse.quote(data)
    HEADERS['cookie'] = cookie
    HEADERS['user-agent'] = ua[random.choice(['ie', 'ff', 'chrome'])]
    url = "https://h5api.m.taobao.com/h5/mtop.alibaba.iic.xinsightshop.olap.query/1.0/?jsv=2.5.8&appKey=27522521&t=" + \
          t + "&sign=" + sign + \
          "&api=mtop.alibaba.iic.xinsightshop.olap.query&v=1.0&type=originaljson&dataType=json&timeout=20000&H5Request=true&data=" + utf8data
    req = requests.get(url, headers=HEADERS, proxies={"http": "http://{}".format(get_proxy())})
    r = req.json()
    try:
        result = r['data']['data']['cellset'][1:][0]
        return result[0]['properties']['raw'], result[2]['properties']['raw']
    except:
        print(r)
        print(req.request.headers['user-agent'])


def save_liveId_info_all(liveId, sell_num, sell_price, cur_time):
    liveId_info = get_liveId_info(liveId)
    start_time = liveId_info['startTime']
    end_time = liveId_info['endTime']
    date = liveId_info['date']
    accountId = liveId_info['accountId']
    data = r'{"param":"{\"queryId\":\"14|58408952|undefined\",\"cubeId\":\"tblive_rpt_abstract_indicator\",\"queryDetail\":false,\"startTime\":\"%s\",\"endTime\":\"%s\",\"timeType\":2,\"sign\":null,\"limit\":1,\"row\":\"[]\",\"measure\":\"[{\\\"name\\\":\\\"观看次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"额外奖励流量\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"计算平均在线时长\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导进店次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"新增粉丝数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"PM观看次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"PM在线人数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"计算封面图点击率\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"直播间浏览次数_粉丝占比\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导进店次数_粉丝占比\\\",\\\"isMeasure\\\":true}]\",\"column\":\"[]\",\"orders\":\"[]\",\"filter\":\"[{\\\"name\\\":\\\"开播日期分区字段yyyymmdd\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"直播间id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"%s\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"主播id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[%s],\\\"oper\\\":\\\"=\\\"}]\",\"extra\":null}","innerId":""}' % (
        start_time, end_time, date, liveId, accountId)

    cookie = get_cookie()
    sign, t = get_sign(data, cookie)
    utf8data = parse.quote(data)
    HEADERS['cookie'] = cookie
    HEADERS['user-agent'] = ua[random.choice(['ie', 'ff', 'chrome'])]
    url = "https://h5api.m.taobao.com/h5/mtop.alibaba.iic.xinsightshop.olap.query/1.0/?jsv=2.5.8&appKey=27522521&t=" + \
          t + "&sign=" + sign + \
          "&api=mtop.alibaba.iic.xinsightshop.olap.query&v=1.0&type=originaljson&dataType=json&timeout=20000&H5Request=true&data=" + utf8data
    req = requests.get(url, headers=HEADERS, proxies={"http": "http://{}".format(get_proxy())})
    r = req.json()
    result = r['data']['data']['cellset'][1:][0]
    # 直播间浏览次数
    browser_num = result[0]['properties']['raw']
    # 额外激励流量
    extra_num = result[1]['properties']['raw']
    # 平均时长
    mean_second = result[2]['properties']['raw']
    # 商品点击次数
    click_num = result[3]['properties']['raw']
    # 商品点击人数
    click_person_nums = 0
    # 新增粉丝数
    add_fansNum = result[4]['properties']['raw']
    # pv
    pv = result[5]['properties']['raw']
    # 在线人数
    online_num = result[6]['properties']['raw']

    save_2_mysql(accountId, liveId, start_time, click_num, click_person_nums, sell_num, sell_price, browser_num,
                 extra_num, mean_second, add_fansNum, pv, online_num,
                 cur_time)


def main():
    live_id = "278971240786"
    cur_time = process_time(time.time(), fmt="%Y-%m-%d %H:%M:00")
    sell_num, sell_price = get_liveId_info_product(live_id)
    # print(sell_num, sell_price)
    save_liveId_info_all(live_id, sell_num, sell_price, cur_time)


def test_proxy():
    proxy = get_proxy()['proxy']
    req = requests.get("http://httpbin.org/ip", proxies={"http": "http://{}".format(proxy)})
    print(req.text)


if __name__ == '__main__':
    # sell_num, sell_price = get_liveId_info_product("278971240786")
    # print(sell_num, sell_price)
    main()
