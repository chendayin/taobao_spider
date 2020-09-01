from brush_pv import *
import threading


def main():
    topic = "99b76cdf-d7b2-4aa8-9b25-27793d1af180"
    jobs = [threading.Thread(target=brush_pv_root, args=(topic,)) for i
            in range(100)]

    for i in jobs:
        i.start()
    for j in jobs:
        j.join()


if __name__ == '__main__':
    main()
