import socket
import json
import threading
import cv2
import numpy as np


def readjson(file_path, cd):
    t_file = open(file_path, encoding=cd)
    t_dict = json.load(t_file)
    t_file.close()
    return t_dict

def img2bytes(img):
    _, enc_img = cv2.imencode(".jpg", img)
    enc_arr = np.array(enc_img)
    enc_bytes = enc_arr.tobytes()
    return enc_bytes

def bytes2img(data):
    img = np.asarray(bytearray(data), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return img
