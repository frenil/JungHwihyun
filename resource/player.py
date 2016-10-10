from pico2d import *

class Ragna:
    def __init__(self):
        self.x,self.y = 900,450
        self.frame =0
        self.state =0
        self.st2co=0
        self.stcount =0
        self.stand = load_image('stand1.png')
        self.stand2 = load_image('stand2.png')
        self.punch = load_image('punch.png')
        self.nomco1 = load_image('nomco1.png')
        self.nomco2 = load_image('nomco2.png')
        self.nomco3 = load_image('nomco3.png')
    def update(self):
        if self.state ==0 :
            self.frame = (self.frame+1)%13
            self.stcount+=1
            if self.stcount == 52:
                self.state = 1
                self.stcount =0
                self.frame =0
        elif self.state == 1:
            self.frame = (self.frame+1)%17
            self.st2co +=1
            if self.st2co>16:
                self.state = 0
                self.st2co = 0
        elif self.state == 2:
            self.frame = self.frame+1
        elif self.state == 211:
            self.frame = (self.frame+1)%17
        elif self.state == 212:
            self.frame = (self.frame+1)%17
        elif self.state == 213:
            self.frame = (self.frame + 1) % 21

    def draw(self):
        if self.state == 0:
            if self.frame <7:
                self.stand.clip_draw_to_origin(self.frame * 350, 0, 350, 450, self.x, self.y, 175, 225)
            else:
                self.stand.clip_draw_to_origin((13-self.frame) * 350, 0, 350, 450, self.x, self.y, 175, 225)
        elif self.state == 1:
            self.stand2.clip_draw_to_origin(self.frame * 350, 0, 350, 350, self.x, self.y, 175, 225)
        elif self.state ==2:
            self.punch.clip_draw_to_origin(self.frame * 480, 0, 480, 430, self.x-90, self.y, 240, 215)
        elif self.state == 211:
            if self.frame>8:
                self.nomco1.clip_draw_to_origin((self.frame-9 )* 720, 0, 720, 430, self.x-180, self.y, 360, 215)
            else:
                self.nomco1.clip_draw_to_origin(self.frame * 720, 430, 720, 430, self.x - 180, self.y, 360, 215)
        elif self.state == 212:
            if self.frame>8:
                self.nomco2.clip_draw_to_origin((self.frame-9) * 800, 0, 800, 430, self.x-270, self.y, 400, 215)
            else:
                self.nomco2.clip_draw_to_origin(self.frame * 800, 430, 800, 430, self.x-270, self.y, 400, 215)
        elif self.state == 213:
            if self.frame<7:
                self.nomco3.clip_draw_to_origin(self.frame*1100, 1000, 1100, 490, self.x-300, self.y,550,250)
            elif self.frame < 14:
                self.nomco3.clip_draw_to_origin((self.frame-7)*1100, 500, 1100, 490, self.x-330, self.y,550,250)
            else:
                self.nomco3.clip_draw_to_origin((self.frame-14)*1100, 0, 1100, 490, self.x-330, self.y,550,250)

def handle_events():
    global running
    global next
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_a :
                next = 1
open_canvas(1800,800)

player = Ragna()
state =0
running = True
stcount = 0
next = 0
frame=0
while running:
    handle_events()
    if player.state==0 and next ==1:
        player.state = 2
        player.frame=0
        player.stcount=0
        next=0
        frame=0
    elif player.state ==2 and frame==5:
        if next == 0:
            player.state = 0
        if next == 1 :
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
    player.update()
    frame +=1
    clear_canvas()

    player.draw()

    update_canvas()
    delay(0.05)

close_canvas()






























