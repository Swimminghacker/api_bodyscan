from flask import Blueprint

taskPage = Blueprint('taskPage', __name__)

from . import addTask
