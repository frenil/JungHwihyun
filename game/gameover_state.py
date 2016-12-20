import game_framework
import Ranking_state
import LoadRe
from pico2d import *

name = "TitleState"
image = None
overcount=0

def enter():
    global image
    global overcount
    overcount = 0

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key)== (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()

def draw():
    clear_canvas()
    LoadRe.back.Game_over.clip_draw_to_origin(0, 0, 1280, 720, 0, 0)
    update_canvas()


def update():
    global overcount
    overcount+=1
    if 50<overcount:
        game_framework.change_state(Ranking_state)


def pause():
    pass


def resume():
    pass






