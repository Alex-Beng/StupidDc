import socket
import json
import time
import math
import cv2
import numpy as np

import sys
sys.path.append("../")
from Util.util import readjson

def sendonce(cofig_file, cfg_cd='utf-8'):
    config = readjson(cofig_file, cfg_cd)
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.connect((config['addr'], config['port']))

    img = cv2.imread("./test.jpg")

    _, enc_img = cv2.imencode(".jpg", img)
    enc_arr = np.array(enc_img)
    enc_bytes = enc_arr.tobytes()
    s.send(enc_bytes)

    s.close()
if __name__ == "__main__":
    for i in range(5):
        sendonce("../config/pc_serv.json")
        time.sleep(1)
    
    