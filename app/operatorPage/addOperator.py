from flask import request
from flask import jsonify

from app import db
from app.models import User,Operator
from . import operatorPage
from app.auth import tokenUtils

import datetime

@operatorPage.route('/operator/add',methods=['POST'])
@tokenUtils.token_required
def addOperator(user_id):
	code = 200 
	msg = "add operator success!"

	values = request.values
	name = values.get('name')
	tel = values.get('tel')

	user = User.query.filter_by(id = user_id).first()
	if user is None:
		code = 201 
		msg = "this user not exist!"
	else:
		if user.role != 0:
			code = 202
			msg = "access deny!"
		else:
			if name is None or tel is None:
				code = 203 
				msg = "no name or tel"
			else:
				user = User.query.filter_by(account = tel).first()
				if user is not None:
					code = 204
					msg = "account exist!"
				else:
					account = tel 
					password = tel[-6:]
					role = 1
					user = User(account,password,role)

					created_time = datetime.date.today()
					operator = Operator(name,account,password,created_time)

					db.session.add(user)
					db.session.add(operator)
					db.session.commit()
	json_to_send = {
			'status':{
				'code':code,
				'msg':msg
			},
			'data':{}
	}
	return jsonify(json_to_send)