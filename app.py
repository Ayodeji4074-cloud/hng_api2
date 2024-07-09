from flask import Flask
from config import Config
from models import db, bcrypt
from routes import auth_blueprint, org_blueprint
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(org_blueprint, url_prefix='/api/organisations')


@app.route('/')
def index():
    return "Welcome to the API!"

if __name__ == '__main__':
    app.run(debug=True)
