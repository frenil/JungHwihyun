import game_framework
from pico2d import *
import start_state
import LoadRe

PIXEL_PER_METER = (100.0 / 1)           #100픽셀 1m


open_canvas(1280,720,sync = True)

image = load_image('title.png')
image.draw_now(640,360)
LoadRe.Loading()
game_framework.run(start_state)

