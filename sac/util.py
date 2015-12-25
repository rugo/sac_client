import os
from base64 import b64encode
import com
import config
import json

DEVICE_ID_FILE_NAME = "/opt/sac/device_id"
SECRET_FILE_NAME = "/opt/sac/secret"

DEF_SECRET_LENGTH = 26

errorMsg = {
    com.NoInternet: config.ERR_NO_INET,
    com.BadResponse: config.ERR_BAD_RESP,
    com.NoAppointments: config.ERR_NO_APPS
}

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

def __str_to_uni(text):
    text = text.decode(config.TEXT_ENCODING)
    if isinstance(text, str):
        text = unicode(text, config.TEXT_ENCODING)
    elif isinstance(text, unicode):
        text = text.encode(config.TEXT_ENCODING)
    return text

def encode_output(text):
    return __str_to_uni(text)

def decode_input(text):
    return __str_to_uni(text)

def save_appointment_to_file(file_name, error_file_name):  
    try:
        app_json = get_default_client().get_next_appointment_raw()

        with open(file_name, "w") as f:
            f.write(encode_output(app_json))

    except com.ClientException as ex:
        try:
            msg = errorMsg[type(ex)]
        except KeyError:
            msg = config.ERR_UNHANDELED

        with open(error_file_name, "w") as f:
            f.write(encode_output(msg))

def get_appointment_from_file(file_name, error_file_name):
    """
    Returns tuple (appointment_dict, error_str)
    appointment_dict might be empty in case of serious error
    """
    try:
        with open(file_name) as f:
            app = json.loads(decode_input(f.read()))

        # we need to return the error as well if the error is newer
        # than the cached appointment
        error = ""
        if os.path.getctime(error_file_name) >= os.path.getctime(file_name):
            with open(error_file_name) as f:
                error = decode_input(f.read())

        return app, error
    except IOError as e:
        # in case no cache was ever written (yet)
        # we inform about not beeing set up yet
        if not os.path.isfile(file_name):
            return {}, config.ERR_NOT_SETUP
        else:  # otherwise: no clue what happend
            return {}, config.ERR_UNHANDELED
    except Exception as e:
        print(e)
        return {}, unicode(type(e))