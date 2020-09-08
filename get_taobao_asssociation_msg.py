from root_api import gw_api


def get_association():
    data = r'{"sellerNick":"hbpenguin","keywords":"D"}'
    version = "1.0"
    api = "mtop.taobao.cbinteraction.association.query"
    host = "guide-acs.m.taobao.com"
    sid = "12e61dab2cb53f14a332e98f82b4315d"
    uid = "2990638377"
    d = gw_api(api=api, version=version, data=data,
               host=host, sid=sid, uid=uid, method="GET")
    print(d)


if __name__ == '__main__':
    get_association()
