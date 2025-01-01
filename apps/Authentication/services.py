from utils.mongodb import get_db
from utils.password import pass_checker
from apps.Shared.types import ServiceReturnType
from apps.Authentication.models import UserModel

class AuthService:

    def __init__(self):
        self.db = get_db()

    def register(self, data: dict) -> ServiceReturnType:
        try:
            new_user = UserModel(
                data['username'],
                data['password'],
                data['name'],
                data['email'],
                data['phone_number']
            )
            self.db['users'].insert_one(new_user.get_dict())
            return ServiceReturnType(
                is_err  = False,
                msg     = 'OK',
                data    = None,
                code    = 200
            )
        except:
            return ServiceReturnType(
                is_err  = True,
                msg     = 'Invalid data',
                data    = None,
                code    = 400
            )

    def login(self, data: dict) -> ServiceReturnType:
        try:
            user = self.db['users'].find_one({'username': data['username']})
            if not pass_checker(data['password'], user['passhash']):
                return ServiceReturnType(
                    is_err  = True,
                    msg     = 'Invalid password',
                    data    = None,
                    code    = 401
                )
            else:
                return ServiceReturnType(
                    is_err  = False,
                    msg     = 'OK',
                    data    = None,
                    code    = 200
                )
        except:
            return ServiceReturnType(
                is_err  = True,
                msg     = 'Invalid data',
                data    = None,
                code    = 400
            )