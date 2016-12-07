
import platform
import os
if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"


import game_framework
from pico2d import *
import start_state
import LoadRe

PIXEL_PER_METER = (100.0 / 0.8)             #100픽셀 0.8m


open_canvas(1280,720,sync = True)           #10.24m * 5.76m


LoadRe.Loading()
game_framework.run(start_state)

