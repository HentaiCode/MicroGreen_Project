from flask import Flask
from flask_login import LoginManager

from database.manage import init_db
from blueprints import MicroGreen, users, admins
from database.repositories import users_rep, admins_rep
import os

from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(MicroGreen)
app.register_blueprint(admins)
app.register_blueprint(users)

login_manager = LoginManager()
login_manager.init_app(app)
init_db()


@login_manager.user_loader
def load_user(user_id):
    return users_rep.get_user_by_id(user_id)


@login_manager.user_loader
def load_admin(admin_id):
    return admins_rep.get_admin_by_id(admin_id)


if __name__ == '__main__':
    app.run()
