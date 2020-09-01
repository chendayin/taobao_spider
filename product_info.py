from get_taobao_timestamp import get_timestamp
from root_api import gw_api
import numpy as np


def main():
    api = "mtop.taobao.detail.getdetail"
    version = "6.0"
    host = "trade-acs.m.taobao.com"
    t = get_timestamp()
    data = r'{"detail_v":"3.1.2","exParams":' + r'"{\"NAV_START_ACTIVITY_TIME\":\"%s\",\"NAV_TO_URL_START_TIME\":\"%s\",\"WEEX_NAV_PROCESSOR_TIME\":\"%s\",' % (
        int(t) + np.random.randint(5, 20, 1)[0], t, int(
            t) + np.random.randint(5, 10, 1)[
            0]) + r'\"action\":\"ipv\",\"ad_type\":\"1.0\",\"appReqFrom\":\"detail\",\"clientCachedTemplateKeys\":\"[{\\\"id\\\":\\\"1538383035450\\\",\\\"version\\\":\\\"120\\\"},{\\\"id\\\":\\\"1558768549860\\\",\\\"version\\\":\\\"52\\\"}]\",\"container_type\":\"detail\",\"countryCode\":\"CN\",\"cpuCore\":\"4\",\"cpuMaxHz\":\"1416000\",\"detailAlgoParam\":\"%E9%9D%A2%E5%8C%85\",\"dinamic_v3\":\"true\",\"from\":\"search\",\"id\":\"584244084598\",\"item_id\":\"584244084598\",\"latitude\":\"0\",\"list_type\":\"save\",\"longitude\":\"0\",\"nick\":\"大隐呀\",\"osVersion\":\"23\",\"phoneType\":\"N7 Pro\",\"search_action\":\"search\",\"soVersion\":\"2.0\",\"spm\":\"a2141.7631557.itemlist\",\"spm-cnt\":\"a2141.7631564\",\"supportV7\":\"true\",\"ultron2\":\"true\",\"utdid\":\"Xz4kYRos5H4DAKkeoL+6HwYQ\"}","itemNumId":"584244084598"}'
    d = gw_api(api, version, data, host)
    print(d)


if __name__ == '__main__':
    main()
