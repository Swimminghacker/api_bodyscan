from flask import request
from flask import jsonify

from app import db
from app.models import User,Organization
from . import organizationPage
from app.auth import tokenUtils

@organizationPage.route("/organization/freeze",methods=['POST'])
@tokenUtils.token_required
def freezeOperator(user_id):
	code = 200
	msg = 'Success!'

	values = request.json
	org_id = values.get('org_id')
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
			if org_id is None or action is None:
				code = 203
				msg = 'parameter error!'
			else:
				organization = Organization.query.filter_by(id = org_id).first()
				if organization is None:
					code = 204
					msg = 'this organization not exsit!'
				else:
					if action == 1:
						organization.status = 1
					elif action == 2:
						organization.status = 0
					db.session.add(organization)
					db.session.commit()

	json_to_send = {
			'status':{
				'code':code,
				'msg':msg
			}
	}
	return jsonify(json_to_send)
