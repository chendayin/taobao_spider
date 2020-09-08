import base64
import re


def base64_decode(data):
    b = re.sub('\n', '', data, re.S)
    ab = base64.b64decode(b)
    return ab.decode('utf-8', 'ignore')


if __name__ == '__main__':
    print(base64_decode('''NAkhCAFHAAokZjgxZWE1OWQtZDU1OS00MzBkLThlOTMtNmI3OTM3NDlhZWYzMhAyazR2Vk1VMGNV
ejVzdURlOJVOQgoyOTkwNjM4Mzc3EwASBHViZWUghNSv7sQuMgR1YmVlGgAIARADGhIKCjI5OTA2
MzgzNzcSBHViZWUgAQ=='''))
