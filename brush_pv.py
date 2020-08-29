import requests
import time
from urllib.parse import quote_plus
import json

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

APP_KEY = "21646297"
TT_ID = '700226%40taobao_android_9.3.0'
APP_VER = "9.3.0"
LAT = ""
LNG = ""
UTD_ID = 'XsedXr/tux4DAJO0f4LI5rtp'
DEVICE_ID = 'AuuhpePts38Ge8uc6EHhX1ERxa8vGUK7CPGVYDrXFuj0'
SIGN_SERVER = 'http://106.53.51.241:6710/xsign'


def get_cur_time(length: int = 0):
    return int(time.time() * pow(10, length))


def get_sign_dic(sign_server, payload):
    headers = {
        "content-type": "application/json;charset=utf-8"
    }
    res = requests.post(sign_server, data=json.dumps(payload), headers=headers)
    return res.json()


def pv_api(sign_server, api, v, data, page_id='', page_name='', use_cookie=False, uid='', sid='', utd_id='',
           device_id='', cookie='', features='27',
           method=''):
    disable_warnings(InsecureRequestWarning)
    if method.lower() == 'get':
        page_id = ' http%3A%2F%2Fh5.m.taobao.com%2Ftaolive%2Fvideo.html'
        page_name = 'com.taobao.tao.sku.view.MainSkuActivity'
    else:
        page_id = 'http%3A%2F%2Fs.m.taobao.com%2Fh5'
        page_name = 'com.taobao.search.sf.MainSearchResultActivity'

    pre_sign_data = {
        "uid": uid,
        "ttid": TT_ID,
        "data": quote_plus(data),
        "lng": LNG,
        "utdid": utd_id,
        "api": api,
        "lat": LAT,
        "deviceId": device_id,
        "sid": sid,
        "x-features": features,
        "v": v,
        "t": str(get_cur_time()),
        "pageName": page_name,
        "pageId": page_id
    }
    print(quote_plus(data))
    sign_dic = get_sign_dic(sign_server, pre_sign_data)
    body = "data=" + quote_plus(data)
    req_url = "https://acs.m.taobao.com/gw/{0}/{1}/".format(api, v)
    headers = {
        "x-m-biz-live-bizcode": "TAOBAO",
        "x-features": features,
        "x-sgext": sign_dic['result']['x-sgext'],
        "c-launch-info": "0,0,1588652065055,1588651952000,3",
        "x-page-name": page_name,
        "User-Agent": "MTOPSDK%2F3.1.1.7+%28Android%3B6.0.1%3BSamsung%3BGalaxy+S8%29",
        "x-ttid": quote_plus(TT_ID),
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "a-orange-q": "appKey=21646297&appVersion=9.6.1&clientAppIndexVersion=1120200504231704166&clientVersionIndexVersion=0",
        "x-region-channel": "CN",
        "x-appkey": APP_KEY,
        "x-nq": "WIFI",
        "x-mini-wua": quote_plus(sign_dic['result']['x-mini-wua']),

        "x-c-traceid": "XpF17gMK9P0DAM5H9D8NAKDU15886444930540109121941",
        "x-SLIDER-Q": "appKey%3D21646297%26ver%3D1588443286014",
        "x-app-conf-v": str(19),
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "x-bx-version": "6.4.16",
        "x-pv": "6.3",
        "x-t": str(get_cur_time()),
        "x-app-ver": APP_VER,
        "f-refer": "mtop",
        "x-nettype": "WIFI",
        "x-utdid": utd_id,
        "x-umt": quote_plus(sign_dic['result']['x-umt']),

        "x-devid": device_id,
        "x-sign": quote_plus(sign_dic['result']['x-sign']),

        "x-page-url": quote_plus(page_id),
        "x-location": quote_plus("{0},{1}".format(LNG, LAT)),
        "Host": "acs.m.taobao.com"
        # "Accept-Encoding": "gzip",
        # "Connection": "Keep-Alive",
    }
    if uid != "":
        headers["x-uid"] = uid

    if sid != "":
        headers["x-sid"] = sid
    if use_cookie:
        headers["Cookie"] = cookie

    if method == 'GET':
        req_url = (req_url + "?{0}").format(body)
        sign_dic = requests.get(req_url, headers=headers, verify=False)

    else:
        print("请求淘宝Http方式: POST")
        print("请求淘宝url:" + req_url)
        print("请求淘宝参数:" + body)

        sign_dic = requests.post(req_url, data=body, headers=headers, verify=True)

    if sign_dic.status_code == requests.codes.ok:
        print("淘宝返回:" + sign_dic.text)
        print("\n")
        return sign_dic.text
    else:
        print("淘宝失败返回代码:" + str(sign_dic.status_code))
        print("淘宝失败响应头:" + sign_dic.headers['location'])
        print("淘宝失败返回:" + sign_dic.text)


def brush_pv_root(sign_server, utd_id, device_id, cookie_str, topic):
    while 1:
        data = json.dumps({'topic': topic, 'role': '2', 'namespace': '1', 'sdkVersion': '0.3.0'})

        v = "1.0"
        api = "mtop.taobao.powermsg.msg.subscribe"
        #
        pv_api(sign_server, api, v, data, utd_id=utd_id, device_id=device_id, use_cookie=False, cookie=cookie_str,
               method="GET")


def main():
    topic = "cc383b36-d4c0-4118-b81e-c38db787a18a"
    cookie = ''
    brush_pv_root(SIGN_SERVER, UTD_ID, DEVICE_ID, cookie, topic)


if __name__ == '__main__':
    t = time.time()
    main()
    print(f"cost time {time.time() - t}s")
