import game_framework
import main_state
from pico2d import *
import tutorial_state

name = "TitleState"
image = None


def enter():
    global image,pimage
    image = load_image('title.png')
    pimage = load_image('press.png')


def exit():
    global image,pimage
    del(image)
    del(pimage)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key)== (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN,SDLK_SPACE ):
                game_framework.change_state(tutorial_state)

def draw():
    clear_canvas()
    image.draw(640,360)
    pimage.draw(640,100)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






