import os

DEVICE_ID_FILE_NAME = "/etc/sac/device_id"
SECRET_FILE_NAME = "/etc/sac/secret"
DEF_SECRET_LENGTH = 26

def is_registered():
    return os.path.exists(SECRET_FILE_NAME)

def __readAndReturn(file_name):
    with open(DEVICE_ID_FILE_NAME) as f:
        return f.read()

def get_device_id():
    __readAndReturn(DEVICE_ID_FILE_NAME)

def get_secret():
    __readAndReturn(SECRET_FILE_NAME)

def create_secret():
    return os.urandom(DEF_SECRET_LENGTH)