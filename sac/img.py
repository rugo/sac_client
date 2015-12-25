from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import config
from datetime import datetime

def _draw_on_pic(img, app_time, app_name, error):
    """
    Draws strings on img.
    @param img: PIL Image
    @return image with strings on it.
    """
    draw = ImageDraw.Draw(img)
    font_app_time = ImageFont.truetype(config.DEFAULT_FONT, config.FONT_TIME_SIZE)
    font_app_name = ImageFont.truetype(config.DEFAULT_FONT, config.FONT_NAME_SIZE)
    draw.text(config.FONT_TIME_LOC, app_time,config.FONT_TIME_COLOR, font=font_app_time)
    draw.text(config.FONT_NAME_LOC, app_name, config.FONT_NAME_COLOR, font=font_app_name)
    return img

def draw_appointment(backg_img, dst_img, app, error=""):
    """
    @param backg_img: Path to background image
    @param dst_img: Path to save output image to
    @param app: Python dict with app info
    @param error: Error text in case error occured
    """
    app_name = app['appointment']['name']
    app_time = datetime.fromtimestamp(app['appointment']['time'])
    app_time_str = app_time.strftime("%H:%M") 
    img = _draw_on_pic(Image.open(backg_img), app_time_str, app_name, error)
    img.save(dst_img)