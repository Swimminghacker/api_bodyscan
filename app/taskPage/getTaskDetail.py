from flask import request
from flask import jsonify

from app.models import User,Organization,Operator,Task,Task_detail
from app import db
from . import taskPage
from app.auth import tokenUtils
import math
import datetime

@taskPage.route("/tasks/detail/<task_id>",methods=['POST'])
@tokenUtils.token_required
def getTaskDetail(user_id,task_id):
	code = 200
	msg = "success!"
	data = {}

	user = User.query.filter_by(id = user_id).first()

	if user is None:
		code = 201 
		msg = 'this user of token no exist!'
	else:

		task_detail = Task_detail.query.filter_by(task_id = task_id).first()
		task = Task.query.filter_by(id = task_id).first()
		if task_detail is None or task is None:
			code = 202
			msg = 'task not exist!'
		else:
			detail = {}
			operator_detail = {}

			detail['name'] = task.name
			detail['gender'] = task.gender
			detail['idcard'] = task_detail.target_id
			detail['part'] = task_detail.measuring_part
			detail['method'] = task_detail.measuring_method
			detail['time'] = task_detail.measuring_time.strftime('%Y/%m/%d')
			detail['description'] = task_detail.description
			detail['age'] = datetime.datetime.now().year - int(task_detail.target_id[6:10])

			operator = Operator.query.filter_by(id = task.operator_id).first()
			operator_name = ''
			operator_tel = ''
			if operator is not None:
				operator_name = operator.name
				operator_tel = operator.account
			operator_detail['name'] = operator_name
			operator_detail['tel'] = operator_tel

			data['task_detail'] = detail
			data['operator_detail'] = operator_detail
			data['stage'] = task.status
			data['task_attachment_is_downloaded'] = True
			data['task_attachment_url'] = task_detail.file_url
			data['task_report_url'] = task_detail.report_file_url
			data['can_operator_confirm'] = False
			if task.status == 2:
				data['can_operator_confirm'] = True

	json_to_send = {
		'status':{
			'code':code,
			'msg':msg
		},
		'data':	data
	}
	return jsonify(json_to_send)

