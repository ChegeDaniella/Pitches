from app import create_app
from flask_script import Manager,Server
from app.models import User,Pitches,Comments
from app import db
from flask_migrate import Migrate,MigrateCommand

#create app instance
app = create_app('development')
# app = create_app('test')

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
    return dict(app = app,db = db, User = User, Pitches = Pitches, Comments = Comments)
    
# if __name__ == '__main__':
#     manager.run()