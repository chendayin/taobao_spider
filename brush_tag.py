import requests
import time
from urllib.parse import quote
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


def tag_api(sign_server, api, v, data, page_id='', page_name='', use_cookie=False, uid='', sid='', utd_id='',
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
        "data": quote(data),
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
    sign_dic = get_sign_dic(sign_server, pre_sign_data)
    body = "data=" + quote(data)
    req_url = "https://acs.m.taobao.com/gw/{0}/{1}/".format(api, v)
    headers = {
        "x-m-biz-live-bizcode": "TAOBAO",
        "x-features": features,
        "x-sgext": sign_dic['result']['x-sgext'],
        "c-launch-info": "0,0,1588652065055,1588651952000,3",
        "x-page-name": page_name,
        "User-Agent": "MTOPSDK%2F3.1.1.7+%28Android%3B6.0.1%3BSamsung%3BGalaxy+S8%29",
        "x-ttid": quote(TT_ID),
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "a-orange-q": "appKey=21646297&appVersion=9.6.1&clientAppIndexVersion=1120200504231704166&clientVersionIndexVersion=0",
        "x-region-channel": "CN",
        "x-appkey": APP_KEY,
        "x-nq": "WIFI",
        "x-mini-wua": quote(sign_dic['result']['x-mini-wua']),
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
        "x-umt": quote(sign_dic['result']['x-umt']),

        "x-devid": device_id,
        "x-sign": quote(sign_dic['result']['x-sign']),

        "x-page-url": quote(page_id),
        "x-location": quote("{0},{1}".format(LNG, LAT)),
        "Host": "trade-acs.m.taobao.com"
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
        print(req_url)
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
        # print("淘宝失败响应头:" + sign_dic.headers['location'])
        print("淘宝失败返回:" + sign_dic.text)


def brush_tag_root(sign_server, utd_id, device_id, cookie_str, itemId, nickname):
    # data3 = r'{"detail_v":"3.3.2","exParams":"{\"NAV_START_ACTIVITY_TIME\":\"1598961079993\",\"NAV_TO_URL_START_TIME\":\"1598961079985\",\"WEEX_NAV_PROCESSOR_TIME\":\"1598961079988\",\"action\":\"ipv\",\"ad_type\":\"1.0\",\"appReqFrom\":\"detail\",\"clientCachedTemplateKeys\":\"[{\\\"id\\\":\\\"1538383035450\\\",\\\"version\\\":\\\"121\\\"}]\",\"container_type\":\"xdetail\",\"countryCode\":\"CN\",\"cpuCore\":\"4\",\"cpuMaxHz\":\"1608000\",\"detailAlgoParam\":\"%E8%80%81%E7%88%B9%E9%9E%8B\",\"dinamic_v3\":\"true\",\"from\":\"search\",\"id\":\"576714440550\",\"item_id\":\"576714440550\",\"latitude\":\"0\",\"list_type\":\"search\",\"longitude\":\"0\",\"nick\":\"大隐呀\",\"osVersion\":\"23\",\"phoneType\":\"Galaxy S8+\",\"search_action\":\"initiative\",\"soVersion\":\"2.0\",\"spm\":\"a2141.7631557.itemlist.2\",\"spm-cnt\":\"a2141.7631564\",\"supportV7\":\"true\",\"ultron2\":\"true\",\"utdid\":\"X03fKfpe1UYDAPhdFrObFmvR\"}","itemNumId":"576714440550"}'
    # data2 = r'{"detail_v":"3.3.2","exParams":"{\"NAV_START_ACTIVITY_TIME\":\"1598960255881\",\"NAV_TO_URL_START_TIME\":\"1598960255870\",\"WEEX_NAV_PROCESSOR_TIME\":\"1598960255875\",\"action\":\"ipv\",\"ad_type\":\"1.0\",\"appReqFrom\":\"detail\",\"clientCachedTemplateKeys\":\"[{\\\"id\\\":\\\"1538383035450\\\",\\\"version\\\":\\\"121\\\"}]\",\"container_type\":\"xdetail\",\"countryCode\":\"CN\",\"cpuCore\":\"4\",\"cpuMaxHz\":\"1608000\",\"detailAlgoParam\":\"%E8%80%81%E7%88%B9%E9%9E%8B\",\"dinamic_v3\":\"true\",\"from\":\"search\",\"id\":\"577114607980\",\"item_id\":\"577114607980\",\"latitude\":\"0\",\"list_type\":\"search\",\"longitude\":\"0\",\"nick\":\"大隐呀\",\"osVersion\":\"23\",\"phoneType\":\"Galaxy S8+\",\"search_action\":\"initiative\",\"soVersion\":\"2.0\",\"spm\":\"a2141.7631557.itemlist.1\",\"spm-cnt\":\"a2141.7631564\",\"supportV7\":\"true\",\"ultron2\":\"true\",\"utdid\":\"X03fKfpe1UYDAPhdFrObFmvR\"}","itemNumId":"577114607980"}'
    data = r'{"itemNumId":"624387840009"}'
    v = "6.0"
    api = "mtop.taobao.detail.getdetail"
    #
    tag_api(sign_server, api, v, data, utd_id=utd_id, device_id=device_id, use_cookie=False, cookie=cookie_str,
            method="GET")


def main():
    itemId = ""
    nickname = ''
    cookie = ''
    brush_tag_root(SIGN_SERVER, UTD_ID, DEVICE_ID, cookie, itemId, nickname)


if __name__ == '__main__':
    t = time.time()
    main()
    print(f"cost time {time.time() - t}s")
