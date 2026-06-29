from flask import Blueprint, render_template

from database.engine import SessionLocal
from database.models import Car, CarDealer


dealer_bp = Blueprint('dealer', __name__, template_folder='templates')


@dealer_bp.route('/')
def get_all_dealers():
	with SessionLocal() as session:
		dealers = session.query(CarDealer).all()
		print(dealers)
	return render_template('all_dealers.html', dealers=dealers)


@dealer_bp.route('/dealer/<int:id>')
def cars_by_dealer(id):
	with SessionLocal() as session:
		cars = session.query(Car).filter_by(dealer_id=id).all()
		print(cars)
	return render_template('cars_by_dealer.html', cars=cars)


# /dealer/2/add -> GET, POST
# /car/13/delete

