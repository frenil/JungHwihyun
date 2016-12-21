import game_framework
import main_state
import Ranking_state
import help_state
import LoadRe
from pico2d import *

name = "TitleState"
image = None


def enter():
    global image,font, music
    music = LoadRe.sound.title_bgm
    image = load_image('title.png')
    font = load_font('ENCR10B.TTF', 50)
    music.repeat_play()

def exit():
    global image,font, music
    music.stop()
    del(image)
    del(font)
    del(music)

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
            elif (event.type, event.key) == (SDL_KEYDOWN,SDLK_i ):
                game_framework.change_state(help_state)

def draw():
    clear_canvas()
    image.draw(640,360)
    font.draw(340,150,"press space to start",(255,0,0))
    font.draw(400,100,"press i to help",(255,0,0))
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






