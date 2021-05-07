from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User,Seller,Product,Orders,Cart



# ...
# Creating app instance

app = create_app('development')

# app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User=User,Seller=Seller,Product=Product,Orders=Orders,Cart=Cart)


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'any secret string'
    manager.run()
