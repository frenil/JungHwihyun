import game_framework
import main_state
import title_state
import LoadRe
from pico2d import *

image = None


def enter():
    global font
    font= load_font('ENCR10B.TTF', 80)

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
    global font
    clear_canvas()
    LoadRe.back.rank.clip_draw_to_origin(0, 0, 1280, 720, 0, 0)

    if main_state.totalpoint<=200:
        LoadRe.back.tier.clip_draw_to_origin(0, 150, 150, 150, 420, 200, 450,450)
        font.draw(50, 150, "YOU ARE BRONZE PLAYER", (153, 56, 0))
    elif main_state.totalpoint<=500:
        LoadRe.back.tier.clip_draw_to_origin(150, 150, 150, 150, 420, 200, 450,450)
        font.draw(50, 150, "YOU ARE SILVER PLAYER", (213,213,213))
    elif main_state.totalpoint<=1000:
        LoadRe.back.tier.clip_draw_to_origin(300, 150, 150, 150, 420, 200, 450,450)
        font.draw(50, 150, "YOU ARE GOLD PLAYER", (250,237,125))
    elif main_state.totalpoint<=1500:
        LoadRe.back.tier.clip_draw_to_origin(450, 150, 150, 150, 420, 200, 450,450)
        font.draw(50, 150, "YOU ARE PLATINUM PLAYER", (212,244,250))
    elif main_state.totalpoint<=2000:
        LoadRe.back.tier.clip_draw_to_origin(0, 0, 150, 150, 420, 200, 450, 450)
        font.draw(50, 150, "YOU ARE DIAMIND PLAYER", (178, 204, 255))
    else:
        LoadRe.back.tier.clip_draw_to_origin(450, 0, 150, 150, 420, 200,450,450)
        font.draw(50, 150, "YOU ARE MASTER PLAYER", (255,255,36))

    update_canvas()

def update():
    pass


def pause():
    pass


def resume():
    pass
