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

    receive_num = db.Column(db.INTEGER)
    process_num = db.Column(db.INTEGER)
    wait_num = db.Column(db.INTEGER)
    finished_num = db.Column(db.INTEGER)

    status = db.Column(db.INTEGER)

    def __init__(self, name, account, password, created_time):
        self.name = name
        self.account = account
        self.password = password
        self.created_time = created_time

    def __repr__(self):
        return '<Operator {}>'.format(self.account)

