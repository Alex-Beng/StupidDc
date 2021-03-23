import socket
import json
import threading
import cv2
import numpy as np

import sys
sys.path.append("../")
from Util.util import readjson


def dnn_server(sock: socket.socket):
    data = sock.recv(102400000)
    if not data:
        sock.close()
        return
    img = np.asarray(bytearray(data), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    cv2.imshow("ya", img)
    cv2.waitKey()
    res = ""
    sock.send(bytes(res, encoding='utf-8'))
    sock.close()


def main(cofig_file, font_cd='utf-8', cfg_cd='utf-8') -> int:
    config = readjson(cofig_file, cfg_cd)

    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # in case CTRLC

    s.bind((config['addr'], config['port']))
    s.listen(socket.SOMAXCONN)
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=dnn_server, args=[sock])
        t.start()

if __name__ == "__main__":
    main(
        "../config/pc_serv.json")
