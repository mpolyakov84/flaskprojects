# setup db in __init__.py
from flask_login import UserMixin
from sqlalchemy.testing.pickleable import User
from myproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppies', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f'Puppy name is {self.name} and owner is {self.owner.name}.'
        else:
            return f'Puppy name is {self.name} and has no owner assigned yet.'

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppie_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self, name, puppie_id):
        self.name = name
        self.puppie_id = puppie_id


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password =db.Column(db.String(124))

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        if check_password_hash(self.password, password):
            return True
        else:
            return False

    def __repr__(self):
        return f'Username: {self.username} \nEmail: {self.email} \nPassword: {self.password}'
