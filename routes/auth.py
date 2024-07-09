from flask import Blueprint, request, jsonify
from models import db, User, bcrypt
from flask_jwt_extended import create_access_token

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(
        userId=data['userId'],
        firstName=data['firstName'],
        lastName=data['lastName'],
        email=data['email'],
        password=bcrypt.generate_password_hash(data['password']).decode('utf-8'),
        phone=data['phone']
    )
    db.session.add(user)
    db.session.commit()
    access_token = create_access_token(identity={'userId': user.userId, 'email': user.email})
    return jsonify({
        'status': 'success',
        'message': 'Registration successful',
        'data': {
            'accessToken': access_token,
            'user': {
                'userId': user.userId,
                'firstName': user.firstName,
                'lastName': user.lastName,
                'email': user.email,
                'phone': user.phone
            }
        }
    }), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'userId': user.userId, 'email': user.email})
        return jsonify({
            'status': 'success',
            'message': 'Login successful',
            'data': {
                'accessToken': access_token,
                'user': {
                    'userId': user.userId,
                    'firstName': user.firstName,
                    'lastName': user.lastName,
                    'email': user.email,
                    'phone': user.phone
                }
            }
        }), 200
    return jsonify({'status': 'Bad request', 'message': 'Authentication failed', 'statusCode': 401}), 401
