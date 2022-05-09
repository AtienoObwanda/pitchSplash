from flask_script import Manager, Server
from  flask_migrate import Migrate, MigrateCommand

from app import create_app,db


from app.models import User, Pitch, Comment


# App instance -> creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User, Pitch=Pitch, Comment=Comment)


migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)




if __name__ == '__main__':
    manager.run()