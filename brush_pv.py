import json
from root_api import gw_api
import time
from get_taobao_timestamp import get_timestamp


def brush_pv_root(topic):
    while 1:
        t = get_timestamp()
        data = json.dumps(
            {"appKey": "21646297", "ext": t, "from": "ubee", "id": "2990638377", "namespace": 1,
             "role": 3, "sdkVersion": "0.3.0", "tag": "ubee", "timestamp": t,
             "topic": topic, "utdId": "X03fKfpe1UYDAPhdFrObFmvR"})

        v = "1.0"
        api = "mtop.taobao.powermsg.msg.subscribe"
        host = "acs.m.taobao.com"
        text = gw_api(api, v, data, host)
        print(text)


def main():
    topic = "f81ea59d-d559-430d-8e93-6b793749aef3"
    brush_pv_root(topic)


if __name__ == '__main__':
    t = time.time()
    main()
    print(f"cost time {time.time() - t}s")
