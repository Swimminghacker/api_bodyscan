from flask import request
from flask import jsonify

from app import db
from app.models import User,Operator
from . import operatorPage
from app.auth import tokenUtils

@operatorPage.route("/operator/freeze",methods=['POST'])
@tokenUtils.token_required
def freezeOperator(user_id):
	code = 200
	msg = 'Success!'

	values = request.json
	operator_id = values.get('operator_id')
	action = values.get('action')

	user = User.query.filter_by(id = user_id).first() 
	if user is None:
		code = 201
		msg = 'this user of token not exsit!'
	else:
		if user.role != 0:
			code = 202
			msg = 'access deny!'
		else:
			if operator_id is None or action is None:
				code = 203
				msg = 'parameter error!'
			else:
				operator = Operator.query.filter_by(id = operator_id).first()
				if operator is None:
					code = 204
					msg = 'this operator not exsit!'
				else:
					if action == 1:
						operator.status = 1
					elif action == 2:
						operator.status = 0
					db.session.add(operator)
					db.session.commit()

	json_to_send = {
			'status':{
				'code':code,
				'msg':msg
			}
	}
	return jsonify(json_to_send)
