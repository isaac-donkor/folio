from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from .models import Car, db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# --- Car List Resource ---
class CarListResource(Resource):
    def get(self):
        cars = Car.query.all()
        return [{
            "id": c.id,
            "title": c.title,
            "description": c.description,
            "price_per_day": c.price_per_day
        } for c in cars], 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('price_per_day', type=float, required=True)
        parser.add_argument('owner_id', type=int, required=True)
        args = parser.parse_args()

        car = Car(**args)
        db.session.add(car)
        db.session.commit()
        return {"message": "Car added", "car_id": car.id}, 201

# --- Single Car Resource ---
class CarResource(Resource):
    def get(self, car_id):
        car = Car.query.get_or_404(car_id)
        return {
            "id": car.id,
            "title": car.title,
            "description": car.description,
            "price_per_day": car.price_per_day
        }

    def delete(self, car_id):
        car = Car.query.get_or_404(car_id)
        db.session.delete(car)
        db.session.commit()
        return {"message": "Car deleted"}

# Registering API resources
api.add_resource(CarListResource, '/api/cars')
api.add_resource(CarResource, '/api/cars/<int:car_id>')
