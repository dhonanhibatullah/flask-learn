from utils.password import pass_hasher

class UserModel:
    def __init__(self, username: str, password: str, name: str, email: str, phone_number: str = '') -> None:
        self.username       = username
        self.passhash       = pass_hasher(password)
        self.name           = name
        self.email          = email
        self.phone_number   = phone_number

    def get_dict(self) -> dict:
        return {
            'username': self.username,
            'passhash': self.passhash,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number
        }