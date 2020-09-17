from root_api import gw_api
from utlis import *
import json
import jsonpath

US_URL = "http://106.53.51.241:2710/queryUser"


# 获取店铺优惠券所有的商品页数
def get_item_list_type_0_page(sell_id):
    data = r'{"m":"couponuse","n":"100","page":"1","seller_id":"%s"}' % sell_id
    version = "1.0"
    api = "mtop.taobao.wsearch.couponuse"
    sid, uid = get_sid_uid(US_URL)
    host = "trade-acs.m.taobao.com"
    r = gw_api(api, version, data, host, sid=sid, uid=uid)
    d = json.loads(r)
    total_page = jsonpath.jsonpath(d, '$..totalPage')[0]
    return total_page


# 获取店铺优惠券所有的商品
def get_item_list_type_all(sell_id):
    page = get_item_list_type_0_page(sell_id)
    item_set = set()
    for i in range(1, int(page)):
        data = r'{"m":"couponuse","n":"100","page":"%s","seller_id":"%s"}' % (i, sell_id)
        version = "1.0"
        api = "mtop.taobao.wsearch.couponuse"
        sid, uid = get_sid_uid(US_URL)
        host = "trade-acs.m.taobao.com"
        r = gw_api(api, version, data, host, sid=sid, uid=uid)
        d = json.loads(r)
        item_id = jsonpath.jsonpath(d, '$..x_item_ids')
        if item_id:
            for item in item_id:
                item_set.add(item)
    return item_set


def main():
    sell_id = "2690231046"
    items = get_item_list_type_all(sell_id)
    print(items, len(items))


if __name__ == '__main__':
    main()
