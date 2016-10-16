import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0

def enter():
    global image
    global WW
    global WH
    WW, WH = 1280, 720

    open_canvas(WW,WH)
    image = load_image('title.png')

def exit():
    global  image
    del(image)
    close_canvas()


def update():
    global logo_time

    if logo_time> 1.0:
        logo_time = 0
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    global WW
    global WH
    clear_canvas()
    image.draw(640,360)
    update_canvas()



def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




