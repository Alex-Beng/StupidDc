import socket
import json
import threading
import cv2
import time
import numpy as np

import sys
sys.path.append("../")
from Util.util import readjson, bytes2img

def dnn_server_udp(sock: socket.socket):
    max_fps = -1
    min_fps = 999
    while True:
        begin_time = time.time()

        data, addr = sock.recvfrom(1024000)
        
        print(f'receive: {len(data)} from {addr}')

        img = bytes2img(data)
        end_time = time.time()
        fps = 1.0/(end_time-begin_time)
        cv2.putText(img, '%.2f fps'%(fps), 
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
        if fps > max_fps:
            max_fps = fps
        if fps < min_fps:
            min_fps = fps
        cv2.putText(img, 'max : %.2f'%(max_fps), 
                    (200, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0))
        cv2.putText(img, 'min : %.2f'%(min_fps), 
                    (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0))


        cv2.imshow(f"ya{sock.getsockname()}", img)
        cv2.waitKey(1)

        

        
        

def main(cofig_file, font_cd='utf-8', cfg_cd='utf-8') -> int:
    config = readjson(cofig_file, cfg_cd)

    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # in case CTRLC

    s.bind((config['addr'], config['port']))
    dnn_server_udp(s)


if __name__ == "__main__":
    main(
        "../config/pc_serv.json")
