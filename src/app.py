from database.engine import SessionLocal
from database.models import Car

with SessionLocal() as session:
	stmt = Car(brand='Toyota', model='Camry', price=3000000, dealer_id=2)
	session.add(stmt)
	session.commit()
	# Этот код был создан на ветке expirience/other