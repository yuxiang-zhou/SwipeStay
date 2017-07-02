from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # fields
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(256), index=True)
    role = db.Column(db.Integer)
    # relationship
    orders = db.relationship('Booking', backref='user', lazy='dynamic')




class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # fields
    name = db.Column(db.String(64), index=True, unique=True)
    details = db.Column(db.String(2048))
    location = db.Column(db.String(120), index=True, unique=True)
    rating = db.Column(db.Float)
    price = db.Column(db.Float)
    price_unit = db.Column(db.Integer)
    n_guests = db.Column(db.Integer)
    n_beds = db.Column(db.Integer)
    n_rooms = db.Column(db.Integer, default=1)
    shared = db.Column(db.Boolean, default=False)
    address = db.Column(db.String(2048), default='')
    room_type = db.Column(db.String(64))
    images = db.Column(db.String(6400))
    # fields
    orders = db.relationship('Booking', backref='hotel', lazy='dynamic')




class Booking(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # fields
    body = db.Column(db.String(140))
    checkin = db.Column(db.DateTime)
    checkout = db.Column(db.DateTime)
    status = db.Column(db.Integer)
    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
