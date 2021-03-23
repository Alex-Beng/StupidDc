import socket
import json
import threading
import cv2
import numpy as np

import sys
sys.path.append("../")
from Util.util import readjson


def dnn_server(sock: socket.socket):
    data = b''
    for i in range(20):
        data += sock.recv(102400)
    
    print(f'receive: {len(data)}')
    if not data:
        sock.close()
        return
    img = np.asarray(bytearray(data), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    cv2.imshow(f"ya{sock.getsockname()}", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    res = ""
    sock.send(bytes(res, encoding='utf-8'))


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
