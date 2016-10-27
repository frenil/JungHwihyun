import random
import json
import os

from pico2d import *

import Dall
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
    global back, player, dall
    global LKeyco, RKeyco
    RKeyco, LKeyco = 0, 0

    back = Back()
    player = Player.Ragna()
    dall = Dall.dall()


def exit():
    global back, player, dall
    del(back)
    del(player)
    del (dall)


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
    dall.update()
    if dall.x<player.x and dall.ishit==False:
        dall.see=1
    elif dall.x>=player.x and dall.ishit==False:
        dall.see=-1
    if collide(player,dall) == True:
        dall.state  = 1
        dall.frame=0
        if player.state==4:
            dall.Xhit = 20
            dall.Yhit=15
        elif player.state==41:
            dall.Xhit = 10
            dall.Yhit=15
        elif player.state== 82:
            dall.Xhit = 4
            dall.Yhit = 30
        elif player.state == 823:
            dall.Xhit = 4
            dall.Yhit = -60
        else:
            dall.Xhit = 4
            dall.Yhit=15
        dall.see = player.see* -1
        dall.ishit =True
    delay(0.1)

def collide(player,dall):
    left_a, bottom_a, right_a, top_a = player.get_bb()
    left_b, bottom_b, right_b, top_b = dall.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def draw():
   clear_canvas()
   back.draw()
   dall.draw()
   player.draw()
   player.get_Rect()
   dall.get_Rect()

   update_canvas()





