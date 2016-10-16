from pico2d import *
import Player
WW,WH = 1200, 800
def handle_events():
    global running
    global next
    global Ldown, Rdown
    events = get_events()
    for event in events:
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
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                player.Ldown = False
                LKeyco =0
            if event.key== SDLK_RIGHT:
                player.Rdown = False
                RKeyco =0

def main_update():
    global next, see
    global LKeyco, RKeyco
    global Rdouble,Ldouble
    LKeyco = LKeyco + 1
    RKeyco = RKeyco + 1

open_canvas(WW,WH)

player = Player.Ragna()
state =0
running = True
stcount = 0
LKeyco , RKeyco = 0 , 0
Ldouble, Rdouble = False, False
Ldown, Rdown = False, False
walking =False
while running:
    handle_events()

    main_update()
    player.update()

    clear_canvas()

    player.draw()

    update_canvas()
    delay(0.04)

close_canvas()

