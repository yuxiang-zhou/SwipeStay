from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
hotel = Table('hotel', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('details', String(length=2048)),
    Column('location', String(length=120)),
    Column('rating', Float),
    Column('price', Float),
    Column('price_unit', Integer),
    Column('n_guests', Integer),
    Column('n_beds', Integer),
    Column('room_type', String(length=64)),
    Column('images', String(length=6400)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
    Column('password', String(length=256)),
    Column('role', Integer),
)

booking = Table('booking', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', TIMESTAMP),
    Column('user_id', INTEGER),
    Column('hotel_id', INTEGER),
)

booking = Table('booking', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('body', String(length=140)),
    Column('checkin', DateTime),
    Column('checkout', DateTime),
    Column('status', Integer),
    Column('user_id', Integer),
    Column('hotel_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['hotel'].columns['details'].create()
    post_meta.tables['hotel'].columns['images'].create()
    post_meta.tables['hotel'].columns['n_beds'].create()
    post_meta.tables['hotel'].columns['n_guests'].create()
    post_meta.tables['hotel'].columns['price'].create()
    post_meta.tables['hotel'].columns['price_unit'].create()
    post_meta.tables['hotel'].columns['rating'].create()
    post_meta.tables['hotel'].columns['room_type'].create()
    post_meta.tables['user'].columns['role'].create()
    pre_meta.tables['booking'].columns['timestamp'].drop()
    post_meta.tables['booking'].columns['checkin'].create()
    post_meta.tables['booking'].columns['checkout'].create()
    post_meta.tables['booking'].columns['status'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['hotel'].columns['details'].drop()
    post_meta.tables['hotel'].columns['images'].drop()
    post_meta.tables['hotel'].columns['n_beds'].drop()
    post_meta.tables['hotel'].columns['n_guests'].drop()
    post_meta.tables['hotel'].columns['price'].drop()
    post_meta.tables['hotel'].columns['price_unit'].drop()
    post_meta.tables['hotel'].columns['rating'].drop()
    post_meta.tables['hotel'].columns['room_type'].drop()
    post_meta.tables['user'].columns['role'].drop()
    pre_meta.tables['booking'].columns['timestamp'].create()
    post_meta.tables['booking'].columns['checkin'].drop()
    post_meta.tables['booking'].columns['checkout'].drop()
    post_meta.tables['booking'].columns['status'].drop()
