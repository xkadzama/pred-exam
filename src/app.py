from flask import Flask, render_template
from dealer.routes import dealer_bp


app = Flask(__name__)


app.register_blueprint(dealer_bp)


if __name__ == '__main__':
	app.run(debug=True, port=2000)