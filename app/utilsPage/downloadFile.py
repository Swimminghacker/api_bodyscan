import os
from flask import request,send_from_directory
from . import utilsPage

from werkzeug import secure_filename
import os
from flask import url_for,send_from_directory
import hashlib,time

ALLOWED_EXTENSIONS = set(['doc', 'docx', 'pdf', 'png','jpg','txt','xls','xlsx'])
basedir = os.path.join(os.getcwd(),'file')

@utilsPage.route('/downloadFile/<filename>',methods = ['POST','GET'])
def download(filename):
	return send_from_directory(basedir,filename)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def uploadFile(file,user_id):
	if file and allowed_file(file.filename):
		ext = '.' + file.filename.rsplit('.',1)[1]
		filename = hashlib.md5((str(user_id) + str(time.time())).encode('UTF-8')).hexdigest()[:15] + ext
		file_url = os.path.join(basedir, filename)
		file.save(file_url)
		download_url = url_for('utilsPage.download',filename=filename)
		return download_url
	return None
