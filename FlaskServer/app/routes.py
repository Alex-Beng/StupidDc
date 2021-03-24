from flask import render_template, flash, redirect, url_for, request, send_from_directory, abort
from app import app, photos
from app.forms import AddClothesForm

import time
import os
import random


@app.route('/')
@app.route('/index')
def index():
    imgs = []
    img_path = app.config['UPLOADED_PHOTOS_DEST']
    pather = os.walk(img_path)
    for path,dir_list,file_list in pather:
        for file_name in file_list:
            # os.path.join(path, file_name)
            # # print(os.path.join(path, file_name) )
            imgs.append(file_name)
    if len(imgs) > 2:
        imgs = [random.choice(imgs) for i in range(2)]
    return render_template('index.html', title='Home', images=imgs)

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/select')
def select():
    return render_template('select.html', title='Home')

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
        return render_template('add.html', title='Home', form=form)
    

@app.route('/delete')
def delete():
    return render_template('delete.html', title='Home')
