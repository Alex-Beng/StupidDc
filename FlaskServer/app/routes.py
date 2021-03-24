from flask import render_template, flash, redirect, url_for, request, send_from_directory, abort
from app import app


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home')

@app.route('/select')
def select():
    return render_template('select.html', title='Home')

@app.route('/add')
def add():
    return render_template('add.html', title='Home')

@app.route('/delete')
def delete():
    return render_template('delete.html', title='Home')
