from app.auth import tokenUtils
from flask import jsonify
from app.models import User
from . import userPage

@userPage.route('/logout',methods = ['GET'])
@tokenUtils.token_required
def logout(user_id):
	return jsonify({
		'status':{
			'code':200,
			'msg':'logout success!'
		},
		'data':{}
		})