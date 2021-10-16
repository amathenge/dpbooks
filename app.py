import os
from flask import Flask, send_file, request, redirect, session, url_for, render_template, g
from werkzeug.utils import secure_filename
from database import get_db
import sqlite3
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = '/home/aamathenge/dpbooks/files'
LOG_FOLDER = '/home/aamathenge/dpbooks'
ALLOWED_EXTENSIONS = {'pdf, xlsx, xls'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['LOG_FOLDER'] = LOG_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.template_filter('nl2br')
def nl2br(item):
    if isinstance(item, str):
        return item.replace('\n','<br>')
    return item

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/clients')
def clients():
    db = get_db()
    cur = db.cursor()
    sql = "select c.id, c.name, c.email, c.phone, a.line1 || ', ' || a.city from clients c left join address a on c.address = a.id"
    cur.execute(sql)
    data = cur.fetchall()
    headers = data[0].keys()
    return render_template('clients.html', headers=headers, data=list(data))

@app.route('/invoices')
def invoices():
    return render_template('construction.html')

@app.route('/payments')
def payments():
    return render_template('construction.html')

@app.route('/reports')
def reports():
    return render_template('construction.html')

@app.route('/logout')
def logout():
    return render_template('construction.html')