from brush_pv import *
import threading


def main():
    topic = "cc383b36-d4c0-4118-b81e-c38db787a18a"
    cookie = ''
    jobs = [threading.Thread(target=brush_pv_root, args=(SIGN_SERVER, UTD_ID, DEVICE_ID, cookie, topic)) for i
            in range(100)]

    for i in jobs:
        i.start()
    for j in jobs:
        j.join()


if __name__ == '__main__':
    main()
