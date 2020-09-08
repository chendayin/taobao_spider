from root_api import gw_api
import numpy as np
from get_taobao_timestamp import get_timestamp
import threading


def root():
    while 1:
        t = get_timestamp()
        data = r'{"detail_v":"3.0.1","exParams":' + r'"{\"NAV_START_ACTIVITY_TIME\":\"%s\",\"NAV_TO_URL_START_TIME\":\"%s\",\"WEEX_NAV_PROCESSOR_TIME\":\"%s\",' % (
            int(t) + np.random.randint(10, 20, 1)[0], t, int(
                t) + np.random.randint(5, 10, 1)[
                0]) + r'\"ad_type\":\"1.0\",\"appReqFrom\":\"detail\",\"clientCachedTemplateKeys\":\"[{\\\"id\\\":\\\"1538383035450\\\",\\\"version\\\":\\\"121\\\"}]\",\"container_type\":\"xdetail\",\"countryCode\":\"CN\",\"cpuCore\":\"4\",\"cpuMaxHz\":\"1608000\",\"dinamic_v3\":\"true\",\"fromChannel\":\"bybtChannel\",\"id\":\"618989901327\",\"item_id\":\"618989901327\",\"latitude\":\"0\",\"longitude\":\"0\",\"nick\":\"苦涩终\",\"osVersion\":\"23\",\"phoneType\":\"Galaxy S8+\",\"soVersion\":\"2.0\",\"spm\":\"a21677.13732377/3.itemBjingxuan.d0_4\",\"spm-cnt\":\"a2141.7631564\",\"supportV7\":\"true\",\"u_channel\":\"bybtqdyh\",\"ultron2\":\"true\",\"umpChannel\":\"bybtqdyh\",\"utdid\":\"X03fKfpe1UYDAPhdFrObFmvR\"}","itemNumId":"618989901327"}'

        print(gw_api(api="mtop.taobao.detail.getdetail", version="6.0", data=data,
                     host="guide-acs.m.taobao.com"))


def main():
    jobs = [threading.Thread(target=root, args=()) for i in range(10)]
    for i in jobs:
        i.start()
    for j in jobs:
        j.join()


if __name__ == '__main__':
    main()
