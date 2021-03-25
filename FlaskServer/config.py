import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or '我裂开了居然让我写这个傻逼大创'
    UPLOADED_PHOTOS_DEST = os.environ.get('UPLOADED_PHOTOS_DEST') or 'D:/Alex_Beng/code/python/StupidDc/FlaskServer/app/images/'
    ICO_PAHT = os.environ.get('ICO_PAHT') or 'D:/Alex_Beng/code/python/StupidDc/FlaskServer/app/'

    PC_SERVER_ADDR = '10.27.29.120'
    PC_SERVER_PORT = 8848

    SERIAL_SERVER_ADDR = '10.70.154.76'
    SERIAL_SERVER_PORT = 8844
    
    # cos 距离取值为[0, 2]
    DNN_THRESHOLD = 0.7