from flask import request
from flask import jsonify
import json
from app import db
from app.models import User
from . import userPage

from app.auth import tokenUtils


@userPage.route('/login',methods = ['POST'])
def login():
	code = 200
	msg = 'success'
	data = {}

	values = request.values
	name = values.get('username')
	password = values.get('password')
	if name is None or password is None:
		code = 201
		msg = 'there is no name or password!'
	else:
		user = User.query.filter_by(account = name).first()
		if user is None:
			code = 202
			msg = 'account not exsit!'
		else:
			if user.password != password:
				code = 203
				msg = 'password error!'
			else:
				data = {
					'ident':user.role,
					'token':tokenUtils.gen_token(user).decode('ascii')
				}
	
	josn_to_send = {
		'status':{
			'code':code,
			'msg':msg
		},
		'data':data
	}

	return json.dumps(josn_to_send,ensure_ascii=False)

@userPage.route('/modifyPassword',methods=['POST'])
@tokenUtils.token_required
def change_password(user_id):
	values = request.values
	pre_password = values.get('prevPwd')
	new_password = values.get('newPwd')

	code = 200
	msg = ""
	user = User.query.filter_by(id = user_id).first()
	if user is None:
		code = 201
		msg = "this user not exsit!"
	else:
		if pre_password is None or new_password is None:
			code = 202
			msg = "no pre_password or new_password!"
		else:
			if user.password != pre_password:
				code = 203
				msg = "pre_password is not correct!"
			else:
				user.password = new_password
				db.session.add(user)
				db.session.commit()

				msg = "change password succsss!"
	josn_to_send = {
			'status':{
				'code':code,
				'msg':msg
			},
			'data':{}
	}
	return jsonify(josn_to_send)