import json
from root_api import gw_api


def brush_pv_root(topic):
    while 1:
        data = json.dumps(
            {'topic': topic, 'role': '0',
             'namespace': '1',
             'sdkVersion': '0.3.0'})

        v = "1.0"
        api = "mtop.taobao.powermsg.msg.subscribe"
        host = "acs.m.taobao.com"
        text = gw_api(api, v, data, host)
        print(text)


def main():
    topic = "99b76cdf-d7b2-4aa8-9b25-27793d1af180"
    brush_pv_root(topic)


if __name__ == '__main__':
    t = time.time()
    main()
    print(f"cost time {time.time() - t}s")
