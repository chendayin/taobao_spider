from root_api import gw_api
from utlis import *
import json
import jsonpath

US_URL = "http://106.53.51.241:2710/queryUser"


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
    pass


if __name__ == '__main__':
    recv_coupon("3006648869", "77f4558a60554ea9b3b85b11dc0b4656")
