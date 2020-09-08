from root_api import gw_api
from get_taobao_timestamp import get_timestamp


def get_item_list():
    # 获取淘宝联盟所有订单 去掉 tkStatus 获取所有订单，  tkStatus:3 获取已经结算的宝贝   tkStatus:13 已失效宝贝   tkStatus:12 已付款    tkStatus:14
    data = r'{"queryType":"1","tkStatus":"3"}'
    version = "1.0"
    api = "mtop.alimama.union.rpt.order.detail.report"
    host = "acs.m.taobao.com"
    sid = "211d78b97841b2893838f0c8ea331cb4"
    uid = "1612710529"
    content = gw_api(api, version, data, host, uid=uid, sid=sid)
    print(content)


def main():
    get_item_list()


if __name__ == '__main__':
    main()
