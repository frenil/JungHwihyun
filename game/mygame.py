import game_framework
from pico2d import *
import start_state
import LoadRe


open_canvas(1280,720)

image = load_image('title.png')
image.draw_now(640,360)
LoadRe.Loading()
game_framework.run(start_state)

