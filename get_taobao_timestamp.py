from root_api import gw_api
import json


def get_timestamp():
    data = r'{}'
    d = gw_api(api="mtop.common.gettimestamp", version="*", data=data,
               host="guide-acs.m.taobao.com")
    return json.loads(d)['data']['t']


if __name__ == '__main__':
    print(get_timestamp())
