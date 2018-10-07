from flask import request
from flask import jsonify

from app.models import User,Organization
from app import db
from . import organizationPage
from app.auth import tokenUtils
import math

@organizationPage.route("/organization/list",methods=['POST'])
@tokenUtils.token_required
def getOrganizationList(user_id):

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
				total_record = len(Organization.query.all())
				total_page = math.ceil(total_record/page_size)

				organization_list = Organization.query.order_by(Organization.created_time.desc()).limit(page_size).offset((page_index-1)*page_size)
				for organization in organization_list:
					item = {}
					item['org_id'] = organization.id
					item['bianhao'] = organization.id
					item['name'] = organization.name
					item['created_time'] = organization.created_time.strftime('%Y/%m/%d')
					item['tel'] = organization.account
					item['password'] = organization.password
					item['belong'] = organization.belonged_organization
					item['email'] = organization.email
					item['taskNumeber'] = organization.task_num
					item['frozen'] = organization.status

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

