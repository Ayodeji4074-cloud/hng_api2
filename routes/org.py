from flask import Blueprint, request, jsonify
from models import db, Organisation
from flask_jwt_extended import jwt_required, get_jwt_identity

org_blueprint = Blueprint('org', __name__)

@org_blueprint.route('/', methods=['POST'])
@jwt_required
def create_org():
    data = request.get_json()
    user = get_jwt_identity()
    org = Organisation(
        orgId=data['orgId'],
        name=data['name'],
        description=data['description']
    )
    db.session.add(org)
    db.session.commit()
    return jsonify({
        'status': 'success',
        'message': 'Organisation created successfully',
        'data': {
            'orgId': org.orgId,
            'name': org.name,
            'description': org.description
        }
    }), 201
