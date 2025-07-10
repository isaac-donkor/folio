from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import User, Car, Booking

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carbnb.db'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .routes.auth import auth as auth_bp
    from .routes.listings import listings as listings_bp
    from .routes.bookings import bookings as bookings_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(listings_bp)
    app.register_blueprint(bookings_bp)


    from . import models

    admin = Admin(app, name="Carbnb Admin", template_mode='bootstrap4')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Car, db.session))
    admin.add_view(ModelView(Booking, db.session))
    return app
