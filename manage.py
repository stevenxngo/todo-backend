from flask_script import Manager
from app import create_app, db
from flask_migrate import MigrateCommand

app = create_app()
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
