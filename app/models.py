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


class Task(db.Model):

    # 定义表名
    __tablename__ = 'task'

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(45))
    gender = db.Column(db.String(45))
    created_time = db.Column(db.Date)
    organization = db.Column(db.String(45))
    measuring_part = db.Column(db.String(45))
    status = db.Column(db.INTEGER,default=0)
    organization_operator_id = db.Column(db.INTEGER)
    operator_id = db.Column(db.INTEGER)

    def __init__(self, name, gender,created_time,organization,measuring_part,status,organization_operator_id):
        self.name = name
        self.gender = gender
        self.created_time = created_time
        self.organization = organization
        self.measuring_part = measuring_part
        self.status = status
        self.organization_operator_id = organization_operator_id

    def __repr__(self):
        return '<Task {}>'.format(self.name)

class Task_detail(db.Model):

    # 定义表名
    __tablename__ = 'task_detail'

    id = db.Column(db.INTEGER, primary_key=True)
    task_id = db.Column(db.INTEGER)
    target_name = db.Column(db.String(45))
    target_gender = db.Column(db.String(45))
    target_id = db.Column(db.String(45))

    measuring_part = db.Column(db.String(45))
    measuring_method = db.Column(db.String(45))
    measuring_time = db.Column(db.Date)

    description = db.Column(db.String(255))

    file_url = db.Column(db.String(45))
    report_file_url = db.Column(db.String(45))

    def __init__(self, task_id, target_name,target_gender,target_id,measuring_part,measuring_method,measuring_time,description,file_url):
        self.task_id = task_id
        self.target_name = target_name
        self.target_gender = target_gender
        self.target_id = target_id
        self.measuring_part = measuring_part
        self.measuring_method = measuring_method
        self.measuring_time = measuring_time
        self.description = description
        self.file_url = file_url

    def __repr__(self):
        return '<Task_detail {}>'.format(self.task_id)


