import game_framework
from pico2d import *
import start_state
import LoadRe

PIXEL_PER_METER = (100.0 / 0.8)           #100픽셀 0.8m


open_canvas(1280,720,sync = True)           #10.24m * 5.76m

image = load_image('title.png')
image.draw_now(640,360)
LoadRe.Loading()
game_framework.run(start_state)

