import os
from base64 import b64encode
import com
import config

DEVICE_ID_FILE_NAME = "/opt/sac/device_id"
SECRET_FILE_NAME = "/opt/sac/secret"

DEF_SECRET_LENGTH = 26

def is_registered():
    """
    raises NoInternet in case there is ... no internet
    """
    client = com.Client(
            get_device_id(),
            get_secret(),
            config.API_SERVER,
            config.CERT_PATH
    )
    return client.connection_works() 

def __read_return(file_name):
    with open(file_name) as f:
        return f.read()

def get_device_id():
    return __read_return(DEVICE_ID_FILE_NAME)

def get_secret():
    try:
        return __read_return(SECRET_FILE_NAME)
    except IOError:
        return create_secret()

def create_secret():
    secret = b64encode(os.urandom(DEF_SECRET_LENGTH))
    with open(SECRET_FILE_NAME, "w") as f:
        f.write(secret)
    return secret

def get_default_client():
    return com.Client(get_device_id(), get_secret(), config.API_SERVER, config.CERT_PATH)
