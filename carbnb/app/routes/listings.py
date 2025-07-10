from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import Car
from .. import db

listings = Blueprint('listings', __name__)

@listings.route('/')
def index():
    cars = Car.query.all()
    return render_template('index.html', cars=cars)

@listings.route('/car/<int:car_id>')
def car_detail(car_id):
    car = Car.query.get_or_404(car_id)
    return render_template('car_detail.html', car=car)

@listings.route('/add', methods=['GET', 'POST'])
@login_required
def add_car():
    if request.method == 'POST':
        # create and save car
        ...
    return render_template('add_car.html')
