from flask import request
from flask import jsonify

from app import db
from app.models import User,Organization
from . import organizationPage
from app.auth import tokenUtils

import datetime

@organizationPage.route('/organization/add',methods=['POST'])
@tokenUtils.token_required
def addOperator(user_id):
	code = 200 
	msg = "add organization-operator success!"
	org_id = None

	values = request.json
	name = values.get('name')
	gender = values.get('gender')
	belong = values.get('belong')
	email = values.get('email')
	tel = values.get('tel')

	id_card = values.get('idcard')
	address = values.get('address')

	user = User.query.filter_by(id = user_id).first()
	if user is None:
		code = 201 
		msg = "this token-user not exist!"
	else:
		if user.role != 0:
			code = 202
			msg = "access deny!"
		else:
			if name is None or gender is None or belong is None or email is None or tel is None:
				code = 203
				msg = 'parameter error!'
			else:
				organization = Organization.query.filter_by(account = tel).first()
				user = User.query.filter_by(account = tel).first()
				if organization is not None or user is not None:
					code = 204 
					msg = 'organization-operator has exist!'
				else:
					account = tel
					password = account[-6:]
					created_time = datetime.date.today()
					role = 2
					
					organization = Organization(name, gender,account, password, created_time,belong,email,address,id_card)
					user = User(account,password,role)

					db.session.add(user)
					db.session.add(organization)
					db.session.commit()

					org_id = organization.id

	json_to_send = {
			'status':{
				'code':code,
				'msg':msg
			},
			'data':{
				'org_id':org_id
			}
	}
	return jsonify(json_to_send)

