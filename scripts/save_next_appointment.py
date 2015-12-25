#!/opt/sac/bin/python
from sac import util
from sac import config

util.save_appointment_to_file(config.APP_CACHE_PATH, config.APP_ERROR_PATH)