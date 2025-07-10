from flask import Blueprint, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import Booking, Car
from .. import db

bookings = Blueprint('bookings', __name__)

@bookings.route('/book/<int:car_id>', methods=['POST'])
@login_required
def book_car(car_id):
    start = request.form['start_date']
    end = request.form['end_date']
    booking = Booking(
        car_id=car_id,
        user_id=current_user.id,
        start_date=start,
        end_date=end
    )
    db.session.add(booking)
    db.session.commit()
    return redirect(url_for('listings.index'))
