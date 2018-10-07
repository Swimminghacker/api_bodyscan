from app import db
from sqlalchemy import ForeignKey


class User(db.Model):

    # 定义表名
    __tablename__ = 'user'

    id = db.Column(db.INTEGER, primary_key=True)
    account = db.Column(db.String(45))
    password = db.Column(db.String(45))
    role = db.Column(db.INTEGER)

    def __init__(self, account, password,role):
        self.account = account
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User {}>'.format(self.account)

class Operator(db.Model):

    # 定义表名
    __tablename__ = 'operator'

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(45))
    account = db.Column(db.String(45))
    created_time = db.Column(db.Date)
    password = db.Column(db.String(45))

    receive_num = db.Column(db.INTEGER,default=0)
    process_num = db.Column(db.INTEGER,default=0)
    wait_num = db.Column(db.INTEGER,default=0)
    finished_num = db.Column(db.INTEGER,default=0)

    status = db.Column(db.INTEGER,default=1)

    def __init__(self, name, account, password, created_time):
        self.name = name
        self.account = account
        self.password = password
        self.created_time = created_time

    def __repr__(self):
        return '<Operator {}>'.format(self.account)


class Organization(db.Model):

    # 定义表名
    __tablename__ = 'organization'

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(45))
    account = db.Column(db.String(45))
    created_time = db.Column(db.Date)
    password = db.Column(db.String(45))
    gender = db.Column(db.String(45))

    belonged_organization = db.Column(db.String(45))
    email = db.Column(db.String(45))
    task_num = db.Column(db.INTEGER,default=0)
    status = db.Column(db.INTEGER,default=1)

    address = db.Column(db.String(45))
    id_card = db.Column(db.String(45))

    def __init__(self, name, gender,account, password, created_time,belonged_organization,email,address,id_card):
        self.name = name
        self.gender = gender
        self.account = account
        self.password = password
        self.created_time = created_time
        self.belonged_organization = belonged_organization
        self.email = email
        self.address = address
        self.id_card = id_card

    def __repr__(self):
        return '<Organization {}>'.format(self.account)


