import os

from app import create_app,db
from app.models import User
from flask_script import Manager, Shell,Server
#from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
#migrate = Migrate(app, db)

print('xxxxxxxxxxxxxxxx',os.path.abspath('.'))


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))
#manager.add_command('db', MigrateCommand)
manager.add_command('runserver',Server(host="0.0.0.0",port=8000,use_debugger=True))

if __name__ == '__main__':
    app.run(host='0.0.0.0')