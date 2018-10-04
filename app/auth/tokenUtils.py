from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired,BadSignature
from config import Config
from functools import wraps
from flask import request
from flask import jsonify

none_token = {
		'status':{
			'code':301,
			'msg':'none token'
		}
		}
expired_token = {
		'status':{
			'code':302,
			'msg':'expired token'
		},
		'data':{}
		}

bad_token = {
		'status':{
			'code':303,
			'msg':'bad token'
		},
		'data':{}
		}

#单位为s  一天过期
def gen_token(user,expiration=60*60*24):
	s = Serializer(Config.SECRET_KEY,expires_in = expiration)
	return s.dumps({'id':user.id})


def token_required(func):
	@wraps(func)
	def wrapper(*args,**kwargs):
		token = request.headers.get('Auth-token')
		if token is None:
			return jsonify(none_token)
		else:
			s = Serializer(Config.SECRET_KEY)
			try:
				data = s.loads(token)
			except SignatureExpired:
				return jsonify(expired_token)
			except BadSignature:
				return jsonify(bad_token)
			kwargs['user_id'] = data['id']
		return func(*args,**kwargs)
	return wrapper

