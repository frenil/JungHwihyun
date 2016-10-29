from pico2d import *
import LoadRe
import Player
class dall:
    PUNCH =2
    def __init__(self):
        self.x,self.y = 800,50
        self.frame =0
        self.state =0
        self.see = -1
        self.Yhit = 20
        self.Xhit = 4
        self.ishit = False
        self.next =0
        self.tmp =0

    def get_Rect(self):

        if self.see == 1:
            draw_rectangle(self.x,self.y, self.x+175,self.y+200)
        elif self.see == -1:
            draw_rectangle(self.x,self.y, self.x+175,self.y+200)
    def get_bb(self):
        return (self.x,self.y, self.x+175,self.y+200)

    def update(self):
        if self.x < 40:
            self.x = 40
        elif self.x > 1280 - 200:
             self.x = 1280 - 200
        if self.state == 0:
            self.frame=(self.frame+1)%15
            if self.frame == 14:
                self.state= self.PUNCH
                self.frame=0
        if self.state == 1:
            if self.frame<9:
                self.frame+=1
            self.x += (self.see*-self.Xhit)
            self.y += self.Yhit
            self.Yhit -=3
            if self.y<=50:
                self.y=50
                self.state=0
                self.frame=0
                self.ishit =False
        if self.state == self.PUNCH:
            self.frame = self.frame+1
            if self.frame >16:
                self.state = 0
                self.frame = 0
    def draw(self):
        if self.see == -1:
            if self.state == 0 or self.state ==8:
                LoadRe.dall.Lstand.clip_draw_to_origin(self.frame * 350, 0, 350, 400, self.x, self.y, 175, 200)
            if self.state == 1:
                if self.frame<5:
                    LoadRe.dall.Lhit.clip_draw_to_origin(self.frame * 400, 0, 400, 410, self.x, self.y, 200, 205)
                else :
                    LoadRe.dall.Lhit.clip_draw_to_origin((9-self.frame) * 400, 0, 400, 410, self.x, self.y, 200, 205)
            if self.state == self.PUNCH:
                if self.frame<9:
                    LoadRe.dall.Lpunch.clip_draw_to_origin(self.frame * 640, 400, 640, 400, self.x, self.y, 320, 200)
                else:
                    LoadRe.dall.Lpunch.clip_draw_to_origin((self.frame-9) * 640, 0, 640, 400, self.x, self.y, 320, 200)

        elif self.see ==1:
            if self.state == 0 or self.state ==8:
                LoadRe.dall.Rstand.clip_draw_to_origin(self.frame * 350, 0, 350, 400, self.x, self.y, 175, 200)
            if self.state == 1:
                if self.frame<5:
                    LoadRe.dall.Rhit.clip_draw_to_origin(self.frame * 400, 0, 400, 410, self.x, self.y, 200, 205)
                else:
                    LoadRe.dall.Rhit.clip_draw_to_origin((9-self.frame) * 400, 0, 400, 410, self.x, self.y, 200, 205)
            if self.state == self.PUNCH:
                if self.frame<9:
                    LoadRe.dall.Rpunch.clip_draw_to_origin(self.frame * 640, 400, 640, 400, self.x, self.y, 320, 200)
                else:
                    LoadRe.dall.Rpunch.clip_draw_to_origin((self.frame-9) * 640, 0, 640, 400, self.x, self.y, 320, 200)
