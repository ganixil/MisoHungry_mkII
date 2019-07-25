import os

from flask import Flask
from . import main
def create_app(test_config=None):
	#create and configure the application
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY = 'dev',
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
		)

	if test_config is None:
		app.config.from_pyfile('config.py',silent=True)
	else:
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	app.register_blueprint(main.bp)
	return app