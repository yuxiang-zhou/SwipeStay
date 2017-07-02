import os
import json
from flask import render_template
from app import app, models
from flask import Flask, request, redirect, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename
from pathlib import Path

from sqlalchemy.ext.declarative import DeclarativeMeta
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


# api hosts
retval_template = {
    'code': -1,
}


# user
@app.route('/api/user/login/<username>/<pswdhash>', methods=['GET'])
def login(username, pswdhash):
    data = retval_template.copy()

    return json.dumps(data)

@app.route('/api/user/info/<username>', methods=['GET'])
def user_info():
    data = retval_template.copy()



    return json.dumps(data)

@app.route('/api/user/list/', methods=['GET'])
def user_list():
    data = retval_template.copy()

    data['code'] = 0
    data['data'] = models.User.query.all()

    return json.dumps(data, cls=AlchemyEncoder)

# hotel
@app.route('/api/hotel/filter/<condition>', methods=['GET'])
def hotel_filter(condition):
    data = retval_template.copy()

    data['code'] = 0
    data['data'] = models.Hotel.query.all()

    return json.dumps(data, cls=AlchemyEncoder)
