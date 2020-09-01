import json
from root_api import gw_api
import threading


def root():
    while 1:
        data = json.dumps({"appId": "10777",
                           "params": "{\"detail_v\":\"3.3.2\",\"flag\":\"true\",\"itemId\":\"577114607980\",\"sellerid\":\"92688455\",\"ttid\":\"2016@taobao_android_7.7.2\"}"})
        print(gw_api(api="mtop.relationrecommend.wirelessrecommend.recommend", version="2.0", data=data,
                     host="guide-acs.m.taobao.com"))


def main():
    jobs = [threading.Thread(target=root, args=()) for i in range(1)]
    for i in jobs:
        i.start()
    for j in jobs:
        j.join()


if __name__ == '__main__':
    main()
