from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from sac import config
from sac import util
from datetime import datetime
import sys

def draw_on_pic(img, app_time, app_name):
    draw = ImageDraw.Draw(img)
    font_app_time = ImageFont.truetype(config.DEFAULT_FONT, config.FONT_TIME_SIZE)
    font_app_name = ImageFont.truetype(config.DEFAULT_FONT, config.FONT_NAME_SIZE)
    draw.text(config.FONT_TIME_LOC, app_time,config.FONT_TIME_COLOR, font=font_app_time)
    draw.text(config.FONT_NAME_LOC, app_name, config.FONT_NAME_COLOR, font=font_app_name)
    return img

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Call %(name)s destination\ne.g. %(name)s /tmp/mypic.bmp" % {"name" : sys.argv[0]})
        sys.exit(1)
    img = Image.open(config.BACKGROUND_IMG)
    client = util.get_default_client()
    app = client.get_next_appointment()
    app_name = app['appointment']['name']
    app_time = datetime.fromtimestamp(app['appointment']['time'])
    app_time_str = app_time.strftime("%H:%M") 
    img = draw_on_pic(img, app_time_str, app_name)
    img.save(sys.argv[1])
