import json
from urllib.parse import quote, quote_plus
import hashlib
import time
import requests

# 1598928887525
# 1598924784544
t = "1598924784544"

data = {"itemNumId": "618913345252"}
ktsts = str(int(time.time() * 1000))
data_str = json.dumps(data)
sign_p = ('' + '&' + t + '&12574478&' + data_str)
loginurl = 'https://h5api.m.taobao.com/h5/mtop.mediaplatform.live.encryption/1.0/?jsv=2.4.16&appKey=12574478&t={}&sign={}&api=mtop.mediaplatform.live.encryption&v=1.0&AntiCreep=true&type=jsonp&dataType=jsonp&callback=mtopjsonp7&data={}'.format(
    ktsts, sign_p, str(data))
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
}
r = requests.get(loginurl, headers=headers, verify=False)
h5_tk = r.cookies.get("_m_h5_tk")
print(h5_tk)
sign_p = ("68034b35ee8a2028950ad240e46fe256_1598939498127" + '&' + t + '&12574478&' + data_str)
sign = hashlib.md5(sign_p.encode()).hexdigest()
print(sign)
