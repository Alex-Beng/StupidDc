import socket
import json
import threading
import cv2
import numpy as np

import sys
sys.path.append("../")
from Util.util import readjson

def send_serial():
    pass

def serial_server(sock: socket.socket):
    data = b''
    for i in range(20):
        data += sock.recv(102400)
    
    print(f'receive: {data}')
    if not data:
        sock.close()
        return
    if data == b'yes':
        print("get the stupid signal")
        send_serial()
    else:
        sock.close()


def main(cofig_file, font_cd='utf-8', cfg_cd='utf-8') -> int:
    config = readjson(cofig_file, cfg_cd)

    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # in case CTRLC

    s.bind(('0.0.0.0', config['port']))
    s.listen(socket.SOMAXCONN)
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=serial_server, args=[sock])
        t.start()

if __name__ == "__main__":
    main(
        "../config/serial_serv.json")
