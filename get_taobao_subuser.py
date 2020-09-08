from root_api import gw_api
from get_taobao_timestamp import get_timestamp


def get_subuser():
    data = r'{"nick":"hbpenguin","page_no":"1","page_size":"100"}'
    version = "1.0"
    api = "mtop.taobao.mmp.subuser.page.get"
    host = "acs.m.taobao.com"
    sid = "16f1ffef3f2b19fd6afa50a4b27ea94a"
    uid = "2615933779"
    content = gw_api(api, version, data, host, uid=uid, sid=sid)
    print(content)


if __name__ == '__main__':
    get_subuser()
