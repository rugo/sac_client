import os
from base64 import b64encode

DEVICE_ID_FILE_NAME = "/etc/sac/device_id"
SECRET_FILE_NAME = "/etc/sac/secret"
DEF_SECRET_LENGTH = 26

def is_registered():
    return os.path.exists(SECRET_FILE_NAME)

def __read_return(file_name):
    with open(file_name) as f:
        return f.read()

def get_device_id():
    return __read_return(DEVICE_ID_FILE_NAME)

def get_secret():
    return __read_return(SECRET_FILE_NAME)

def create_secret():
    secret = b64encode(os.urandom(DEF_SECRET_LENGTH))
    with open(SECRET_FILE_NAME, "w") as f:
        f.write(secret)
    return secret