from app import create_app
from flask_script import Manager,Server

# from  flask_migrate import Migrate, MigrateCommand
# Import models



# ...
# Creating app instance

app = create_app('development')

# app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)

# @manager.shell
# def make_shell_context():
#     return dict(app = app,db = db,Todo = Todo )







if __name__ == '__main__':
    manager.run()
