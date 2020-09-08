from root_api import gw_api
from get_taobao_timestamp import get_timestamp


def get_user_msg():
    data = r'{"syncId":"0","messageType":"A","bizId":"0"}'
    version = "3.0"
    api = "mtop.taobao.amp.im.sync"
    host = "acs.m.taobao.com"
    sid = "16f1ffef3f2b19fd6afa50a4b27ea94a"
    uid = "2615933779"
    d = gw_api(api=api, version=version, data=data,
               host=host, sid=sid, uid=uid, method="GET")

    print(d)


def get_group_msg():
    data = r'{"syncId":"0","messageType":"G","bizId":"0"}'
    version = "3.0"
    api = "mtop.taobao.amp.im.sync"
    host = "acs.m.taobao.com"
    sid = "1032f916702f9333a315552358d6fbce"
    uid = "2615933779"
    d = gw_api(api=api, version=version, data=data,
               host=host, sid=sid, uid=uid, method="GET")

    print(d)


if __name__ == '__main__':
    get_user_msg()
    # get_group_msg()
