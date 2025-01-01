import bcrypt

def pass_hasher(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def pass_checker(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())