import random
import json
import os

from pico2d import *

import Dall
import Player
import game_framework
import title_state
import Stage_set
import main_state_2
import main_state


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
    global back, player, dalls
    global LKeyco, RKeyco
    global count
    count=0
    RKeyco, LKeyco = 0, 0
    stage = Stage_set.stage()
    stage.update(1)
    back = Back()
    player = Player.Ragna()
    player.x = stage.Playerx
    dalls = [Dall.dall() for i in range(10)]
    j=0
    for dall in dalls:
        dall.x = stage.dallx[j]
        dall.HP = stage.dall_HP
        dall.Wsp = Dall.Speed(stage.speed[j])
        j += 1

def exit():
    global back, player, dall
    del(back)
    del(player)
    for dall in dalls:
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
            elif event.key == SDLK_z :
                player.state = player.HIT
                player.total_frames = 0
            elif event.key == SDLK_1:
                game_framework.change_state(main_state)
            elif event.key == SDLK_2:
                game_framework.change_state(main_state_2)

            if event.key == SDLK_LEFT:
                player.Ldown = True
                if player.state == 0 or player.state == 3:
                    player.see = -1
                if LKeyco < 10:
                    player.Ldouble = True
            if event.key == SDLK_RIGHT:
                player.Rdown = True
                if player.state == 0 or player.state == 3:
                    player.see = 1
                if RKeyco < 10:
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
    global count
    if player.Ldown == False:
        LKeyco = LKeyco + 1
    if player.Rdown == False:
        RKeyco = RKeyco + 1
    player.update()
    for dall in dalls:
        dall.update()
        if(player.x-dall.x)*(player.x-dall.x)<20000:
            dall.isP=True
        else:
            dall.isP = False
        if dall.x<player.x and dall.ishit==False:
            dall.see=1
        elif dall.x>=player.x and dall.ishit==False:
            dall.see=-1
        if collide(player.A_get_bb(),dall.H_get_bb()) == True:
            dall.state  = 1
            dall.total_frames=0
            dall.frame=0
            if player.state==4:
                dall.hitxSp = 25
                dall.hitySp=5
                dall.HP-=30
            elif player.state==41:
                dall.hitxSp = 10
                dall.hitySp = 5
                dall.HP-=20
            elif player.state== player.UPPER:
                dall.hitxSp = 5
                dall.hitySp = 13
                dall.HP -=15
            elif player.state == 823:
                dall.hitxSp = 5
                dall.hitySp = -30
                dall.HP -=20
            else:
                dall.hitxSp = 15
                dall.hitySp=7
                dall.HP -=50
            dall.see = player.see* -1
            dall.ishit =True
        if collide(player.H_get_bb(),dall.A_get_bb()) == True:
            player.state = player.HIT
            player.total_frames = 0
            player.frame = 0
            player.see = dall.see * -1
            player.HP -= 50
        if dall.HP<=0 and dall.state==1 and dall.frame==7:
            dalls.remove(dall)

def collide(player,dall):
    left_a, bottom_a, right_a, top_a = player
    left_b, bottom_b, right_b, top_b = dall
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def draw():
   clear_canvas()
   back.draw()

   for dall in dalls:
       dall.draw()
   player.draw()
   player.get_Rect()
   for dall in dalls:
       dall.get_Rect()

   update_canvas()





