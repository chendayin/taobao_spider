# !/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests
from urllib.parse import quote_plus
import time
import random
import string
import random
import pymysql
import multiprocessing
import base64
import re
import datetime

appKey = "21646297"
ttid = '700226%40taobao_android_9.3.0'
app_ver = "9.3.0"
ua = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
lat = ""
lng = ""


def user_agent():
    MY_USER_AGENT = [
        "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0",
        "Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3",
        "Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
        "Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1",
        "Mozilla/5.0 (Linux; U; Android 1.5; en-gb; T-Mobile_G2_Touch Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
        "Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522  (KHTML, like Gecko) Safari/419.3",
        "Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
        "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
        "Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]

    return random.choice(MY_USER_AGENT)


def random_str(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for x in range(length))


def call_gw_api(sign_server, api, v, data, pageId='', pageName='', use_cookie=False, uid='', sid='', utdid='',
                deviceId='', Cookie='', features='27',
                method=''):
    requests.packages.urllib3.disable_warnings()
    timestamp = time.time()
    t = int(timestamp)
    UA = user_agent()
    if method == 'GET':
        pageId = ' http%3A%2F%2Fh5.m.taobao.com%2Ftaolive%2Fvideo.html'
        pageName = 'com.taobao.tao.sku.view.MainSkuActivity'
    else:
        pageId = 'http%3A%2F%2Fs.m.taobao.com%2Fh5'
        pageName = 'com.taobao.search.sf.MainSearchResultActivity'
    pre_sign_data = {
        "uid": uid,
        "ttid": ttid,
        "data": quote_plus(data),
        "lng": lng,
        "utdid": utdid,
        "api": api,
        "lat": lat,
        "deviceId": deviceId,
        "sid": sid,
        "x-features": features,
        "v": v,
        "t": str(t),
        "pageName": pageName,
        "pageId": pageId
    }
    sign_dic = get_sign_dic(sign_server, pre_sign_data)
    print(sign_dic)
    body = "data=" + quote_plus(data)
    req_url = "https://acs.m.taobao.com/gw/{0}/{1}/".format(api, v)

    # t = 1590387584
    headers = {
        "x-m-biz-live-bizcode": "TAOBAO",
        "x-features": features,
        "x-sgext": sign_dic['result']['x-sgext'],
        "c-launch-info": "0,0,1588652065055,1588651952000,3",
        "x-page-name": pageName,
        "User-Agent": "MTOPSDK%2F3.1.1.7+%28Android%3B6.0.1%3BSamsung%3BGalaxy+S8%29",
        "x-ttid": quote_plus(ttid),
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "a-orange-q": "appKey=21646297&appVersion=9.6.1&clientAppIndexVersion=1120200504231704166&clientVersionIndexVersion=0",
        # "Content-Length": "343",
        "x-region-channel": "CN",
        "x-appkey": appKey,
        "x-nq": "WIFI",
        "x-mini-wua": quote_plus(sign_dic['result']['x-mini-wua']),

        "x-c-traceid": "XpF17gMK9P0DAM5H9D8NAKDU15886444930540109121941",
        "x-SLIDER-Q": "appKey%3D21646297%26ver%3D1588443286014",
        "x-app-conf-v": str(19),
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "x-bx-version": "6.4.16",
        "x-pv": "6.3",
        "x-t": str(t),
        "x-app-ver": app_ver,
        "f-refer": "mtop",
        "x-nettype": "WIFI",
        "x-utdid": utdid,
        "x-umt": quote_plus(sign_dic['result']['x-umt']),

        "x-devid": deviceId,
        "x-sign": quote_plus(sign_dic['result']['x-sign']),

        "x-page-url": quote_plus(pageId),
        "x-location": quote_plus("{0},{1}".format(lng, lat)),
        "Host": "acs.m.taobao.com"
        # "Accept-Encoding": "gzip",
        # "Connection": "Keep-Alive",
    }
    if uid != "":
        headers["x-uid"] = uid

    if sid != "":
        headers["x-sid"] = sid
    if use_cookie:
        headers["Cookie"] = Cookie

    # print("开始请求:" + api)
    # print("请求淘宝Http头:")
    # for key in headers.keys():
    #     print(key + ":" + headers[key])
    proxie = {  # 'http': '113.66.181.205:25075',
        'http': 'http://117.26.192.168:47608'
    }
    if method == 'GET':
        # print("请求淘宝Http方式: GET")
        req_url = (req_url + "?{0}").format(body)
        # print("请求淘宝url:" + req_url)
        # ,proxies=proxie
        sign_dic = requests.get(req_url, headers=headers, verify=False)

    else:
        print("请求淘宝Http方式: POST")
        print("请求淘宝url:" + req_url)
        print("请求淘宝参数:" + body)

        sign_dic = requests.post(req_url, data=body, headers=headers, verify=True)

    if sign_dic.status_code == requests.codes.ok:

        print("淘宝返回:" + sign_dic.text)
        return sign_dic.text
    else:
        print("淘宝失败返回代码:" + str(sign_dic.status_code))
        print("淘宝失败响应头:" + sign_dic.headers['location'])
        print("淘宝失败返回:" + sign_dic.text)


def get_sign_dic(sign_server, payload):
    headers = {
        "content-type": "application/json;charset=utf-8"
    }
    # print("待签名参数:" + json.dumps(payload))
    res = requests.post(sign_server, data=json.dumps(payload), headers=headers)
    res_content = res.content
    # print("签名返回:" + str(res_content))
    sign_dic = {}
    if res.status_code == requests.codes.ok:
        sign_dic = json.loads(res_content.decode())
    return sign_dic


def get_curr_user(uc_server):
    headers = {
        "content-type": "application/json;charset=utf-8"
    }
    res = requests.post(uc_server, data=json.dumps('{}'), headers=headers)
    res_content = res.content
    print("获取当前登录用户返回:" + str(res_content))
    user_dic = {}
    if res.status_code == requests.codes.ok:
        user_dic = json.loads(res_content.decode())
    return user_dic


def live_searchv3(sign_server, q, uid, sid, utdid, deviceId, cookie_str):
    # data = "{\"q\":\"" + q + "\",\"broadCasterPageNum\":\"0\",\"livePageSize\":\"10\",\"broadCasterPageSize\":\"50\",\"livePageNum\":\"0\",\"viewversion\":\"2.0\"}"
    data = '{"q": "%s ", "broadCasterPageNum": "0", "livePageSize": "10", "broadCasterPageSize": "50","livePageNum": "0", "viewversion": "3.0"}' % q
    v = "1.0"
    api = "mtop.mediaplatform.live.searchv3"
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, Cookie=cookie_str,
                use_cookie=False, method='GET')


# def lightlive_videolist(sign_server, utdid, deviceId):
#     data = "{\"channelId\":\"13\",\"versionDate\":\"20200130\",\"n\":\"20\",\"s\":\"0\",\"moduleIndex\":\"0\",\"PARCELABLE_WRITE_RETURN_VALUE\":\"1\",\"CREATOR\":\"{}\",\"CONTENTS_FILE_DESCRIPTOR\":\"1\"}"
#     v = "1.0"
#     api = "mtop.mediaplatform.lightlive.videolist"
#     call_gw_api(sign_server, api, v, data, utdid=utdid, deviceId=deviceId)


def videolist(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = "{\"queryAd\":\"1\",\"s\":\"0\",\"channelId\":\"29\",\"n\":\"10\",\"deviceLevel\":\"3\",\"version\":\"12\",\"moduleIndex\":\"0\",\"PARCELABLE_WRITE_RETURN_VALUE\":\"1\",\"CREATOR\":\"{}\",\"CONTENTS_FILE_DESCRIPTOR\":\"1\",\"haveOnlook\":\"false\"}"
    v = "5.0"
    api = "mtop.mediaplatform.live.videolist"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def lightlive_videolist(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = "{\"channelId\":\"13\",\"versionDate\":\"20200130\",\"n\":\"20\",\"s\":\"0\",\"moduleIndex\":\"0\",\"PARCELABLE_WRITE_RETURN_VALUE\":\"1\",\"CREATOR\":\"{}\",\"CONTENTS_FILE_DESCRIPTOR\":\"1\"}"
    v = "1.0"
    api = "mtop.mediaplatform.lightlive.videolist"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, pageName=pageName, deviceId=deviceId,
                Cookie=cookie_str, use_cookie=True, method='GET')


def shuapv(sign_server, utdid, deviceId, accountId, accountName, timestamp):
    data = '{"appKey":"21646297","ext":"%s","from":"%s","id":"%s","namespace":1,"role":3,"sdkVersion":"0.3.0","tag":"tb","timestamp":%s,"topic":"b132e16e-59c6-4248-be90-d15eb2f83cd1","utdId":"XpF17gMK9P0DAM5H9D8NAKDU"}' % (
        timestamp, accountName, accountId, timestamp)
    v = "1.0"
    api = "mtop.taobao.powermsg.msg.subscribe"
    call_gw_api(sign_server, api, v, data, utdid=utdid, deviceId=deviceId)


# 刷观看
def shuapv2(sign_server, uid, sid, utdid, deviceId, cookie_str, topic):
    timestamp = int(time.time() * 1000)
    data = r'{"appKey":"21646297","ext":"1598492811764","from":"hu3357055","id":"1006665907","namespace":1,"role":2,"sdkVersion":"0.3.0","tag":"tb","timestamp":1598492811764,"topic":"%s","utdId":"%s"}' % (
        topic, utdid)
    # print(data)
    v = "1.0"
    api = "mtop.taobao.powermsg.msg.subscribe"
    call_gw_api(sign_server, api, v, data, utdid=utdid, deviceId=deviceId, use_cookie=False, Cookie=cookie_str,
                method='GET')


# 刷观看（不可行）
def unsubscribe(sign_server, uid, sid, utdid, deviceId, cookie_str, topic, timestamp, timestamp2):
    # timestamp = int(time.time()*1000)
    # print(timestamp)
    # data ='{"appKey":"21646297","ext":"%s","from":"勾玉楠","id":"1003957259","namespace":1,"role":3,"sdkVersion":"0.3.0","tag":"tb","timestamp":%s,"topic":"%s","utdId":"XpF17gMK9P0DAM5H9D8NAKDU"}'%(timestamp,timestamp,topic)
    data = r'{"appKey":"21646297","ext":"%s","from":"苦涩终","id":"1612710529","namespace":1,"role":5,"sdkVersion":"0.3.0","tag":"tb","timestamp":%s,"topic":"%s","utdId":"XpF17gMK9P0DAM5H9D8NAKDU"}' % (
        timestamp, timestamp2, topic)
    print(data)
    v = "1.0"
    api = "mtop.taobao.powermsg.msg.unsubscribe"
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, sid=sid, deviceId=deviceId, use_cookie=True,
                Cookie=cookie_str, method='GET')


def video_subscribe(sign_server, utdid, deviceId, sid):
    timestamp = int(time.time() * 1000)
    print(timestamp)
    data = '{"accountId":"1612710529"}'
    # data='{"appKey":"21646297","ext":"%s","from":"","id":"","namespace":1,"role":3,"sdkVersion":"0.3.0","tag":"tb","timestamp":%s,"topic":"%s","utdId":""}'%(timestamp,timestamp,topic)
    # print(data)
    v = "1.0"
    api = "mtop.mediaplatform.video.subscribe"
    call_gw_api(sign_server, api, v, data, sid=sid, utdid=utdid, deviceId=deviceId, use_cookie=False, method='GET')


# def test_jinlai(sign_server, utdid, deviceId, cookie_str, sid):
#     timestamp = time.time()
#     data = r'{"bizCode":1,"bizTag":"tb","offset":0,"pagesize":8,"role":5,"sdkversion":"0.3.0","timestamp":1587733510394,"topic":"68087f57-5961-445d-8732-60cd856c6940"}'
#     v = "1.0"
#     api = "mtop.taobao.powermsg.msg.pullnativemsg"
#     call_gw_api(sign_server, api, v, data, utdid=utdid, sid=sid, deviceId=deviceId, Cookie=cookie_str, use_cookie=True)


# def test_enter(sign_server, utdid, deviceId, cookie_str, sid, uid):
#     timestamp = time.time()
#     data = r'{"action":"enter","params":"","scopeId":"970","subScope":"1612710529_1_277380438972","trackParams":"{\"activityId\":\"277380438972\",\"broadcasterId\":\"1612710529\",\"userId\":\"1006665907\"}"}'
#     v = "1.0"
#     api = "mtop.taobao.iliad.task.action"
#     call_gw_api(sign_server, api, v, data, utdid=utdid, sid=sid, uid=uid, deviceId=deviceId, use_cookie=True,
#                 Cookie=cookie_str, method='GET')


def senditemmessage(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = '{"bizCode":"1","itemId":"598777838683","linkUrl":"www.taobao.com","msgType":"1","pictUrl":"https:\/\/wstplug.oss-cn-beijing.aliyuncs.com\/zbzs\/plug-zhongkong\/img\/20191231\/ff_gou.png","price":"","receiveUserId":"1612710529","shareType":"item","title":"款式多多"}'
    v = "1.0"
    api = "mtop.taobao.aris.message.senditemmessage"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True)


def sendfriendshare(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"shareUrl":"https://a.m.taobao.com/i598777838683.htm?price=27&original_price=54&sourceType=item&sourceType=item&suid=a3c32c9c-6948-4b46-ae1f-5a5230a69fbd&ut_sk=1.XpF17gMK9P0DAM5H9D8NAKDU_21646297_1587871287052.Contacts.1","taoFriends":"2207822575874","shareDesc":"2019新款防水双肩包女高中大学生背包手提包韩版潮百搭电脑包批发","shareType":"item","msgType":"1","shareSendName":"","extendInfo":"{\"price\":\"27\"}","activityId":"1","shareItemId":"598777838683","friendName":"好物分享qaq","contacts":"","shareRemark":"","sharePicUrl":"http://img.alicdn.com/imgextra/i4/1714575714/O1CN01RVtwb71s53fGUCc06_!!1714575714.jpg"}'
    v = "1.0"
    api = "mtop.taobao.aris.share.sendfriendshare"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='POST')


def sendfriendshare(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"ccodeList":"[\"0_U_1612710529_275510256858\"]"}'
    v = "1.0"
    api = "mtop.taobao.amp.im.getbatchconversation"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def searchdata(sign_server, uid, sid, utdid, deviceId, cookie_str, accountName):
    # data = '{"q":"%s","broadCasterPageNum":"0","livePageSize":"10","broadCasterPageSize":"5","livePageNum":"0","viewversion":"2.0"}'%accountName
    data = '{"searchID":"","s":"0","n":"10","CREATOR":"{}","PARCELABLE_WRITE_RETURN_VALUE":"1","searchKey":"%s","type":"accountLive","CONTENTS_FILE_DESCRIPTOR":"1"}' % accountName
    v = "1.0"
    api = "mtop.mediaplatform.live.searchv2"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, utdid=utdid, uid=uid, sid=sid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


def search_recommend(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"appId":"10211","params":"{\"URL_REFERER_ORIGIN\":\"https://s.m.taobao.com/h5entry?utparam=%7B%22ranger_buckets_native%22%3A%22tsp2189_23049_newuser01%22%7D&spm=a2141.1.searchbar.searchbox&scm=1007.home_topbar.searchbox.d&_navigation_params=%7B%22needdismiss%22%3A%220%22%2C%22animated%22%3A%220%22%2C%22needpoptoroot%22%3A%220%22%7D\",\"_input_charset\":\"UTF8\",\"_navigation_params\":\"{\\\"needdismiss\\\":\\\"0\\\",\\\"animated\\\":\\\"0\\\",\\\"needpoptoroot\\\":\\\"0\\\"}\",\"_output_charset\":\"UTF8\",\"ad_type\":\"1.0\",\"area\":\"active_page\",\"code\":\"utf-8\",\"editionCode\":\"CN\",\"isBeta\":\"false\",\"placeholder\":\"华为荣耀v30手机\",\"q\":\"\",\"nick\":\"陪你ll\",\"referrer\":\"com.taobao.taobao\",\"scm\":\"1007.home_topbar.searchbox.d\",\"searchdoorFrom\":\"homepage\",\"searchhint\":\"on\",\"searchquery\":\"华为荣耀v30手机\",\"spm\":\"a2141.1.searchbar.searchbox\",\"src\":\"c2c\",\"sversion\":\"9.4\",\"tab\":\"all\",\"ttid\":\"1571044501368@taobao_android_9.6.1\",\"utd_id\":\"XpF17gMK9P0DAM5H9D8NAKDU\",\"utparam\":\"{\\\"ranger_buckets_native\\\":\\\"tsp2189_23049_newuser01\\\"}\"}"} '
    v = "2.0"
    api = "mtop.relationrecommend.wirelessrecommend.recommend"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def collectionids_get(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"favType":1,"size":200,"appName":"taobaolive"} '
    v = "2.0"
    api = "mtop.taobao.mercury.collectionids.get"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def sendmsg(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"msgId":"76bdddf584391bcc1b46d42d0414d907","namespace":1,"qos":0,"sdkVersion":"0.3.0","sendAll":false,"subType":10010,"tagList":"[]","topic":"4a09bd94-baa2-4c6e-bb01-8fb5fd672aae"}'
    v = "1.0"
    api = "mtop.taobao.powermsg.msg.sendmsg"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def get_shop_data(shopid, sellerid, sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"sellerId":"%s","shopId":"%s"}' % (sellerid, shopid)
    v = "1.0"
    api = "mtop.taobao.shop.impression.intro.get"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def get_detail(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"detail_v":"3.3.2","exParams":"{\"__application_id__\":\"taobaolive\",\"appReqFrom\":\"detail\",\"bizType\":\"taolive\",\"container_type\":\"xdetail\",\"cpuCore\":\"4\",\"cpuMaxHz\":\"1608000\",\"descVersion\":\"7.0\",\"dinamic_v3\":\"true\",\"id\":\"579956116482\",\"item_id\":\"579956116482\",\"latitude\":\"0\",\"liveInfo\":\"1612710529~262182342155\",\"longitude\":\"0\",\"nick\":\"苦涩终\",\"osVersion\":\"23\",\"pg1stepk\":\"ucm:262182342155_1612710529\",\"phoneType\":\"Mix\",\"scm\":\"1007.13381.38597.101200300000000\",\"soVersion\":\"2.0\",\"spm\":\"a2141.8001249\",\"spm-cnt\":\"a2141.7631564\",\"ultron2\":\"true\",\"utdid\":\"XpF17gMK9P0DAM5H9D8NAKDU\",\"utparam\":\"{\\\"_tbk\\\":\\\"1\\\"}\"}","itemNumId":"579956116482"} '
    v = "6.0"
    api = "mtop.taobao.detail.getdetail"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def get_detail2(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"detail_v":"3.1.8","exParams":"{\"NAV_START_ACTIVITY_TIME\":\"1588640690571\",\"NAV_TO_URL_START_TIME\":\"1588640690562\",\"ad_type\":\"1.0\",\"bizName\":\"taobaolive\",\"referrer\":\"http://h5.m.taobao.com/taolive/video.html?id=616912768993\"}","itemNumId":"616912768993"} '
    v = "6.0"
    api = "mtop.taobao.detail.getdetail"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def task_action(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"action":"enter","params":"","scopeId":"970","subScope":"1612710529_1_262263248013","trackParams":"{\"activityId\":\"276798272411\",\"broadcasterId\":\"1612710529\",\"userId\":\"1002780897\"}"}'
    v = "1.0"
    api = "mtop.taobao.iliad.task.action"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def task_action1(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"action":"enter","params":"","scopeId":"-1","subScope":"-1","trackParams":"{\"activityId\":\"276798272411\",\"broadcasterId\":\"1612710529\",\"userId\":\"1002780897\"}"} '
    v = "1.0"
    api = "mtop.taobao.iliad.task.action"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=False, method='GET')


def task_action_gotoDetail(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"scopeId":"970","subScope":"1612710529_1_267675607065","action":"gotoDetail","params":"{\"itemId\":593994665414}","trackParams":"{\"activityId\":\"267675607065\",\"broadcasterId\":\"1612710529\",\"userId\":\"1003957259\"}"} '
    v = "1.0"
    api = "mtop.taobao.iliad.task.action"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


# 增加商品点击次数
def track_regist(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"contentId":"275317175314","popularizeTargetId":"606612666404","popularizeTargetType":"1","popularizerId":"1612710529","tcpSceneId":"4","extendInfo":"{\"bizTraceId\":\"2444131929_1612710529_275317175314_606612666404_1596893417363\",\"lightShopStoreId\":\"\"}"}'
    v = "1.0"
    api = "mtop.com.taobao.tcp.track.regist"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=True, method='POST')


# 可以增加商品点击次数
def addtrace(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"platformType":"1","adUserId":"1612710529","contentId":"277380438972","itemId":"568498834282","context":"{\"bizTraceId\":\"1006665907_1612710529_277380438972_568498834282_1598516613389\",\"lightShopStoreId\":\"\"}","popularizeTargetType":"1","businessScenceId":"6","tcpSceneId":"4","sourceType":"2"}'
    v = "1.0"
    api = "mtop.com.taobao.tbtrace.commission.addtrace"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=True, method='POST')


def click_add(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = get_time_stamp13()
    data = r'{"platformType":"1","adUserId":"1990842883","contentId":"274317228250","itemId":"545946056107","context":"{\"bizTraceId\":\"90434288_1990842883_274317228250_545946056107_1596804757395\",\"lightShopStoreId\":\"\"}","businessScenceId":"6","sourceType":"2"}'
    v = "1.0"
    api = "mtop.uzjump.business.cps.click.add"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='POST')


def batch(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"liveEventsJson":"[{\"accountId\":\"1612710529\",\"action\":\"exit\",\"count\":1,\"extendJson\":\"{\\\"entrySource\\\":\\\"null\\\",\\\"fansLevel\\\":\\\"3\\\",\\\"liveSource\\\":\\\"anchorInfo\\\",\\\"roomStatus\\\":\\\"1\\\",\\\"serverParams\\\":\\\"null\\\",\\\"timeShift\\\":\\\"false\\\",\\\"timeShiftEntry\\\":\\\"0\\\"}\",\"feedId\":\"272251178262\",\"scene\":\"taobaolive\",\"timestamp\":\"1594800938230\",\"type\":\"0\"}]"}'
    v = "1.0"
    api = "mtop.taobao.iliad.event.report.batch"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def batch2(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"liveEventsJson":"[{\"accountId\":\"1612710529\",\"action\":\"enter\",\"count\":1,\"extendJson\":\"{\\\"fansLevel\\\":\\\"1\\\",\\\"liveSource\\\":\\\"null\\\",\\\"roomStatus\\\":\\\"1\\\",\\\"serverParams\\\":\\\"null\\\",\\\"sjsdItemId\\\":\\\"null\\\",\\\"timeMovingItemId\\\":\\\"null\\\",\\\"timeShift\\\":\\\"false\\\",\\\"timeShiftEntry\\\":\\\"1\\\"}\",\"feedId\":\"267646029919\",\"scene\":\"taobaolive\",\"timestamp\":\"1591411435307\",\"type\":\"0\"}]"} '
    v = "1.0"
    api = "mtop.taobao.iliad.event.report.batch"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def pullnativemsg(sign_server, uid, sid, utdid, deviceId, cookie_str, topic):
    nowtime = int(time.time()) * 1000
    # data = r'{"bizCode":1,"bizTag":"tb","offset":%s,"pagesize":8,"role":6,"sdkversion":"0.3.0","timestamp":%s,"topic":"%s"}'%(nowtime,nowtime,topic)
    data = r'{"bizCode":1,"bizTag":"tb","offset":1596197659949,"pagesize":50,"role":6,"sdkversion":"0.3.0","timestamp":1596197659949,"topic":"02039bd9-c160-40f7-9227-5043273a31cf"}'
    v = "1.0"
    api = "mtop.taobao.powermsg.msg.pullnativemsg"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    data = call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                       pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')
    return data


def query_latest(sign_server, uid, sid, utdid, deviceId, cookie_str, topic):
    nowtime = int(time.time()) * 1000
    data = r'{"paginationContext":"{\"commentId\":273973567643,\"refreshTime\":1596010461799,\"timestamp\":1596010453000}","order":"asc","topic":"%s","tab":"2","neoRoomType":"0","limit":"20"}' % topic
    v = "1.0"
    api = "mtop.taobao.iliad.comment.query.latest"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def query_latest2(sign_server, uid, sid, utdid, deviceId, cookie_str, topic):
    nowtime = int(time.time()) * 1000
    # data = r'{"paginationContext":"{\"commentId\":272123917951,\"refreshTime\":%s,\"timestamp\":%s}","order":"asc","topic":"%s","tab":"2","neoRoomType":"0","limit":"20"} '%(nowtime,nowtime,topic)
    data = r'{"paginationContext":"{\"commentId\":272123917951,\"refreshTime\":1594860019244,\"timestamp\":1594860012000}","order":"asc","topic":"b3a92ce0-e07b-46fa-8a94-8fce4d83baa4","tab":"2","neoRoomType":"0","limit":"20"}'
    v = "1.0"
    api = "mtop.taobao.iliad.comment.query.latest"
    pageName = "com.taobao.taolivehome.TaoLiveHomepageActivity"
    pageId = "http://h5.m.taobao.com/taolive/main.html"
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


# 刷在线
def addpv(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"anchorId":"1612710529","count":"1","topic":"c89aa991-3381-49ce-a8c6-c86ccbd4caf9","liveId":"273541940277"}'
    v = "1.0"
    api = "mtop.mediaplatform.live.addpv"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


# 刷点赞（无反应）
def task_action(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"scopeId":"970","subScope":"1612710529_1_273936652138","action":"addFavor","params":"{\"favorCount\":\"1\",\"totalFavorCount\":\"1\"}","trackParams":"{\"activityId\":\"273936652138\",\"broadcasterId\":\"1612710529\",\"userId\":\"1002780897\"}"}'
    v = "1.0"
    api = "mtop.taobao.iliad.task.action"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def detail_task_action(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"scopeId":"970","subScope":"1612710529_1_262182342155","action":"gotoDetail","params":"{\"itemId\":579956116482}","trackParams":"{\"activityId\":\"262182342155\",\"broadcasterId\":\"1612710529\",\"userId\":\"1002780897\"}"}'
    v = "1.0"
    api = "mtop.taobao.iliad.task.action"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


# 增加亲密度，缩短时间
def stay_task_action(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"scopeId":"970","subScope":"103838830_1_267537037815","action":"stay","params":"{\"stayTime\":60}","trackParams":"{\"activityId\":\"267537037815\",\"broadcasterId\":\"103838830\",\"userId\":\"267537037815\"}"} '
    v = "1.0"
    api = "mtop.taobao.iliad.task.action"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


# 刷点赞（可行）
def publish(sign_server, uid, sid, utdid, deviceId, cookie_str, topic, j):
    nowtime = int(time.time()) * 1000
    data = r'{"count":"%s","topic":"%s"}' % (j, topic)
    # data = r'{"ext":"%s","timestamp":%s,"topic":"%s","count":"%s"}' % (timestamp, timestamp, topic, j)
    v = "1.0"
    api = "mtop.taobao.iliad.recommend.publish"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


def sendmsg(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"msgId":"27b37dc66245419fa885f8af0eaf3a66","namespace":1,"qos":0,"sdkVersion":"0.3.0","sendAll":false,"subType":10010,"tagList":"[]","topic":"ad136e50-42f4-4f76-9672-98ff3d558e7e"} '
    v = "1.0"
    api = "mtop.taobao.powermsg.msg.sendmsg"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


# 刷谁来了（可行）10031表示进入直播间，10010表示点击商品，
def sendmsg_action(sign_server, uid, sid, utdid, deviceId, cookie_str, topic, nick_ww):
    nowtime = int(time.time()) * 1000
    data_json = '{"identify":{"APASS_USER":"0","VIP_USER":"0","fanLevel":"0"},"nick":"%s","userid":"1612710529"}' % nick_ww
    data_str = data_json.encode('utf-8')
    base64_datas = base64.b64encode(data_str)
    base64_data = base64_datas.decode()
    data = r'{"bizData":"%s","msgId":"27Smzqs0cQDxFvQF","namespace":1,"qos":0,"sdkVersion":"0.3.0","sendAll":false,"subType":10031,"tagList":"[]","topic":"%s"} ' % (
        base64_data, topic)
    v = "1.0"
    api = "mtop.taobao.powermsg.msg.sendmsg"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=False, method='GET')


def get_messageid(topic):
    conn = pymysql.connect(host="192.168.1.114", user="root", passwd="5560203@wstSpider!", db="taobao_live",
                           charset="utf8mb4")
    cursor = conn.cursor()
    sql = "select * from MessagebyNick where nick!=''  order by rand() limit 1"
    # print(param)
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


# 正在去买
def sendmsg_action_buy(sign_server, uid, sid, utdid, deviceId, cookie_str, topic):
    msgIds = get_messageid(topic)
    print(msgIds)
    msgId = msgIds[0][0]
    data = r'{"msgId":"%s","namespace":1,"qos":0,"sdkVersion":"0.3.0","sendAll":false,"subType":10010,"tagList":"[]","topic":"%s"}' % (
        msgId, topic)
    print(data)
    v = "1.0"
    api = "mtop.taobao.powermsg.msg.sendmsg"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, sid=sid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def sendmsg2(sign_server, uid, sid, utdid, deviceId, cookie_str, topic):
    msgIds = get_messageid(topic)
    print(msgIds)
    msgId = msgIds[0][0]
    nick = msgIds[0][1]
    data_json = '{"identify":{"APASS_USER":"0","VIP_USER":"0","fanLevel":"0"},"nick":"%s","userid":"1612710529"}' % nick
    data_str = data_json.encode('utf-8')
    base64_datas = base64.b64encode(data_str)
    base64_data = base64_datas.decode()
    data = r'{"bizData":"tb","msgId":"%s","namespace":1,"qos":0,"sdkVersion":"0.3.0","sendAll":false,"subType":10010,"tagList":"[]","topic":"%s"}' % (
        nick, msgId, topic)
    print(data)
    v = "1.0"
    api = "mtop.taobao.powermsg.msg.sendmsg"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, sid=sid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


def getliveinfovobysellerid(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"detail_v":"3.3.2","sellerId":"1612710529","type":"online"}'
    print(data)
    v = "1.0"
    api = "mtop.mediaplatform.live.getliveinfovobysellerid"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, sid=sid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def getdynservice(sign_server, uid, sid, utdid, deviceId, cookie_str):
    data = r'{"detail_v":"3.3.2","from":"recCube","itemId":"568498834282"}'
    print(data)
    v = "1.0"
    api = "mtop.taobao.detail.getdynservice"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, sid=sid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def report(sign_server, uid, sid, utdid, deviceId, cookie_str, topic):
    nowtime = int(time.time()) * 1000
    data = r'{"biztag":"tb","messageid":"0e23e60e6f6a7b83eaa54a0e6f5f6cde","namespace":0,"presubtype":0,"sdkversion":"0.3.0","source":0,"subtype":504,"timestamp":1588667824964,"topic":"%s"}' % topic
    v = "1.0"
    api = "mtop.taobao.powermsg.report.report"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def amp_sync(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"accountType":"3","dataTypeIdMap":"{\"imba_relation\":0,\"imbaCmd\":0,\"imba\":7,\"tao_friend\":0,\"imGroupEvent\":0,\"imMsg\":0,\"imCmd\":0}","fetchSize":"30","namespace":"0","sdkVersion":"1","source":"0"}'
    v = "1.0"
    api = "mtop.com.taobao.wireless.amp.sync"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='POST')


# 通过旺旺id获取旺旺信息
def getbatchampuserinfoforim(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"channel":"1","targetUserIdMapJson":"{\"11001\":[\"2201232865993\"]}"}'
    v = "3.0"
    api = "mtop.amp.ampservice.getbatchampuserinfoforim"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='POST')


def entry(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"accountId":"1612710529","liveId":"267626800723"} '
    v = "1.0"
    api = "mtop.mediaplatform.livedetail.entry"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def checksubscription(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"namespace":"1","sdkVersion":"12","topic":"2f1ebe20-8b48-4d74-a24d-effa9b84433b"}'
    v = "1.0"
    api = "mtop.taobao.powermsg.msg.checksubscription"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


# 发送弹幕
def comment_publish(sign_server, uid, sid, utdid, deviceId, cookie_str, topic):
    nowtime = int(time.time()) * 1000
    data = r'{"content":"我来了咯","topic":"%s","renders":"{\"fanLevel\":\"5\"}"} ' % topic
    v = "1.0"
    api = "mtop.taobao.iliad.comment.publish"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


# 直播间提示关注主播（苹果机可以看到）
def comment_publish2(sign_server, uid, sid, utdid, deviceId, cookie_str, topic):
    nowtime = int(time.time()) * 1000
    data = r'{"content":"⁂∰⏇follow","topic":"%s","os":"ios"} ' % topic
    v = "1.0"
    api = "mtop.taobao.iliad.comment.publish"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


#
# def test_follow(sign_server, utdid, deviceId, cookie_str, sid):
#     timestamp = time.time()
#     data = r'{"scopeId":"970","subScope":"1612710529_1_274506627780","action":"follow","params":"{\"accountId\":\"1612710529\"}","trackParams":"{\"activityId\":\"274506627780\",\"broadcasterId\":\"1612710529\",\"userId\":\"90434288\"}"}'
#
#     v = "1.0"
#     api = "mtop.taobao.iliad.task.action"
#     pageName = ""
#     pageId = ""
#
#     call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
#                 pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')
#

def change_user(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"force":"false","gender":"0","snsNick":"思恋需要时间88888"}'
    v = "1.0"
    api = "mtop.taobao.cus.tb.user.update"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def anniversary_ranklist(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"activityId":"212","broadcasterId":"3957261314","cycleDate":"2020060114","cycleType":"30","daySeq":"2000","n":"49","requireData":"0","s":"0","type":"1"} '
    v = "1.0"
    api = "mtop.taobao.live.anniversary.ranklist.get"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def ranklist_fans(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"broadcasterId":"1612710529"}'
    v = "1.0"
    api = "mtop.taobao.live.anniversary.ranklist.fans.get"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def follow_detail(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"followedId":"1921624371","type":"1"} '
    v = "3.0"
    api = "mtop.cybertron.follow.detail"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def ack_upload(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"sdkversion":"0.3.0","data":"[{\"uploadTime\":%s,\"source\":1,\"time\":%s,\"code\":1000,\"serverTime\":%s,\"platform\":1,\"mark\":0,\"bizTag\":\"tb\",\"key\":612793206450984,\"mode\":5,\"bizCode\":1,\"id\":\"2cdt1KH0cxwLy8am\",\"mtopTime\":%s,\"topic\":\"de8fcbed-94ee-4e32-bf1b-7a97b3d54df6\",\"type\":1,\"taskId\":\"mass-reset@@34OZlOR0cSZijCMD@@powermsg@de8fcbed-94ee-4e32-bf1b-7a97b3d54df6_tb@@false\"},{\"uploadTime\":%s,\"source\":1,\"time\":%s,\"code\":1000,\"serverTime\":%s,\"platform\":1,\"mark\":0,\"bizTag\":\"tb\",\"key\":612794152490192,\"mode\":5,\"bizCode\":1,\"id\":\"2cdt2ef0cwzMFknA\",\"mtopTime\":%s,\"topic\":\"de8fcbed-94ee-4e32-bf1b-7a97b3d54df6\",\"type\":1,\"taskId\":\"mass-reset@@34OZm4Z0cSZijCMS@@powermsg@de8fcbed-94ee-4e32-bf1b-7a97b3d54df6_tb@@false\"},{\"uploadTime\":%s,\"source\":1,\"time\":%s,\"code\":1000,\"serverTime\":%s,\"platform\":1,\"mark\":0,\"bizTag\":\"tb\",\"key\":612795130667276,\"mode\":5,\"bizCode\":1,\"id\":\"2cdt2gS0cSZijr0x\",\"mtopTime\":%s,\"topic\":\"de8fcbed-94ee-4e32-bf1b-7a97b3d54df6\",\"type\":1,\"taskId\":\"mass-reset@@34OZml60cSZijCNc@@powermsg@de8fcbed-94ee-4e32-bf1b-7a97b3d54df6_tb@@false\"}]"}' % (
        nowtime, nowtime, nowtime, nowtime, nowtime, nowtime, nowtime, nowtime, nowtime, nowtime, nowtime, nowtime)
    v = "1.0"
    api = "mtop.taobao.powermsg.monitor.ack.upload"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='POST')


def livedetail_messinfo(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"n":"0","s":"0","serviceVersion":"5.0","PARCELABLE_WRITE_RETURN_VALUE":"1","CREATOR":"{}","creatorId":"1612710529","liveId":"277380438972","type":"sponsor,timerInteractive4NeoProtocol,broadcasterScore,activity,liveHeadBanner,visitorIdentity,hasLive","CONTENTS_FILE_DESCRIPTOR":"1"}'
    v = "2.0"
    api = "mtop.mediaplatform.livedetail.messinfo"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


def anchor_accountid(sign_server, uid, sid, utdid, deviceId, cookie_str, accountId):
    data = '{"offline":"false","online":"true","pre":"false","sellerId":"%s"}' % accountId
    v = "4.0"
    api = "mtop.mediaplatform.live.getshopliveinfolist"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False)


def get_card(sign_server, uid, sid, utdid, deviceId, cookie_str, accountId, liveId):
    nowtime = int(time.time()) * 1000
    data = r'{"anchorId":"%s","liveId":"%s"}' % (accountId, liveId)
    v = "1.0"
    api = "mtop.mediaplatform.anchor.info.card"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


# 获取主播信息
def accountId_get_data(sign_server, uid, sid, utdid, deviceId, cookie_str, accountId):
    data = r'{"broadcasterId":"%s","start":"0","limit":"10"}' % accountId
    v = "1.0"
    api = "mtop.mediaplatform.anchor.info"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False)


# app分享商品生成淘口令
def get_tkl(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"expireTime":"0","password":"","title":"2020夏新款宽松显瘦圆领黑色中长款短袖T恤裙女开叉过膝T恤连衣裙","templateId":"item","passwordType":"copy","extendInfo":"{\"price\":\"79\"}","picUrl":"http://img.alicdn.com/imgextra/i4/1875230540/O1CN01ZIZWlI1FrMT6teUuM_!!1875230540.jpg","target":"copy","targetUrl":"https://a.m.taobao.com/i615928467419.htm?price=79&original_price=158&sourceType=item&sourceType=item&suid=b8248fbd-fbac-4ae4-980e-3c52eab1c051&shareUniqueId=1714072898&ut_sk=1.XwlB91CAzcADAAztOtJh7u%2Ft_21646297_1594445260146.Copy.1","popType":"","sourceType":"item","bizId":"1"}'
    v = "1.0"
    api = "mtop.taobao.sharepassword.genpassword"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='POST')


# app解析淘口令
def querypassword_tkl(sign_server, uid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"passwordContent":"覆置本段内容$RVbq1BnL1iZ$到淘tao寳或掂击炼接https://m.tb.cn/h.VruRhzp?sm=d4051b 至瀏lan嘂..【新款格纹棉质系腰衬衫式连衣裙 女款收腰中长款卡其格子连衣长裙】"} '
    v = "1.0"
    api = "mtop.taobao.sharepassword.querypassword"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=False, method='GET')


# app分享直播间生成淘口令
def live_get_tkl(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    origin_data = r'taobaozhibo|{"account_id":"1612710529","app_key":"21646297","feed_id":"274186971625","os":"android"}'
    urft_origin_data = quote_plus(origin_data)
    data = r'{"expireTime":"0","password":"","title":"户外彪客的直播间简直太火爆了，快来看！\n11111","templateId":"common","passwordType":"copy","extendInfo":"{\"bottomLogo\":\"\",\"bottomText\":\"\",\"descriptionImage\":\"\",\"isCallClient\":\"0\",\"title\":\"11111\",\"topLogo\":\"\",\"topTitle\":\"户外彪客\"}","picUrl":"http://gw.alicdn.com/tfscom/i3/O1CN010aktLo1FmK8FCKWzU_!!0-dgshop.jpg","target":"copy","targetUrl":"http://huodong.m.taobao.com/act/talent/live.html?id=274186971625&type=508&livesource=share&cp_origin=' + urft_origin_data + '","popType":"","sourceType":"talent","bizId":"zhibo"}'
    v = "1.0"
    api = "mtop.taobao.sharepassword.genpassword"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='POST')


def querypassword_tkl(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"longUrl":"http://huodong.m.taobao.com/act/talent/live.html?id=277380438972&type=508&livesource=share&cp_origin=taobaozhibo%7Ca2141.8001249%7C%7B%22account_id%22%3A%221612710529%22%2C%22app_key%22%3A%2221646297%22%2C%22feed_id%22%3A%22277380438972%22%2C%22os%22%3A%22android%22%2C%22spm-cnt%22%3A%22a2141.8001249%22%7D&sourceType=talent&suid=7544d8cf-5e94-4596-b33d-c65245191e9a&ut_sk=1.XV69DmXtfpwDAMvWbJZim1pq_21646297_1598492763236.Copy.zhibo&un=6292614812087b623431ceaac3991f67&share_crt_v=1&spm=a2159r.13376460.0.0&sp_tk=MG9IZWMyd2pyc1A=&bxsign=tcd159849280716290560faa83d8d185ed68a4728e7dbba3&ut_sk=1.XV69DmXtfpwDAMvWbJZim1pq_21646297_1598492763236.Copy.zhibo&s_share_url=http%253A%252F%252Fhuodong.m.taobao.com%252Fact%252Ftalent%252Flive.html%253Fid%253D277380438972%2526type%253D508%2526livesource%253Dshare%2526cp_origin%253Dtaobaozhibo%25257Ca2141.8001249%25257C%25257B%252522account_id%252522%25253A%2525221612710529%252522%25252C%252522app_key%252522%25253A%25252221646297%252522%25252C%252522feed_id%252522%25253A%252522277380438972%252522%25252C%252522os%252522%25253A%252522android%252522%25252C%252522spm-cnt%252522%25253A%252522a2141.8001249%252522%25257D%2526sourceType%253Dtalent%2526suid%253D7544d8cf-5e94-4596-b33d-c65245191e9a%2526ut_sk%253D1.XV69DmXtfpwDAMvWbJZim1pq_21646297_1598492763236.Copy.zhibo%2526un%253D6292614812087b623431ceaac3991f67%2526share_crt_v%253D1%2526spm%253Da2159r.13376460.0.0%2526sp_tk%253DMG9IZWMyd2pyc1A%253D%2526bxsign%253Dtcd159849280716290560faa83d8d185ed68a4728e7dbba3"} '
    v = "1.0"
    api = "mtop.com.taobao.relation.shareback"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


# 获取直播间信息
def livedetail(sign_server, uid, sid, utdid, deviceId, cookie_str, liveId):
    nowtime = int(time.time()) * 1000
    data = r'{"isDuke":"true","liveId":"%s"}' % liveId
    v = "3.0"
    api = "mtop.mediaplatform.live.livedetail"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


# 获取直播间信息,将版本号v改为1.0版相对不会频繁
def livedetail4(sign_server, uid, sid, utdid, deviceId, cookie_str, liveId):
    nowtime = int(time.time()) * 1000
    data = r'{"ignoreH265":"false","liveId":"%s"}' % liveId
    v = "4.0"
    api = "mtop.mediaplatform.live.livedetail"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, utdid=utdid, sid=sid, uid=uid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


# 获取直播间信息,可以获取下播后的观看和点赞
def livedetail_pre(sign_server, uid, utdid, deviceId, cookie_str, liveId):
    nowtime = int(time.time()) * 1000
    data = r'{"feedId":"%s"}' % liveId
    v = "2.0"
    api = "mtop.mediaplatform.live.pre.get"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=False, method='GET')


def personal_homepage(sign_server, uid, sid, utdid, deviceId, cookie_str, accountId):
    nowtime = int(time.time()) * 1000
    data = r'{"source":"taolive","type":"h5","userId":"%s","page":1,"pageSize":12,"identity":""}' % accountId
    v = "1.0"
    api = "mtop.taobao.maserati.personal.homepage"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, utdid=utdid, deviceId=deviceId, sid=sid, uid=sid, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


def pv_uv_end(sign_server, uid, sid, utdid, deviceId, cookie_str, topic):
    nowtime = int(time.time()) * 1000
    data = r'{"topic":"%s","sdkversion":"H5_0.0.0"}' % topic
    v = "1.0"
    api = "mtop.taobao.powermsg.h5.msg.pulltopicstat"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, sid=sid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


# 获取直播间商品信息
def livedetail_itemlist(sign_server, uid, utdid, deviceId, cookie_str, liveId):
    nowtime = int(time.time()) * 1000
    data = r'{"groupNum":"0","liveId":"%s","n":"350","type":"0"} ' % liveId
    v = "1.0"
    api = "mtop.mediaplatform.video.livedetail.itemlist.withpaginationv5"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=False, method='GET')


# 获取视频播放地址
def playUrl(sign_server, uid, utdid, deviceId, cookie_str):
    data = r'{"topic":"492f4c4f-123c-41da-aa54-c86421301b67"}'
    v = "1.0"
    api = "mtop.mediaplatform.live.playurls"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=False, method='GET')


# 获取推荐主播数据
def web_videolist(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{}'
    v = "2.0"
    api = "mtop.mediaplatform.live.videolist"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


# 获取推荐主播数据
def getshopliveinfo(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"sellerId":914064904}'
    v = "1.0"
    api = "mtop.mediaplatform.live.getshopliveinfo"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=True, method='GET')


# 获取直播间pv、uv、在线、点赞
def pulltopicstat(sign_server, uid, sid, utdid, deviceId, cookie_str, topic):
    # data = "{\"q\":\"" + q + "\",\"broadCasterPageNum\":\"0\",\"livePageSize\":\"10\",\"broadCasterPageSize\":\"50\",\"livePageNum\":\"0\",\"viewversion\":\"2.0\"}"
    data = '{"topic":"%s","sdkversion":"H5_0.0.0"}' % topic
    v = "1.0"
    # api = "mtop.mediaplatform.live.pulltopicstat"
    api = "mtop.taobao.powermsg.msg.pulltopicstat"
    call_gw_api(sign_server, api, v, data, utdid=utdid, uid=uid, sid=sid, deviceId=deviceId, Cookie=cookie_str,
                use_cookie=False, method='GET')


def zhongkongtai_livedata(sign_server, uid, sid, utdid, deviceId, cookie_str, topic):
    data = r'{"param":"{\"queryId\":\"1|25081173|undefined\",\"cubeId\":\"tblive_rpt_abstract_indicator\",\"queryDetail\":false,\"startTime\":\"2020-08-20 13:49:19\",\"endTime\":\"2020-09-19 13:49:19\",\"timeType\":2,\"sign\":null,\"limit\":1,\"row\":\"[]\",\"measure\":\"[{\\\"name\\\":\\\"观看次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"额外奖励流量\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"计算平均在线时长\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导进店次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"新增粉丝数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"PM观看次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"PM在线人数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"计算封面图点击率\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"直播间浏览次数_粉丝占比\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导进店次数_粉丝占比\\\",\\\"isMeasure\\\":true}]\",\"column\":\"[]\",\"orders\":\"[]\",\"filter\":\"[{\\\"name\\\":\\\"开播日期分区字段yyyymmdd\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"20200820\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"直播间id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"276625058401\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"主播id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[1612710529],\\\"oper\\\":\\\"=\\\"}]\",\"extra\":null}","innerId":""}'
    v = "1.0"
    api = "mtop.alibaba.iic.xinsightshop.olap.query"
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, Cookie=cookie_str,
                use_cookie=False, method='GET')


# 获取推流地址和秘钥
def check_info(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"liveId":"275988573506"}'
    v = "1.0"
    api = "mtop.mediaplatform.live.check.info"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


# 获取推流地址和秘钥
def tabmenu(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"contentId":"588298943528_1","channelId":"0","lbsJson":"","selectedChnlId":"0","deviceLevel":"3","version":"4","menuType":"videoMenuV2","subContentId":"591061671430_1"} '
    v = "2.0"
    api = "mtop.mediaplatform.live.tabmenu"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


# 搜索店铺
def search_appshop(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"LBS":"{\"SG_TMCS_1H_DS\":\"{\\\"stores\\\":[]}\",\"SG_TMCS_FRESH_MARKET\":\"{\\\"stores\\\":[]}\",\"TB\":\"{\\\"stores\\\":[]}\",\"TMALL_MARKET_B2C\":\"{}\",\"TMALL_MARKET_O2O\":\"{}\"}","apptimestamp":"1595214817","areaCode":"CN","brand":"OnePlus","canP4pVideoPlay":"true","countryNum":"156","device":"OnePlus5T","editionCode":"CN","from":"nt_history","homePageVersion":"v64","imei":"866550396953177","imsi":"39897OnePlu4943","info":"wifi","isBeta":"false","n":"10","network":"wifi","page":"1","pvFeature":"561837524071;562217798988;620899975574;613771433303","q":"阿玛尼","rainbow":"12885,14325,14394,13978,14239,14478,14154","search_action":"initiative","sort":"common","style":"list","sversion":"9.8","tab":"shop","ttid":"231200@taobao_android_9.9.1","utd_id":"XwlB91CAzcADAAztOtJh7u/t","vm":"nw"}'
    v = "1.0"
    api = "mtop.taobao.wsearch.appsearch"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=False, method='GET')


# 首页类目搜索
def search_Categorynew(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"LBS":"{\"SG_TMCS_1H_DS\":\"{\\\"stores\\\":[]}\",\"SG_TMCS_FRESH_MARKET\":\"{\\\"stores\\\":[]}\",\"TB\":\"{\\\"stores\\\":[]}\",\"TMALL_MARKET_B2C\":\"{}\",\"TMALL_MARKET_O2O\":\"{}\"}","active_bd":"1","apptimestamp":"1595320983","areaCode":"CN","brand":"OnePlus","canP4pVideoPlay":"true","countryNum":"156","device":"OnePlus 5T","editionCode":"CN","from":"Categorynew","homePageVersion":"v64","imei":"866550396953177","imsi":"39897OnePlu4943","info":"wifi","isBeta":"false","n":"10","network":"wifi","page":"1","pvFeature":"603864237359;619103360407;588719191859;605699905543;596000814831","q":"方便面","rainbow":"12885,14325,14394,13978,14239,14478,14154","style":"list","sversion":"9.8","tab":"shop","ttid":"231200@taobao_android_9.9.1","utd_id":"XwlB91CAzcADAAztOtJh7u/t","vm":"nw"}'
    v = "1.0"
    api = "mtop.taobao.wsearch.appsearch"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=False, method='GET')


# 首页搜索记录
def wirelessrecommend(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"appId":"10211","params":"{\"URL_REFERER_ORIGIN\":\"https://s.m.taobao.com/h5entry?utparam=%7B%22ranger_buckets_native%22%3A%22tsp2189_23049_newuser01%22%7D&spm=a2141.1.searchbar.searchbox&scm=1007.home_topbar.searchbox.d&_navigation_params=%7B%22needdismiss%22%3A%220%22%2C%22animated%22%3A%220%22%2C%22needpoptoroot%22%3A%220%22%7D\",\"_input_charset\":\"UTF8\",\"_navigation_params\":\"{\\\"needdismiss\\\":\\\"0\\\",\\\"animated\\\":\\\"0\\\",\\\"needpoptoroot\\\":\\\"0\\\"}\",\"_output_charset\":\"UTF8\",\"ad_type\":\"1.0\",\"nick\":\"苦涩终\",\"userId\":\"1002780897\",\"area\":\"active_page\",\"code\":\"utf-8\",\"editionCode\":\"CN\",\"isBeta\":\"false\",\"placeholder\":\"\",\"q\":\"\",\"referrer\":\"http://m.taobao.com/index.htm\",\"scm\":\"1007.home_topbar.searchbox.d\",\"searchdoorFrom\":\"homepage\",\"searchhint\":\"on\",\"searchquery\":\"\",\"spm\":\"a2141.1.searchbar.searchbox\",\"src\":\"c2c\",\"sversion\":\"9.8\",\"tab\":\"all\",\"ttid\":\"231200@taobao_android_9.9.1\",\"utd_id\":\"XwlB91CAzcADAAztOtJh7u/t\",\"utparam\":\"{\\\"ranger_buckets_native\\\":\\\"tsp2189_23049_newuser01\\\"}\"}"}'
    v = "2.0"
    api = "mtop.relationrecommend.wirelessrecommend.recommend"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=False, method='GET')


# 获取淘宝app首页分类及对应的二级类
def app_index_class(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"appId":"14658","params":"{\"area\":\"shouye_classifier\",\"type\":\"industry_detail\",\"industry_id\":\"6\",\"catmap_version\":\"3.0\",\"sversion\":\"\"}"} '
    v = "2.0"
    api = "mtop.relationrecommend.wirelessrecommend.recommend"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=False, method='GET')


def search_highway(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"version":1,"eventName":"behavior.expose.Page_SearchItemList.Search-ItemExposure.old","reason":"BXBatch_PageLeave","eventId":1,"events":"[{\"time\":1595323369509,\"content\":{\"userId\":\"1612710529\",\"seqId\":2694,\"isFirstEnter\":1,\"toScene\":\"\",\"reserve2\":\"bx\",\"sessionId\":\"\",\"actionArgs\":\"{\\\"exposeDuration\\\":1,\\\"exposeEndTime\\\":1595323369509,\\\"exposeStartOffsetX\\\":1,\\\"exposeStartOffsetY\\\":1,\\\"exposeStartTime\\\":1595323369509}\",\"fromScene\":\"\",\"updateTime\":1595323369509,\"createTime\":1595323369509,\"actionDuration\":0,\"actionName\":\"Search-ItemExposure\",\"actionType\":\"expose\",\"bizArgs\":\"item_id=603864237359,sessionid=,pos=0,pagePos=0,rn=,utLogMap={\\\"item_price\\\":\\\"15.90\\\",\\\"list_param\\\":\\\"方便面_75_c6072c7f2ea7072ea853f32c94a282dc\\\",\\\"srp_pos\\\":\\\"0\\\",\\\"srp_seq\\\":\\\"1\\\",\\\"x_ad\\\":\\\"1\\\",\\\"x_object_id\\\":\\\"603864237359\\\",\\\"x_object_type\\\":\\\"item\\\",\\\"x_object_type_search\\\":\\\"item\\\"},pageSize=13,spm=a2141.7631557.itemlist.0,pvid=,q=方便面,page=1,business=all\",\"bizId\":\"603864237359\",\"scene\":\"Page_SearchItemList\"}}]","count":5,"timestamp":1595323369509}'
    v = "1.0"
    api = "mtop.taobao.search.highway.upload"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, utdid=utdid, deviceId=deviceId, pageName=pageName, pageId=pageId,
                Cookie=cookie_str, use_cookie=False, method='POST')


def get_live_sold(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"param":"{\"queryId\":\"1|66464289|undefined\",\"cubeId\":\"tblive_rpt_abstract_indicator\",\"queryDetail\":false,\"startTime\":\"2020-07-31 20:37:01\",\"endTime\":\"2020-08-30 20:37:01\",\"timeType\":2,\"sign\":null,\"limit\":1,\"row\":\"[]\",\"measure\":\"[{\\\"name\\\":\\\"观看次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"额外奖励流量\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"计算平均在线时长\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导进店次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"新增粉丝数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"PM观看次数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"PM在线人数\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"计算封面图点击率\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"直播间浏览次数_粉丝占比\\\",\\\"isMeasure\\\":true},{\\\"name\\\":\\\"引导进店次数_粉丝占比\\\",\\\"isMeasure\\\":true}]\",\"column\":\"[]\",\"orders\":\"[]\",\"filter\":\"[{\\\"name\\\":\\\"开播日期分区字段yyyymmdd\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"20200731\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"直播间id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[\\\"273541940277\\\"],\\\"oper\\\":\\\"=\\\"},{\\\"name\\\":\\\"主播id\\\",\\\"type\\\":\\\"dimension\\\",\\\"isMeasure\\\":false,\\\"values\\\":[1612710529],\\\"oper\\\":\\\"=\\\"}]\",\"extra\":null,\"sdkversion\":\"H5_0.0.0\"}","innerId":""}'
    v = "1.0"
    api = "mtop.alibaba.iic.xinsightshop.olap.query"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


def nologin(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"params":"{\"tabId\":1172,\"iconChangeAllowed\":true,\"lastTimestamp\":0,\"tabHashCode\":1954708175,\"microVersion\":2}","entityId":"1185"}'
    v = "1.0"
    api = "mtop.cogman.redpoint.nologin"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


def dynamicmsg(sign_server, uid, sid, utdid, deviceId, cookie_str):
    nowtime = int(time.time()) * 1000
    data = r'{"avatar":"1185","content":"11224","dynamic_msg_type":"coming","login_id":"424550648","nick":"泽屏君","topic":"ff011ad8-ddf0-41b4-aae7-203392b3e986"}'
    v = "1.0"
    api = "taobao.live.dynamicmsg.publish"
    pageName = ""
    pageId = ""
    call_gw_api(sign_server, api, v, data, uid=uid, sid=sid, utdid=utdid, deviceId=deviceId, pageName=pageName,
                pageId=pageId, Cookie=cookie_str, use_cookie=False, method='GET')


def get_account():
    conn = pymysql.connect(host='192.168.1.105', user='root', passwd='5560203@wstSpider!', db='taobao_live',
                           charset='utf8mb4')
    cursor = conn.cursor()

    sql = "select accountId,accountName  from source_taobao_live_detail_basic where accountId>0 and accountName!='' limit 100"
    # sql = "select  accountId,accountName from source_taobao_live_basic_anchor_wangwang where accountId= 72126688 "
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data


def get_topic():
    conn = pymysql.connect(host='192.168.1.105', user='root', passwd='5560203@wstSpider!', db='taobao_live',
                           charset='utf8mb4')
    cursor = conn.cursor()

    sql = "select b.accountId,b.topic from (select accountId,liveId from  source_taobao_live_detail_basic where `status`=0)as a join (select accountId,liveId,topic from zhibo_fenlei_20200427 where channelId=29  GROUP BY liveId) as b on a.liveId=b.liveId limit 100"
    # sql = "select  accountId,accountName from source_taobao_live_basic_anchor_wangwang where accountId= 72126688 "
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data


# def process_start(shop_list,sign_server, uid, sid, utdid, deviceId, cookie_str):
#     process = []
#     process_num = 20
#     print('将会启动进程数为:', process_num)
#     for i in shop_list:
#         print('启动进程'.center(100, '='))
#         p = multiprocessing.Process(target=seller_shopId,args=(i,sign_server, uid, sid, utdid, deviceId, cookie_str))  ##创建进程
#         p.start()  ##启动进程
#         process.append(p)  ##添加进进程队列
#     for p in process:
#         p.join()  ##等待进程队列里面的进程结束
#         print("开始end进程")

def process_start(shop_list, sign_server, uid, sid, utdid, deviceId, cookie_str):
    process = []
    print("启动的进程数 %s")
    for i in shop_list:
        # print(i)
        print("启动进程")
        p = multiprocessing.Process(target=seller_shopId, args=(i, sign_server, uid, sid, utdid, deviceId, cookie_str))
        p.start()
        process.append(p)  # 添加进进程队列
    for p in process:
        p.join()  # 等待进程队列里面的进程结束
        print("开始end进程")


def seller_shopId(shop_list, sign_server, uid, sid, utdid, deviceId, cookie_str):
    for i in shop_list:
        get_shop_data(i[1], i[0], sign_server, uid, sid, utdid, deviceId, cookie_str)


def get_shops():
    conn1 = pymysql.connect(host='192.168.1.101', user='root', passwd='5560203@wstSpider!', db='taobao_live',
                            charset='utf8mb4')
    cursor = conn1.cursor()
    # sql1 = 'select a.userId,a.shopId from (select userId,shopId from  source_taobao_goods_shopinfo where shopId>0)as a left join taobao_shop_phone as b on a.userId=b.sellerId and a.shopId=b.shopId where b.sellerId is null and b.shopId is null limit 10; '
    sql1 = 'select a.userId,a.shopId from (select userId,shopId from  source_taobao_goods_shopinfo where shopId>0)as a left join taobao_shop_phone as b on a.userId=b.sellerId and a.shopId=b.shopId where b.sellerId is null and b.shopId is null limit 100'
    cursor.execute(sql1)
    data = cursor.fetchall()
    shopID = list(data)
    cursor.close()
    conn1.close()
    return shopID


def write_mysql101(param):
    start_time = time.time()
    print("开始装入总数据%s" % start_time)
    db = pymysql.connect(host='192.168.1.101', user='root', passwd='5560203@wstSpider!', db='taobao_live',
                         charset='utf8mb4')
    cursor = db.cursor()
    insert_sql = "replace into taobao_shop_phone values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(insert_sql, param)
    db.commit()
    cursor.close()
    db.close()
    end_time = time.time()
    spend_time = end_time - start_time
    print('装入总数据花费%s时间' % spend_time)
    print("装入完成")


def process_start2(list_pingjun):
    process = []
    # num_cpus = multiprocessing.cpu_count()
    # print('将会启动进程数为：', num_cpus)
    print('将会启动进程数为：4')
    for j in list_pingjun:
        print('启动进程'.center(100, '='))
        p = multiprocessing.Process(target=get_search_result, args=(j,))  ##创建进程
        p.start()  ##启动进程
        process.append(p)  ##添加进进程队列
    for p in process:
        p.join()  ##等待进程队列里面的进程结束
        print("开始end进程")


def get_search_result(list_anchor):
    for j in list_anchor:
        accountId = j[0]
        accountName = j[1]
        # print(accountId,accountName)
        sign_server = "http://106.52.5.238:6778/xsign"
        uc_server = "http://106.52.5.238:6778/xsign"
        user = get_curr_user(uc_server)
        uid = ''
        utdid = 'XpF17gMK9P0DAM5H9D8NAKDU'
        deviceId = 'AprSoaZCDG9Gmo4eXKiHQY0VfNkj-rL1k--_4CcoNq1m'
        sid = '1494e00e826a035c25a5a8d7c3fd5811'

        # cookie_str = 'enc=guhlO4KLS77qxXvEV7LYM5tsqtSQGFUaTbnDrglo5WUw0d5gORwvh4Gtd3f7htKWkUPWNUpVbSkQB5eTRBCWLw%3D%3D; unb=63833443; sn=; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dBxGR2VtGKSDfC0eg%3D&id2=VWw42fHe%2FWM%3D&nk2=1upcYIYr4zYplg%3D%3D; uc1=cookie21=W5iHLLyFfoaZ&cookie15=VT5L2FSpMGV7TQ%3D%3D&existShop=false&cookie14=UoTUPcljAQb1dw%3D%3D; csg=8d4155a5; lgc=%5Cu5355%5Cu773C%5Cu76AE1985; t=908f16a484aa4b5a6d0360eba80c4aeb; cookie17=VWw42fHe%2FWM%3D; dnk=%5Cu5355%5Cu773C%5Cu76AE1985; skt=4850e7628c33db1a; munb=63833443; cookie2=197f07fc4952360d4795f4f77ea0396a; uc4=id4=0%40V83wb8xPRomS%2Fjvvw74YeJz6iQ%3D%3D&nk4=0%401FtOwONtBxTW3k5MYCZXlREQFnrv; tracknick=%5Cu5355%5Cu773C%5Cu76AE1985; _cc_=Vq8l%2BKCLiw%3D%3D; ti=; sg=539; _l_g_=Ug%3D%3D; _nk_=%5Cu5355%5Cu773C%5Cu76AE1985; cookie1=UR2KPGpVv83Z7gIMTDMT3YwZJwkib4LVGguWMooEHgs%3D; _tb_token_=deeb76377e71; imewweoriw=36HDW35qnKh76W5Hr2itB70uJVpr3FlZRQbOVVZQTzs%3D; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BuXl33bJYC5HSfwWjK67r; _w_tb_nick=%E5%8D%95%E7%9C%BC%E7%9A%AE1985; ockeqeudmj=mLSDp44%3D; sgcookie=Y6lY7qOyBAYMlIZ1fHyRjeQdH5Q44tBb8l9lxJrXoTztz0cwysXcn3gRuPBPBceCHzk%3D; cna=5PQfF1xSywcCAbc9WoSGqSXW; enc=guhlO4KLS77qxXvEV7LYM5tsqtSQGFUaTbnDrglo5WUw0d5gORwvh4Gtd3f7htKWkUPWNUpVbSkQB5eTRBCWLw%3D%3D; unb=63833443; sn=; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dBxGR2VtGKSDfC0eg%3D&id2=VWw42fHe%2FWM%3D&nk2=1upcYIYr4zYplg%3D%3D; uc1=cookie21=W5iHLLyFfoaZ&cookie15=VT5L2FSpMGV7TQ%3D%3D&existShop=false&cookie14=UoTUPcljAQb1dw%3D%3D; csg=8d4155a5; lgc=%5Cu5355%5Cu773C%5Cu76AE1985; t=908f16a484aa4b5a6d0360eba80c4aeb; cookie17=VWw42fHe%2FWM%3D; dnk=%5Cu5355%5Cu773C%5Cu76AE1985; skt=4850e7628c33db1a; munb=63833443; cookie2=197f07fc4952360d4795f4f77ea0396a; uc4=id4=0%40V83wb8xPRomS%2Fjvvw74YeJz6iQ%3D%3D&nk4=0%401FtOwONtBxTW3k5MYCZXlREQFnrv; tracknick=%5Cu5355%5Cu773C%5Cu76AE1985; _cc_=Vq8l%2BKCLiw%3D%3D; ti=; sg=539; _l_g_=Ug%3D%3D; _nk_=%5Cu5355%5Cu773C%5Cu76AE1985; cookie1=UR2KPGpVv83Z7gIMTDMT3YwZJwkib4LVGguWMooEHgs%3D; _tb_token_=deeb76377e71; imewweoriw=36HDW35qnKh76W5Hr2itB70uJVpr3FlZRQbOVVZQTzs%3D; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BuXl33bJYC5HSfwWjK67r; _w_tb_nick=%E5%8D%95%E7%9C%BC%E7%9A%AE1985; ockeqeudmj=mLSDp44%3D; sgcookie=Y6lY7qOyBAYMlIZ1fHyRjeQdH5Q44tBb8l9lxJrXoTztz0cwysXcn3gRuPBPBceCHzk%3D; cna=5PQfF1xSywcCAbc9WoSGqSXW'
        cookie_str = ''
        searchdata(sign_server, uid, sid, utdid, deviceId, cookie_str, accountId, accountName)
        # time.sleep(5)


def get_userData():
    conn = pymysql.connect(host='192.168.1.112', user='root', passwd='5560203@wstSpider!', db='taobao_live',
                           charset='utf8mb4')
    cursor = conn.cursor()

    sql = "select * from (select nick,user_id  from liveid_chat_inmation_20200425_copy1 where user_id>0 and nick!=-1) as a GROUP BY a.user_id "
    # sql = "select  accountId,accountName from source_taobao_live_basic_anchor_wangwang where accountId= 72126688 "
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data


def get_topic():
    conn = pymysql.connect(host='192.168.1.114', user='root', passwd='5560203@wstSpider!', db='taobao_live',
                           charset='utf8mb4')
    cursor = conn.cursor()

    sql = "select b.topic  from source_taobao_live_detail_basic as a join zhibo_fenlei_20200714 as b on a.liveId=b.liveId where a.`status`=0 and b.accountId %20=0"
    # sql = "select  accountId,accountName from source_taobao_live_basic_anchor_wangwang where accountId= 72126688 "
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data


def get_tbNick():
    conn = pymysql.connect(host='192.168.1.114', user='root', passwd='5560203@wstSpider!', db='taobao_live',
                           charset='utf8mb4')
    cursor = conn.cursor()

    sql = "select nick  from ChatMessage20200802  where nick !=''  limit 1000 "
    # sql = "select  accountId,accountName from source_taobao_live_basic_anchor_wangwang where accountId= 72126688 "
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data


def get_time_stamp13():
    # 生成13时间戳   eg:1540281250399895
    datetime_now = datetime.datetime.now()

    # 10位，时间点相当于从UNIX TIME的纪元时间开始的当年时间编号
    date_stamp = str(int(time.mktime(datetime_now.timetuple())))

    # 3位，微秒
    data_microsecond = str("%06d" % datetime_now.microsecond)[0:3]

    date_stamp = date_stamp + data_microsecond
    return int(date_stamp)


def baesjiemi(list1):
    # res=re.findall('mtopjsonp9\((.*?)\)',list1,re.S)[0]
    json_res = json.loads(list1).get('data').get('timestampList')
    # print(json_res)
    # print(type(json_res))
    for i in json_res:
        data_ = i['data']
        jiemi(data_)
    # print(res)
    # print(type(res))


def jiemi(data_):
    print('=' * 160)
    b = re.sub('\n', '', data_, re.S)
    ab = base64.b64decode(b)
    print(ab.decode('utf-8', 'ignore'))


def getAccount():
    conn = pymysql.connect(host='192.168.10.78', user='root', passwd='5560203@wstSpider!', db='taobao_hudong',
                           charset='utf8mb4')
    cursor = conn.cursor()
    sql = "select userid,cookies from sell_account_password where cookie_status=0 ORDER BY update_time desc limit 40"
    # sql = "select  accountId,accountName from source_taobao_live_basic_anchor_wangwang where accountId= 72126688 "
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data


if __name__ == '__main__':
    sign_server = "http://106.53.51.241:6710/xsign"
    # uc_server = "http://119.45.8.57:6778/queryUser"
    # sign_server = "http://phone.wstdashuju.com:6786/xsign"
    # sign_server = "http://119.45.8.57:6778/xsign"
    # sign_server = "http://192.168.2.225:6780/xsign"
    # sign_server = "http://test3.cvc.cx/xsign"
    # uc_server = "http://106.53.51.241:2710/queryUser"
    uc_server = "http://192.168.79.60:2778/queryUser"
    user = get_curr_user(uc_server)
    print("==========================================")
    print(user)
    uid = user['result']['uid']
    sid = user['result']['sid']
    timestamp = int(time.time() * 1000)

    utdid = 'XsedXr/tux4DAJO0f4LI5rtp'
    deviceId = 'AuuhpePts38Ge8uc6EHhX1ERxa8vGUK7CPGVYDrXFuj0'
    # get_sign_dic(sign_server, payload={'username': 'dayin'})
    cookie_str = ''
    topic = "99b76cdf-d7b2-4aa8-9b25-27793d1af180"
    while True:
        shuapv2(sign_server, uid, sid, utdid, deviceId, cookie_str, topic)
