from sac import util
from sac import img
from sac import config

def main():
    app, error = util.get_appointment_from_file(config.APP_CACHE_PATH, config.APP_ERROR_PATH)

    if app:
        img.draw_appointment(config.BACKGROUND_IMG, config.APP_CACHE_IMG, app, error)
    else:
        raise ValueError("No appointment in cache file!") # wtf?

if __name__ == '__main__':
    main()
