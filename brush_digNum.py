import json
from root_api import gw_api, get_curr_user, UC_SERVER
import time
from get_taobao_timestamp import get_timestamp


def brush_pv_root(topic):
    while 1:
        user = get_curr_user(UC_SERVER)
        uid = user['result']['uid']
        sid = user['result']['sid']
        data = json.dumps(
            {"bizCode": 1, "bizTag": "ubee", "offset": "0", "pagesize": "8", "role": "5",
             "sdkversion": "0.3.0",
             "timestamp": get_timestamp(), "topic": topic})

        v = "1.0"
        api = "mtop.taobao.powermsg.msg.pullnativemsg"
        host = "guide-acs.m.taobao.com"
        text = gw_api(api, v, data, host)
        print(text)


def main():
    topic = "f81ea59d-d559-430d-8e93-6b793749aef3"
    brush_pv_root(topic)


if __name__ == '__main__':
    t = time.time()
    main()
    print(f"cost time {time.time() - t}s")
