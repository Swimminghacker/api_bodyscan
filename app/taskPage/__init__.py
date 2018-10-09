from flask import Blueprint

taskPage = Blueprint('taskPage', __name__)

from . import addTask
from . import getTaskList
from . import getTaskDetail
from . import operateTask
