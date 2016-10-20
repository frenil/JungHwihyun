import random
import json
import os

from pico2d import *

import Player
import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None


class Back:
    def __init__(self):
        self.image = load_image('back.png')

    def draw(self):
        self.image.draw(600, 400)


def enter():
    global back, player
    global LKeyco, RKeyco
    RKeyco, LKeyco = 0, 0

    back = Back()
    player = Player.Ragna()


def exit():
    global back, player
    del(back)
    del(player)


def pause():
    pass


def resume():
    pass


def handle_events():
    global LKeyco, RKeyco
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.change_state(title_state)
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_a :
                player.next = 1
            if event.key == SDLK_LEFT:
                player.Ldown = True
                if player.state == 0 or player.state == 3:
                    player.see = -1
                if LKeyco < 5:
                    player.Ldouble = True
            if event.key == SDLK_RIGHT:
                player.Rdown = True
                if player.state == 0 or player.state == 3:
                    player.see = 1
                if RKeyco < 5:
                    player.Rdouble = True
            if event.key == SDLK_UP:
                player.next=8
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                player.Ldown = False
                LKeyco =0
            if event.key== SDLK_RIGHT:
                player.Rdown = False
                RKeyco =0


def update():
    global LKeyco, RKeyco
    if player.Ldown == False:
        LKeyco = LKeyco + 1
    if player.Rdown == False:
        RKeyco = RKeyco + 1

    player.update()

    delay(0.04)

def draw():
   clear_canvas()
   back.draw()
   player.draw()
   update_canvas()





