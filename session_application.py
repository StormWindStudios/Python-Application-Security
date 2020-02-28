from flask import Flask, render_template
from flask_security import Security, SQLAlchemySessionUserDatastore, \
    login_required

from database import db_session, init_db
from models import User, Role

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'averysecurekey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SECURITY_PASSWORD_SALT'] = 'egb43uigf43iugbguh'

user_datastore = SQLAlchemySessionUserDatastore(
    db_session,
    User,
    Role
)

security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    init_db()
    user_datastore.create_user(
        email='zac@stormwind.com',
        password='securepassword'
    )
    db_session.commit()

@app.route('/')
@login_required
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
