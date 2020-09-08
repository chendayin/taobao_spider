from brush_pv import *
import threading


def main():
    topic = "f81ea59d-d559-430d-8e93-6b793749aef3"
    jobs = [threading.Thread(target=brush_pv_root, args=(topic,)) for i
            in range(100)]

    for i in jobs:
        i.start()
    for j in jobs:
        j.join()


if __name__ == '__main__':
    main()
