import time

import requests


def get_sid_uid(url):
    r = requests.get(url).json()
    uid = r['result']['uid']
    sid = r['result']['sid']
    return sid, uid


def process_time(t, fmt="%Y-%m-%d %X"):
    t = str(t)[:10]
    return time.strftime(fmt, time.localtime(int(t)))


def get_proxy():
    proxy = requests.get("http://192.168.1.115:5000/get/").json()['proxy']
    return {"http": "http://{}".format(proxy)}


def get_cookie(url):
    r = requests.get(url)
    result = r.json()
    cookie = result['result']
    return cookie


if __name__ == '__main__':
    s, u = get_sid_uid("http://192.168.79.60:2778/queryUser")
    pass
