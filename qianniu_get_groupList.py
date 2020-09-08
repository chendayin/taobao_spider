from root_api import gw_api
from get_taobao_timestamp import get_timestamp


def get_group_list():
    # codeList 组成  由创建人的userId加上群创建时间组成
    data = r'{"ccodeList":"[\"0_G_2990638377_1599202021942\"]","bizId":"0"}'
    version = "1.0"
    api = "mtop.taobao.amp.im.group.getgroupinfolistbyccodelist"
    host = "acs.m.taobao.com"
    sid = "16f1ffef3f2b19fd6afa50a4b27ea94a"
    uid = "2615933779"
    content = gw_api(api, version, data, host, uid=uid, sid=sid, method="POST")
    print(content)


def check_userid_in_group():
    # 更改 groupUserId 能够判断用户是否再这个淘宝群中
    data = r'{"groupUserId":"2990638377","bizId":"0","ccode":"0_G_2615933779_1599124187784"}'
    version = "1.0"
    api = "mtop.taobao.amp.im.group.getgroupuserinfonotnull"
    host = "acs.m.taobao.com"
    sid = "12a565f448f9f5b42ce87de1f0148f97"
    uid = "1612710529"
    content = gw_api(api, version, data, host, uid=uid, sid=sid)
    print(content)


def get_group_info_list():
    # 获取该userid创建的群
    data = r'{"bizId":"0"}'
    version = "2.0"
    api = "mtop.taobao.amp.im.group.getgroupinfolist"
    host = "acs.m.taobao.com"
    sid = "12a565f448f9f5b42ce87de1f0148f97"
    uid = "1612710529"
    content = gw_api(api, version, data, host, uid=uid, sid=sid)
    print(content)


def main():
    # get_group_info_list()
    # get_group_list()
    check_userid_in_group()


if __name__ == '__main__':
    main()
