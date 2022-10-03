import uuid
from flask import request, jsonify
from flask.views import MethodView
from webargs import fields
from webargs.flaskparser import parser
from flask_jwt_extended import create_access_token, \
    get_jwt_identity, \
    jwt_required, get_jwt_claims
from werkzeug.security import safe_str_cmp
from app.main import secret_key, jwt, ma
from ..models.auth import User, Role, RolesUsers
from ..utils.role import claim_role_required
from ..utils.abort import abort


@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'roles': [role.id for role in user.roles]}


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


class RoleResource(MethodView):
    class RoleSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = Role
        id = ma.auto_field()
        name = ma.auto_field()
        description = ma.auto_field()

    request_fields = {
        'name': fields.Str(required=True),
        'description': fields.Str(required=True)
    }

    def __init__(self):
        self.roleSchema = self.RoleSchema(many=True)

    @claim_role_required(allow_list=[999])
    def get(self):
        roles = Role.find_all()
        print(roles)
        result = self.roleSchema.dump(roles)
        return jsonify(result)

    @claim_role_required(allow_list=[999])
    def post(self):
        data = parser.parse(self.request_fields, request)
        if Role.find_by_name(data['name']):
            return {'message': 'role name already existed'}, 409
        role = Role(**data)
        try:
            role.save()
        except TypeError as e:
            return abort(500, message=str(e))
        return {'message': 'success'}, 201


class UserResource(MethodView):
    class UserSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            model = User

        id = ma.auto_field()
        username = ma.auto_field()
        roles = ma.Nested(RoleResource.RoleSchema, many=True)

    request_fields = {
        'username': fields.Str(required=True),
        'password': fields.Str(required=True)
    }

    def __init__(self):
        self.userSchema = self.UserSchema()

    def post(self):
        data = parser.parse(self.request_fields, request)
        user = User.authenticate(username=data['username'], password=data['password'])
        if user:
            access_token = create_access_token(identity=user)
            return {'access_token': access_token,
                    'id': user.id}, 201
        return abort(401, message='Bad username or password')

    @claim_role_required(allow_list=[], skip=True)
    def get(self):
        current_user = get_jwt_identity()
        user = User.find_by_id(current_user)
        if user is None:
            return abort(404, message="bad User Information")
        return self.userSchema.dump(user)


class RegisterResource(MethodView):
    request_fields = {
        'username': fields.Str(required=True),
        'password': fields.Str(required=True),
        'role_id': fields.Int(required=False)
    }

    def post(self, key):
        if not safe_str_cmp(secret_key, key):
            return abort(400, message='wrong secret key ' + str(key))
        data = parser.parse(self.request_fields, request)
        if not User.find_by_username(data['username']):
            if data['role_id'] is not None:
                role = Role.find_by_id(data['role_id'])
                if role is None:
                    return {'message': 'role_id does not exist in system'}, 409
                data['roles'] = [role]
            data['id'] = str(uuid.uuid4())
            data.pop('role_id', None)
            user = User(**data)
            try:
                user.save()
            except TypeError as e:
                return abort(500, message=str(e))
        else:
            return {'message': 'user already existed'}, 409
        return {'message': 'success'}, 201
