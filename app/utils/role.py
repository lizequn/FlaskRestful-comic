from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_claims, get_current_user
from .abort import abort
from ..models.auth import User


def claim_role_required(allow_list, skip=False):
    def role_verify(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            verify_jwt_in_request()
            if skip:
                return func(*args,**kwargs)
            claims = get_jwt_claims()
            num = len(set(allow_list).intersection(claims['roles']))
            if num == 0:
                return abort(401, message='User role error')
            else:
                return func(*args,**kwargs)
        return wrapper
    return role_verify


def db_role_required(allow_list, skip=False):
    def role_verify(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            verify_jwt_in_request()
            if skip:
                return func(*args,**kwargs)
            user = User.find_by_id(get_current_user())
            roles = [role.id for role in user.roles]
            num = len(set(allow_list).intersection(roles))
            if num == 0:
                return abort(401, message='User role error')
            else:
                return func(*args,**kwargs)
        return wrapper
    return role_verify

