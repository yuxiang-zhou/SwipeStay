import os
import json
from flask import render_template
from app import app
from flask import Flask, request, redirect, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename
from pathlib import Path

# api hosts
retval_template = {
    'code': -1,
}


# user
@app.route('/api/user/login/<username>/<pswdhash>', methods=['GET'])
def login(username, pswdhash):
    data = retval_template.copy()

    return json.dumps(data)

@app.route('/api/user/info', methods=['GET'])
def user_info():
    data = retval_template.copy()

    return json.dumps(data)

# hotel
@app.route('/api/hotel/filter/<condition>', methods=['GET'])
def hotel_filter(condition):
    data = retval_template.copy()

    return json.dumps(data)
