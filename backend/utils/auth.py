from jose import jwt
from utils.security import SECRET_KEY, ALGORITHM

def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
