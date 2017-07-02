from app import db, models
import datetime
import sys
import numpy as np

location_range = [[51.482233, 51.487871], [-0.095151, -0.112494]]
print(sys.argv)

if sys.argv > 1:
    for i in range(1000):
        lat = np.random.rand()*(location_range[0][1]-location_range[0][0])+location_range[0][0]
        lon = np.random.rand()*(location_range[1][1]-location_range[1][0])+location_range[1][0]
        h = models.Hotel(
            name='Hotel-%04d'%i,
            location='%f,%f'%(lat,lon),
            details = 'Hotel Discription',
            rating = np.random.rand()*3+2,
            price = np.random.rand()*100+50,
            price_unit = np.random.randint(5)+1,
            n_guests = np.random.randint(5)+1,
            n_beds = np.random.randint(3)+1,
            room_type = 'Appartment',
            images = '',
        )
        db.session.add(h)
        db.session.commit()
else:
    h = models.Hotel(name='Hotel1', location='123.3412,124.123')
    db.session.add(h)
    db.session.commit()

    u = models.User(nickname='admin', email='admin@swipestay.com', password='admin')
    db.session.add(u)
    db.session.commit()

    o = models.Booking(body='First Order', timestamp=datetime.datetime.utcnow(), user=u, hotel=h)
    db.session.add(o)
    db.session.commit()
