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

    t = s.send(b'yes')

    s.close()
if __name__ == "__main__":
    sendonce("../config/serial_serv.json")    
    
