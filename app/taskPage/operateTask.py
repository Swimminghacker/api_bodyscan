from flask import request
from flask import jsonify

from app import db
from app.models import User,Organization,Task,Task_detail,Operator
from . import taskPage
from app.auth import tokenUtils
from app.utilsPage import downloadFile

import datetime

@taskPage.route('/tasks/operate/<task_id>',methods=['GET','POST'])
@tokenUtils.token_required
def operateTask(user_id,task_id):
	action = request.values.get('action')

	code = 205 
	msg = "unknown error!"

	user = User.query.filter_by(id = user_id).first()
	task = Task.query.filter_by(id = task_id).first()
	task_detail = Task_detail.query.filter_by(task_id = task_id).first()

	user_role = user.role
	if user is None:
		code = 201 
		msg = "this token-user not exist!"
	else:
		if user_role == 0:
			code = 202
			msg = "access deny!"
		else:
			if task is None:
				code = 203
				msg = 'task not exist!'
			else:
				if action not in ['receive','process','confirm']:
					code = 204
					msg = 'action error!'
				else:
					if user_role == 1:
						operator = Operator.query.filter_by(account = user.account).first()
						if operator is not None:
							if action == 'receive' and task.status == 0:
								
								task.operator_id = operator.id
								task.status = 1

								operator.receiveTask(True)
								operator.processTask(True)

								db.session.add(task)
								db.session.add(operator)
								db.session.commit()

								code = 200
								msg = 'operate task success!'

							elif action == 'process' and (task.status == 1 or task.status == 2) and task.operator_id == operator.id:

								file = request.files['report_file']
								report_file_url = downloadFile.uploadFile(file)

								if report_file_url is not None:

									task_detail.report_file_url = report_file_url
									task.status = 2

									operator.processTask(False)
									operator.receiveTask(False)
									operator.waitTask(True)

									db.session.add(task)
									db.session.add(task_detail)
									db.session.add(operator)
									db.session.commit()

									code = 200
									msg = 'operate task success!'
									data = {'task_report_url':report_file_url}

							elif action == 'confirm' and task.status == 2 and task.operator_id == operator.id:
								
								task.status = 3
					
								operator.finishTask(True)
								operator.waitTask(False)
								
								db.session.add(task)
								db.session.add(operator)
								db.session.commit()

								code = 200
								msg = 'operate task success!'

					elif user_role == 2:
						if action == 'confirm' and task.status == 2:
							task.status = 3
							operator = Operator.query.filter_by(id = task.operator_id).first()
							if operator is not None:
								operator.finishTask(True)
								operator.waitTask(False)
							db.session.add(task)
							db.session.add(operator)
							db.session.commit()

							code = 200
							msg = 'operate task success!'


	json_to_send = {
			'status':{
				'code':code,
				'msg':msg
			},
			'data':{}
	}
	return jsonify(json_to_send)

