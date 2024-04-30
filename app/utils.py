from passlib.context import CryptContext


# here we are telling passlib what the default hashing algorithm is.
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)