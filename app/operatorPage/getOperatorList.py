from flask import request
from flask import jsonify

from app.models import User,Operator
from app import db
from . import operatorPage
from app.auth import tokenUtils
import math

@operatorPage.route("/operator/list",methods=['POST'])
@tokenUtils.token_required
def getOperatorList(user_id):

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
		if user.role != 0:
			code = 202
			msg = 'access deny!'
		else:
			if page_index <= 0 or page_size <= 0:
				code = 203
				msg = 'parameter error!'
			else:
				total_record = len(Operator.query.all())
				total_page = math.ceil(total_record/page_size)

				operator_list = Operator.query.order_by(Operator.created_time.desc()).limit(page_size).offset((page_index-1)*page_size)
				for operator in operator_list:
					item = {}
					item['operator_id'] = operator.id
					item['bianhao'] = operator.id
					item['name'] = operator.name
					item['created_time'] = operator.created_time.strftime('%Y/%m/%d')
					item['tel'] = operator.account
					item['password'] = operator.password
					
					task_statistics = {}
					task_statistics['received'] = operator.receive_num
					task_statistics['processing'] = operator.process_num
					task_statistics['confirming'] = operator.wait_num
					task_statistics['finished'] = operator.finished_num

					item['task_statistics'] = task_statistics
					item['frozen'] = operator.status

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

