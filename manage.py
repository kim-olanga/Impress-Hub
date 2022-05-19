from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand



from app.models import User,Pitch

# Creating app instance
app = create_app('development')
# app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server) # launch the server to run application
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

#FlaskScript shell
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Pitch = Pitch)
if __name__ == '__main__':
    app.config['SECRET_KEY']='iamhonestlyexhautedlikedamn'
    manager.run()