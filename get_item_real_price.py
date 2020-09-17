from root_api import gw_api
from utlis import *
from get_item_skuId import get_sku_id
import re
import time

US_URL = "http://106.53.51.241:2779/queryUser"
C_URL = "http://192.168.79.38:2778/queryCookie"


def get_price(item_id):
    sku_id = get_sku_id(item_id)
    if sku_id:
        data = r'{"itemId":"%s","skuId":"%s"}' % (item_id, sku_id)
        version = "4.0"
        api = "mtop.trade.order.build"
        host = "trade-acs.m.taobao.com"
        sid, uid = get_sid_uid(US_URL)
        r = gw_api(api, version, data, host, uid=uid, sid=sid, method="POST")
        try:
            price = eval(re.findall(r'"orderPay_.*?"price":(.+?").*?', r)[0])
            return price
        except:
            print("----" * 10)
            print(r)
            print("----" * 10)
            print(item_id)
            print("----" * 10)
    else:
        print("该商品没有sku_id")


if __name__ == '__main__':
    t = time.time()
    p = get_price("623747744327")
    print(p)
    print(f"cost time {time.time() - t}s")
