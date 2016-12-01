from pico2d import *
import LoadRe

class Background:
    def __init__(self):
        self.width = 1600
        self.height = 800
    def draw(self):
        LoadRe.back.back_1.clip_draw_to_origin(0, 0, self.width,self.height,0,0)
