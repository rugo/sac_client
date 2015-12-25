# encoding: utf-8

# Communication
CERT_PATH = "/opt/sac/keys/cert.pem"
API_SERVER = "comfortaable.com:1443"
REQUEST_TIMEOUT = 3

# Stuff
TEXT_ENCODING = "utf-8"

# Desgin config
BACKGROUND_IMG = "/opt/sac/res/background.bmp"
APP_CACHE_IMG = "/tmp/sac_app.bmp"
DEFAULT_FONT = "/opt/sac/res/deja_serif.ttf"
FONT_TIME_SIZE = 100
FONT_NAME_SIZE = 18

FONT_TIME_LOC = (15, 55)
FONT_NAME_LOC = (25, 165)

FONT_TIME_COLOR = (255, 0, 0)
FONT_NAME_COLOR = (255, 0, 0)

# Errors to appear on screen
ERR_NO_INET = u"No internet connection"
ERR_BAD_RESP = u"Communication error"
ERR_UNHANDELED = u"Encountered errors"

# Paths to cache data (should be in /tmp)
APP_CACHE_PATH = "/tmp/sac_next_app.json"
APP_ERROR_PATH = "/tmp/sac_next_app_error.txt"