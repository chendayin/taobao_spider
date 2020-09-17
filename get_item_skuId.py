from root_api import gw_api
from utlis import *
import json
import jsonpath

US_URL = "http://106.53.51.241:2760/queryUser"


def get_sku_id(item_id):
    data = r'{"itemNumId":"%s"}' % item_id
    version = "6.0"
    api = "mtop.taobao.detail.getdetail"
    host = "trade-acs.m.taobao.com"
    result = gw_api(api, version, data, host, method="GET")
    d = json.loads(result)
    sku_ids = jsonpath.jsonpath(d, "$..skuId")
    if sku_ids:
        return sku_ids[0]


if __name__ == '__main__':
    sku = get_sku_id("623747744327")
    print(sku)
