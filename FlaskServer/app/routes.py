from flask import render_template, flash, redirect, url_for, request, send_from_directory, abort
from app import app, photos, feat_extractor
from app.forms import AddClothesForm, SelectForm, DeleteForm

import time
import os
import random
import cv2
from scipy.spatial import distance

import sys
sys.path.append("../")
from Util.util import get_imgs_name
from PcServer.dnn_serv import dnn_server_udp_once
from Piserver.test import sendonce

def get_local_img_features():
    b_t = time.time()

    imgs = get_imgs_name(app.config['UPLOADED_PHOTOS_DEST'])
    fets = []
    for img_name in imgs:
        full_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], img_name)
        img = cv2.imread(full_path)
        img = cv2.resize(img, (224, 224))

        feature = feat_extractor.feat_extractor.predict(img.reshape(-1, 224, 224, 3))[0]
        fets.append(feature)
    
    e_t = time.time()
    print(f"local img feature take {e_t-b_t}")
    return fets

def selecting(full_name):
    # steps
    # 1. get real-time frame with udp from pi
    # 2. comp cos distance between frame and the pic existed
    #        if distance < threshold: 
    #            give signal to pi
    local_features = get_local_img_features()
    dnn_config = dict()
    dnn_config['addr'] = '0.0.0.0'
    dnn_config['port'] = app.config['PC_SERVER_PORT']
    serial_config = dict()
    serial_config['addr'] = app.config['SERIAL_SERVER_ADDR']
    serial_config['port'] = app.config['SERIAL_SERVER_PORT']
    while True:
        img = dnn_server_udp_once(dnn_config)
        img = cv2.resize(img, (224, 224))
        
        # feature shape is (4096, )
        feature = feat_extractor.feat_extractor.predict(img.reshape(-1, 224, 224, 3))[0]

        cos_dists = [ distance.cosine(feature, l_f) for l_f in local_features]
        cloest_idx = min(range(len(cos_dists)), key = lambda k: cos_dists[k])
        if cos_dists[cloest_idx] < app.config['DNN_THRESHOLD']:
            sendonce(serial_config)
            return
    #     cv2.imshow("ya", img)
    #     key = cv2.waitKey(1)
    #     if key == ord('q'):
    #         break
    # cv2.destroyAllWindows()


@app.route('/')
@app.route('/index')
def index():
    imgs = get_imgs_name(app.config['UPLOADED_PHOTOS_DEST'])
    if len(imgs) > 2:
        imgs = [random.choice(imgs) for i in range(2)]
    return render_template('index.html', title='Home', images=imgs)

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)
@app.route('/favicon.ico')
def ico():
    return send_from_directory(app.config['ICO_PAHT'], 'favicon.ico')

@app.route('/select', methods=['GET', 'POST'])
def select():
    form = SelectForm()
    imgs = get_imgs_name(app.config['UPLOADED_PHOTOS_DEST'])

    if request.method == 'POST':
        if form.validate_on_submit():
            short_name = form.name.data
            full_name = ''
            for f_name in imgs:
                if f_name.split('@')[0] == short_name:
                    full_name = f_name
            print(full_name)
            
            selecting(full_name)
            
            flash(f"you have fucking select the {short_name}.")
        return redirect('select')
    else:
        return render_template('select.html', title='Select', form=form, images=imgs)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddClothesForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.title.data
            print(name)
            images = request.files.getlist("photo")
            for idx, img in enumerate(images):
                # 处理文件名
                filename = f'{name}@{str(idx)}@{str(time.time())}'
                image = photos.save(img, name=filename + '.')
            flash("you have fucking add a clothes.")
        return redirect('add')
    else:
        return render_template('add.html', title='Add', form=form)
    

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeleteForm()
    imgs = get_imgs_name(app.config['UPLOADED_PHOTOS_DEST'])

    if request.method == 'POST':
        if form.validate_on_submit():
            short_name = form.name.data
            full_name = ''
            for f_name in imgs:
                if f_name.split('@')[0] == short_name:
                    full_name = f_name
            f_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], full_name)
            ret = os.system(f"rm {f_path}")
            if ret:
                flash("Something gone worry...Havn't deleted...")
            else:
                flash(f"you have fucking delete the {short_name}.")
        return redirect('delete')
    else:
        return render_template('delete.html', title='Delete', form=form, images=imgs)
