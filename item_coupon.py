from root_api import gw_api
from utlis import *
import json
import jsonpath

US_URL = "http://106.53.51.241:2710/queryUser"


# 获取优惠券信息
def get_coupon_info(sell_id, activity_id):
    data = r'{"sellerId":"%s","uuid":"%s"}' % (sell_id, activity_id)
    version = '3.0'
    api = "mtop.taobao.couponmtopreadservice.findshopbonusactivitys"
    host = "trade-acs.m.taobao.com"
    sid, uid = get_sid_uid(US_URL)
    r = gw_api(api, version, data, host, sid=sid, uid=uid)
    d = json.loads(r)
    start_time = jsonpath.jsonpath(d, '$..startTime')[0]
    end_time = jsonpath.jsonpath(d, '$..endTime')[0]
    # 优惠券状态 -1，0表示优惠券失效，1表示优惠券有效
    status = jsonpath.jsonpath(d, '$..status')[0]
    # 优惠券类型 0表示店铺优惠券 1 表示商品优惠券
    coupon_type = jsonpath.jsonpath(d, '$..couponType')[0]
    print(d)
    coupon_price = int(jsonpath.jsonpath(d, '$..discount')[0]) // 100
    info = {'startTime': start_time, 'end_time': end_time, 'status': status, 'coupon_price': coupon_price,
            'coupon_type': coupon_type}
    return info


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


def recv_coupon(sell_id, activity_id):
    data = r'{"supplierId":"%s","uuid":"%s"}' % (sell_id, activity_id)
    version = "3.0"
    api = "mtop.taobao.buyerresourcemtopwriteservice.applycoupon"
    host = "trade-acs.m.taobao.com"
    sid, uid = get_sid_uid(US_URL)
    r = gw_api(api, version, data, host, sid=sid, uid=uid)
    d = json.loads(r)
    try:
        resource_code = jsonpath.jsonpath(d, "$..resourceCode")[0]
        return resource_code
    except:
        print("已经领取过优惠券了...")


def main():
    info = get_coupon_info("2690231046", "c33228522a0e4e1085f417ba99aab4ca")
    print(info)


if __name__ == '__main__':
    main()
