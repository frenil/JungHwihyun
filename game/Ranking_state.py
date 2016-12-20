import game_framework
import main_state
import title_state
import LoadRe
from pico2d import *

name = "TitleState"
image = None


def enter():
    pass

def exit():
    pass
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key)== (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN,SDLK_SPACE ):
                game_framework.change_state(title_state)

def draw():
    clear_canvas()
    LoadRe.back.rank.clip_draw_to_origin(0, 0, 1280, 720, 0, 0)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
