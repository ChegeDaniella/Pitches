from app import create_app
from flask_script import Manager,Server
from app.main.models import User,Role 
from app import db
from flask_migrate import Migrate,MigrateCommand

#create app instance
app = create_app('development')

migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    '''
    run unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User = User, Role = Role)
    
if __name__ == '__main__':
    manager.run()