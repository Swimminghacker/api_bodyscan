from flask import request, session, make_response
import json

from app import db
from . import operatorPage

@operatorPage.route("/operator/list",methods=['GET'])
def getOperatorList():
    return 'operatorPage'

