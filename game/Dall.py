from pico2d import *
import LoadRe
import Player
class dall:
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
    def draw(self):
        if self.see == -1:
            if self.state == 0 or self.state ==8:
                LoadRe.dall.Lstand.clip_draw_to_origin(self.frame * 350, 0, 350, 400, self.x, self.y, 175, 200)
            if self.state == 1:
                if self.frame<5:
                    LoadRe.dall.Lhit.clip_draw_to_origin(self.frame * 400, 0, 400, 410, self.x, self.y, 200, 205)
                else:
                    LoadRe.dall.Lhit.clip_draw_to_origin((9-self.frame) * 400, 0, 400, 410, self.x, self.y, 200, 205)

        elif self.see ==1:
            if self.state == 0 or self.state ==8:
                LoadRe.dall.Rstand.clip_draw_to_origin(self.frame * 350, 0, 350, 400, self.x, self.y, 175, 200)
            if self.state == 1:
                if self.frame<5:
                    LoadRe.dall.Rhit.clip_draw_to_origin(self.frame * 400, 0, 400, 410, self.x, self.y, 200, 205)
                else:
                    LoadRe.dall.Rhit.clip_draw_to_origin((9-self.frame) * 400, 0, 400, 410, self.x, self.y, 200, 205)
