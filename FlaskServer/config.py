import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or '我裂开了居然让我写这个傻逼大创'
    UPLOADED_PHOTOS_DEST = os.environ.get('UPLOADED_PHOTOS_DEST') or 'D:/Alex_Beng/code/python/StupidDc/FlaskServer/app/images/'