from root_api import gw_api
from get_taobao_timestamp import get_timestamp


def get_itemId():
    itemId = "15564317460"
    t = get_timestamp()
    data = r'{"nick":"大隐呀","gatewayVersion":"2.0","encryptUserId":"0%40U2OcRhVC%2BDHlXLT3oFl1M7qUqBUL","userId":"2990638377","containerParams":"{\"recommend_itemdetail_main\":{\"baseCacheTime\":' + t + r',\"bizParams\":{\"itemId\":\"' + itemId + r'\",\"latestHundredItem\":\"\",\"m\":\"detail\",\"tb_homepage_clientCache_lbs\":{\"SG_TMCS_1H_DS\":\"{\\\"stores\\\":[]}\",\"SG_TMCS_FRESH_MARKET\":\"{\\\"stores\\\":[]}\",\"TB\":\"{\\\"stores\\\":[{\\\"code\\\":\\\"185836187\\\",\\\"bizType\\\":\\\"2\\\",\\\"type\\\":\\\"1\\\"}]}\",\"TMALL_MARKET_O2O\":\"{\\\"stores\\\":[{\\\"code\\\":\\\"233930453\\\",\\\"bizType\\\":\\\"DELIVERY_TIME_ONE_HOUR\\\",\\\"addrId\\\":\\\"12207859969\\\",\\\"type\\\":\\\"CHOOSE_ADDR\\\"},{\\\"code\\\":\\\"236853011\\\",\\\"bizType\\\":\\\"DELIVERY_TIME_HALF_DAY\\\",\\\"addrId\\\":\\\"12207859969\\\",\\\"type\\\":\\\"CHOOSE_ADDR\\\"}]}\"}},\"clientReqOffsetTime\":0,\"deltaCacheTime\":0,\"pageParams\":{\"isLastPage\":\"n\",\"itemLastCount\":\"25\",\"pageNum\":1,\"requestInAdvance\":10},\"passParams\":{\"iconReplaceRecord\":\"{\\\"icon_tmall_huiyuandian\\\":{\\\"sourceItemBizCode\\\":\\\"icon_tmall_huiyuandian\\\",\\\"targetItemBizCode\\\":\\\"icon_guoji\\\",\\\"timestamp\\\":1599186203151},\\\"icon_tmallnc\\\":{\\\"sourceItemBizCode\\\":\\\"icon_tmallnc\\\",\\\"targetItemBizCode\\\":\\\"icon_waimai\\\",\\\"timestamp\\\":1599189021115}}\",\"isCategorySearch\":\"true\",\"isG9Group\":\"true\",\"lastVersion\":\"v6\",\"poiRefreshTime\":\"0\",\"searchPassParams\":\"{\\\"g_taoxianda\\\":\\\"true\\\"}\",\"txdShopId\":\"185836187\",\"whiteNavi\":\"true\"},\"realBaseCacheTime\":0,\"requestType\":\"scrollNextPage\"}}"}'
    version = "1.0"
    api = "mtop.taobao.wireless.home.awesome.itemdetail.recommend"
    host = "guide-acs.m.taobao.com"
    d = gw_api(api=api, version=version, data=data,
               host=host, method="GET")
    print(d)


if __name__ == '__main__':
    get_itemId()
