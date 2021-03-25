from flask import render_template, flash, redirect, url_for, request, send_from_directory, abort
from app import app, photos
from app.forms import AddClothesForm, SelectForm, DeleteForm

import time
import os
import random

import sys
sys.path.append("../")
from Util.util import get_imgs_name


def selecting():
    time.sleep(10)

def deleteing():
    time.sleep(10)

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
            
            selecting()
            
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
