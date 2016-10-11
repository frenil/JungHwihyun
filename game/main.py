from pico2d import *
import Player

def handle_events():
    global running
    global next
    global Ldown, Rdown
    global see
    global Ldouble,Rdouble
    global LKeyco, RKeyco
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_a :
                next = 1
            if event.key == SDLK_LEFT:
                Ldown = True
                see = -1
                if LKeyco < 5:
                    Ldouble = True
            if event.key == SDLK_RIGHT:
                Rdown = True
                see = 1
                if RKeyco < 5:
                    Rdouble = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                Ldown = False
                if Rdown == True:
                    see = 1
                if Ldouble == True:
                    LKeyco =0
            if event.key== SDLK_RIGHT:
                Rdown = False
                if Ldown == True:
                    see = -1
                if Rdouble == True:
                    RKeyco =0

open_canvas(1800,800)

player = Player.Ragna()
state =0
running = True
stcount = 0
next = 0
frame=0
see =1
LKeyco , RKeyco = 0 , 0
Ldouble, Rdouble = False, False
Ldown, Rdown = False, False
walking =False
while running:
    handle_events()
    player.see = see
    if Ldown == False and Rdown == False:
        walking = False
    if player.state == 0 :
        if Ldown == True or Rdown == True:
            walking = True
        if next==0 and walking == True:
            player.state = 3
            player.see = see
        elif next == 1:
            player.state = 2
            next = 0
            player.frame = 0
            frame = 0
    elif player.state == 3 :
        if walking == False:
            player.walkframe =0
            player.state =0
            player.frame=0
            frame =0
        elif frame<5 and (Rdouble== True or Ldouble==True):
            player.state = 4
            player.frame = 0
            next=0
            frame=0
    elif player.state ==2 and frame==5:
        if next == 0:
            player.state = 0
        elif next == 1 :
            player.state = 211
        next = 0
        player.frame = 0
        frame=0
    elif player.state ==211and frame == 17:
        if next == 0:
            player.state = 0
        elif next == 1 :
            player.state = 212
        player.frame = 0
        next = 0
        frame=0
    elif player.state ==212 and frame ==16:
        if next == 0:
            player.state = 0
        elif next == 1:
            player.state = 213
        player.frame = 0
        frame=0
        next=0
    elif  player.state == 213and frame ==20:
        player.state=0
        player.frame = 0
        frame=0
        next=0
    elif player.state == 4:
        if frame==18:
            player.state=0
            player.frame = 0
            frame=0
            next=0
    player.update()
    frame +=1
    clear_canvas()

    player.draw()

    update_canvas()
    delay(0.04)

close_canvas()

