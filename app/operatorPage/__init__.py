from flask import Blueprint

operatorPage = Blueprint('operatorPage', __name__)

from . import getOperatorList
from . import addOperator