import json
from root_api import gw_api
import threading


def root():
    while 1:
        data = json.dumps({"targetId": "577114607980", "source": "ali.china.taobao"})
        print(gw_api(api="mtop.alibaba.rate.impressions.get", version="1.0", data=data,
                     host="guide-acs.m.taobao.com"))


def main():
    jobs = [threading.Thread(target=root, args=()) for i in range(100)]
    for i in jobs:
        i.start()
    for j in jobs:
        j.join()


if __name__ == '__main__':
    main()
