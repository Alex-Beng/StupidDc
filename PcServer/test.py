import socket
import json
import time
import math
import cv2
import numpy as np

import sys
sys.path.append("../")
from Util.util import readjson, img2bytes

window_name = 'ctmd'

def sendonce(cofig_file, cfg_cd='utf-8'):
    config = readjson(cofig_file, cfg_cd)
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    cp = cv2.VideoCapture(0)
    while True:
        begin_time = time.time()
        _, frame = cp.read()
        end_time = time.time()

        frame = cv2.resize(frame, (320, 240))
        if not _:
            print("opening...")
            continue
        
        enc_frame = img2bytes(frame)
        print(f'encoded frame len: {len(enc_frame)}', 
              'raw fps: %.2f'%(1.0/(end_time-begin_time)))
        s.sendto(enc_frame, (config['addr'], config['port']))

    s.close()

if __name__ == "__main__":
    sendonce("../config/pc_serv.json")    
    