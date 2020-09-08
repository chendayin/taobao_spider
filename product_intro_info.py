import json
from root_api import gw_api
import threading


def root():
    while 1:
        data = r'{"sellerId":"92688455","shopId":"57299736"}'
        cookie = 'unb=2990638377; sn=; csg=9804d66c; lgc=%5Cu5927%5Cu9690%5Cu5440; cookie17=UUGrdlH0KjV1gQ%3D%3D; dnk=%5Cu5927%5Cu9690%5Cu5440; munb=2990638377; cookie2=2ac1b16a50292d0ae159f1f4b5b8e74c; tracknick=%5Cu5927%5Cu9690%5Cu5440; ti=; sg=%E5%91%807c; _l_g_=Ug%3D%3D; _nk_=%5Cu5927%5Cu9690%5Cu5440; cookie1=B0OkwIWMiJcx6TtNXUL4CDIzYRtDy4YxMH94QKNjouE%3D; _tb_token_=38e63b844337e; sgcookie=W100MbbcZmleQ9BOUgINTNchCcIkByLsX1jrDJ95BDavR4NTXximu3BUVjCs%2F%2FZiHkAI1ZX6%2BKJaOhRrx7kbN%2BuzlL6q8l2XyuKub9B2LEhGgM8%3D; imewweoriw=3CVFNT7SA9xqOA5Qf%2FL0iKjeDWaihxzzivpPJ9OW9oE%3D; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BuVDzczIcbl%2Fj6Ts%3D; _w_tb_nick=%E5%A4%A7%E9%9A%90%E5%91%80; ockeqeudmj=vf7cWYQ%3D; cna=KM/UF0Z2fAcCAX1YvAspUitb; v=0; uc1=cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie14=UoTV5OMT8LX36A%3D%3D; uc3=id2=UUGrdlH0KjV1gQ%3D%3D&nk2=1z8jSrOc&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dCufXF3YQCj7cu6zw%3D; _cc_=VT5L2FSpdA%3D%3D; t=023e1eadde30a102f645de31eae232d7; skt=da3351ef45d6f292; uc4=nk4=0%401fDYSHGNunits%2FkFH8mBUg0%3D&id4=0%40U2OcRhVC%2BDHlXLT3oFl0JG5gdi9g; isg=BLCw7x4Zm_xt4kf6u9nKslK5inwC-ZRDCoUwWaoBfIveZVAPUglk0wZ3uWsFbkwb'
        d = gw_api(api="mtop.taobao.shop.impression.intro.get", version="1.0", data=data,
                   host="guide-acs.m.taobao.com", use_cookie=True, cookie=cookie)
        print(d)


def main():
    jobs = [threading.Thread(target=root, args=()) for i in range(5)]
    for i in jobs:
        i.start()
    for j in jobs:
        j.join()


if __name__ == '__main__':
    main()
