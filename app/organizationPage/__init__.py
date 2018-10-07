from flask import Blueprint

organizationPage = Blueprint('organizationPage', __name__)

from . import getOrgList
from . import addOrg
from . import freezeOrg