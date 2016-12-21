import game_framework
import main_state
import LoadRe
from pico2d import *

name = "TitleState"
image = None


def enter():
    global image,font
    image = load_image('title.png')
    font = load_font('ENCR10B.TTF', 50)


def exit():
    global image,font
    del(image)
    del(font)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key)== (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN,SDLK_SPACE ):
                game_framework.change_state(main_state)

def draw():
    clear_canvas()
    LoadRe.back.help_back.clip_draw_to_origin(0, 0, 1280, 720, 0, 0)
    font.draw(340,100,"press space to start",(255,0,0))
    font.draw(10,650,"UPcom",(255,255,0))
    font.draw(10,600,"a-up-a-a-a",(255,255,0))
    font.draw(10, 450, "NOMALcom", (255, 255, 0))
    font.draw(10, 400, "a-a-a-a", (255, 255, 0))
    font.draw(10, 250, "DASHcom", (255, 255, 0))
    font.draw(10, 200, "->-> - a", (255, 255, 0))

    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






