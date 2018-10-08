from flask import request
from flask import jsonify

from app import db
from app.models import User,Organization,Task,Task_detail
from . import taskPage
from app.auth import tokenUtils

import datetime

@taskPage.route('/tasks/add',methods=['POST'])
@tokenUtils.token_required
def addOperator(user_id):
	
	code = 200 
	msg = "add task success!"
	task_id = 0

	values = request.values
	name = values.get('name')
	gender = values.get('gender')
	id_card = values.get('idcard')
	part = values.get('part')
	method = values.get('method')
	time = values.get('time')
	description = values.get('description')
	attachment = values.get('attachment')

	user = User.query.filter_by(id = user_id).first()
	if user is None:
		code = 201 
		msg = "this token-user not exist!"
	else:
		if user.role != 2:
			code = 202
			msg = "access deny!"
		else:
			if name is None or gender is None or id_card is None or part is None or method is None or time is None or description is None or attachment is None:
				code = 203
				msg = 'parameter error!'
			else:
				account = user.account
				organization = Organization.query.filter_by(account = account).first()
				organization_name = organization.belonged_organization
				organization_operator_id = organization.id

				created_time = datetime.date.today()
				status = 0
				
				task = Task(name, gender,created_time,organization_name,part,status,organization_operator_id)
				db.session.add(task)
				db.session.commit()

				task_id = task.id
				measuring_time = datetime.datetime.strptime(time,'%Y/%m/%d').date()
				task_detail = Task_detail(task_id, name,gender,id_card,part,method,measuring_time,description,attachment)
				db.session.add(task_detail)
				db.session.commit()

	json_to_send = {
			'status':{
				'code':code,
				'msg':msg
			},
			'data':{
				'task_id':task_id
			}
	}
	return jsonify(json_to_send)

