from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


# verifies the user's input and the hashed password by hashing the user input and comparing
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
