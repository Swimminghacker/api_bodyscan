from flask import request
from flask import jsonify
from sqlalchemy import or_

from app.models import User,Organization,Operator,Task,Task_detail
from app import db
from . import taskPage
from app.auth import tokenUtils
import math

@taskPage.route("/tasks/list",methods=['POST'])
@tokenUtils.token_required
def getTaskList(user_id):

	code = 200
	msg = "success!"

	values = request.json
	
	total_page = 0
	total_record = 0

	page_index = 0
	page_size = 0
	try:		
		page_index = values['pagination']['pageNumber']
		page_size = values['pagination']['pageSize']
	except:
		pass
	data = []

	user = User.query.filter_by(id = user_id).first()

	if user is None:
		code = 201 
		msg = 'this user of token no exist!'
	else:
		if page_index <= 0 or page_size <= 0:
			code = 203
			msg = 'parameter error!'
		else:

			total_record = 0
			total_page = 0
			task_list = []

			if user.role == 0:
				total_record = len(Task.query.all())
				total_page = math.ceil(total_record/page_size)
				task_list = Task.query.order_by(Task.created_time.desc()).limit(page_size).offset((page_index-1)*page_size)
			elif user.role == 1:
				account = user.account
				#选择自己跟进的任务以及没有领取的任务
				operator = Operator.query.filter_by(account = account).first()

				total_record = len(Task.query.filter(or_(Task.operator_id == operator.id,Task.status == 0)).all())
				total_page = math.ceil(total_record/page_size)

				task_list = Task.query.filter(or_(Task.operator_id == operator.id,Task.status == 0)).order_by(Task.created_time.desc()).limit(page_size).offset((page_index-1)*page_size)
				

			elif user.role == 2:

				account = user.account
				organization_operator = Organization.query.filter_by(account = account).first()

				total_record = len(Task.query.filter_by(organization_operator_id = organization_operator.id).all())
				total_page = math.ceil(total_record/page_size)

				task_list = Task.query.filter_by(organization_operator_id = organization_operator.id).order_by(Task.created_time.desc()).limit(page_size).offset((page_index-1)*page_size)
			
			for task in task_list:
				item = {}

				operator_id = task.operator_id
				operator = Operator.query.filter_by(id = operator_id).first()
				operator_name = ''
				if operator is not None:
					operator_name = operator.name

				organization_operator_id = task.organization_operator_id
				organization_operator = Organization.query.filter_by(id = organization_operator_id).first()
				organization_operator_name = ''
				if organization_operator is not None:
					organization_operator_name = organization_operator.name

				item['task_id'] = task.id
				item['name'] = task.name
				item['gender'] = task.gender
				item['created_time'] = task.created_time.strftime('%Y/%m/%d')
				item['operator_name'] = operator_name
				item['org_name'] = organization_operator_name
				item['org_belong'] = task.organization
				item['part'] = task.measuring_part
				item['stage'] = task.status

				data.append(item)

	json_to_send = {
		'pageInfo':{
			'totalPage':total_page,
			'totalRecord':total_record
		},
		'status':{
			'code':code,
			'msg':msg
		},
		'data':	data
	}
	return jsonify(json_to_send)

