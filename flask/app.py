# -*- coding: utf-8 -*-

import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from models.Entry import Entry
from dao.MysqlConn import get_db

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='session key',
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/debug')
def debug():
    return 'debug'

@app.route('/')
def show_entries():
    db = get_db()
    entries = db.query(Entry).all()
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    try:
        entry = Entry(
            title = request.form['title'],
            text = request.form['text']
        )
        db = get_db()
        # 添加到session:
        ret = db.add(entry)
        print "add ret:", ret
        # 提交即保存到数据库:
        db.commit()
        # 关闭session:
        db.close()
        flash('New entry was successfully posted')
    except :
        flash('New entry posted failed')
        db.rollback()
        db.close()
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
            error = 'Invalid username'
        elif request.form['password'] != 'admin':
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


app.run(debug=True)