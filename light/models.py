####################################
# File name: models.py             #
# Author: Joe Abbate               #
####################################
from light import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    picture = db.Column(db.String, nullable=False)

    def __init__(self, uid, firstname, lastname, picture, style, color1, color2, color3, numcolors):
        self.id = uid
        self.firstname = firstname
        self.lastname = lastname
        self.picture = picture

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def get_id(self):
        return self.id

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False


class Seat(db.Model):
    __tablename__ = 'seat'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String, db.ForeignKey('user.id'), nullable=True)
    style = db.Column(db.String, nullable=True)
    color1 = db.Column(db.String, nullable=True)
    color2 = db.Column(db.String, nullable=True)
    color3 = db.Column(db.String, nullable=True)

    def __init__( self, style, color1, color2, color3 ):
        self.type = style
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Room(db.Model):
    __tablename__ = 'room'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    style = db.Column(db.String, nullable=True)
    color1 = db.Column(db.String, nullable=True)
    color2 = db.Column(db.String, nullable=True)
    color3 = db.Column(db.String, nullable=True)
    last_modify_user = db.Column(db.String, nullable=True)
    last_modify_time = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=True)
    pi_ip = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<id {}>'.format(self.id)