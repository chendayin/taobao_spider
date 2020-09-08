import requests

url = r'https://shop.taobao.com/getShopInfo.htm?shopId=64585238'
# data = {'_ksTS': '1599017987683_102'}

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    'cookie': 'cna=59bAF7vHb3gCAWp645dO/RM8; lgc=%5Cu5927%5Cu9690%5Cu5440; tracknick=%5Cu5927%5Cu9690%5Cu5440; thw=cn; miid=1941224392903274209; enc=HVhaw0EEXNM%2Ff8NI0f1lRuGGq3mRdBkDmue7%2B1Po4peDGquqQvj6IvkW%2Bf0DcfS4gicg44rwXeUTynjE7JdEoA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; cookie2=1e98c048d560e1f47da4e6d679f239b0; t=f2d2588bb07ac5b6a2e1f5c9c79147a9; _samesite_flag_=true; mt=ci=10_1; v=0; unb=2990638377; cookie17=UUGrdlH0KjV1gQ%3D%3D; dnk=%5Cu5927%5Cu9690%5Cu5440; _l_g_=Ug%3D%3D; sg=%E5%91%807c; _nk_=%5Cu5927%5Cu9690%5Cu5440; cookie1=B0OkwIWMiJcx6TtNXUL4CDIzYRtDy4YxMH94QKNjouE%3D; xlly_s=1; sgcookie=E100mr%2BjoCAkHhl7%2BOnqC5kClaTJOWQD5M%2FTkQpSbmk0LBYb2xHnlu5jIyZzaOcRLIIjlYbfTwHhc0sVH4SpFkTLLQ%3D%3D; uc3=nk2=1z8jSrOc&id2=UUGrdlH0KjV1gQ%3D%3D&vt3=F8dCufXGB0GeuRSu4D4%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; csg=a3d90d83; skt=aae42dd8492f6172; existShop=MTU5OTAxNTM0Nw%3D%3D; uc4=nk4=0%401fDYSHGNunits%2FjL3uchRqI%3D&id4=0%40U2OcRhVC%2BDHlXLT3oFl1N40w5YpY; _cc_=VFC%2FuZ9ajQ%3D%3D; _tb_token_=31310e3e5559d; _m_h5_tk=162e714732a87bde1751a60173e2a1bf_1599029532252; _m_h5_tk_enc=f66afac790727ef82c1e3ff81bb6edb4; uc1=cookie14=UoTV5YzfNS%2FdMA%3D%3D&pas=0&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=true; tfstk=cTkNBIZb7dpahXwXwRwVh5HfUqaOZenim9r7sjqrUfXJblVGil_YxH_YYoaJK5f..; l=eBQbjK1rOIGgKXPhXOfwourza77OSIRAguPzaNbMiOCP9w5p5cTNWZP37hY9C3GNh6JkR3-WSGYuBeYBqIvwEV8IBr9-V0Mmn; isg=BC0t-1cuDsNuCOpaid2mwD9QPMmnimFcc6BN1G8yaUQz5k2YN9pxLHuw0LIA5nkU'
}

r = requests.get(url, headers=headers)

print(r.text)
