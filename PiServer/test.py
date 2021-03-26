import socket
import json
import time
import math
import cv2
import numpy as np

import sys
sys.path.append("../")
from Util.util import readjson

def sendonce(config):
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.connect((config['addr'], config['port']))

    t = s.send(b'yes')

    s.close()
if __name__ == "__main__":
    cfg = readjson("../config/serial_serv.json", 'utf-8')
    sendonce(cfg)
    
