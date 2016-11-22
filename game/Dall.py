from pico2d import *
import LoadRe
import Player
import game_framework


def Speed(kmph):
    PIXEL_PER_METER = (100.0 / 0.8)  # 100픽셀 0.8m
    SPEED_KMPH = kmph
    SPEED_MPM = (SPEED_KMPH * 1000 / 60)
    SPEED_MPS = SPEED_MPM / 60
    SPEED_PPS = SPEED_MPS * PIXEL_PER_METER
    distance = SPEED_PPS * game_framework.frame_time
    return distance

class dall:
    PUNCH =2
    Wkmph, Xhkmph,Yhkmph = 4,5, 29

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAME_PER_ACTION = 12

    def __init__(self):
        self.x,self.y = 800,50
        self.frame =0
        self.total_frames =0
        self.state =0
        self.see = -1
        self.hitxSp =4
        self.hitySp =4
        self.Yhit = 20
        self.Xhit = 4
        self.ishit = False
        self.next =0
        self.tmp =0
        self.isP = False
        self.Wsp = Speed(self.Wkmph)
        self.Ysp = Speed(self.Yhkmph)
        self.HP = 1000

        self.font = load_font('ENCR10B.TTF',20)

    def get_Rect(self):
        if self.see == 1:
            if self.state == self.PUNCH and self.frame == 8:
                draw_rectangle(self.x + (self.see * 70), self.y, self.x + 250, self.y + 200)

            draw_rectangle(self.x,self.y, self.x+175,self.y+200)
        elif self.see == -1:
            if self.state==self.PUNCH and self.frame==8:
                draw_rectangle(self.x+(self.see*70), self.y, self.x + 100, self.y + 200)
            draw_rectangle(self.x,self.y, self.x+175,self.y+200)
    def A_get_bb(self):
        if self.state==self.PUNCH and self.frame==8:
            if self.see ==1:
                return (self.x+(self.see*70), self.y, self.x + 250, self.y + 200)
            if self.see == -1:
                return (self.x+(self.see*70), self.y, self.x + 100, self.y + 200)

        return (0,0,0,0)


    def H_get_bb(self):
        return (self.x,self.y, self.x+175,self.y+200)

    def update(self):
        self.total_frames += self.FRAME_PER_ACTION * self.ACTION_PER_TIME * game_framework.frame_time



        if self.state == 0:
            self.frame = int(self.total_frames)%15

            self.x += self.see*self.Wsp
            if self.frame == 14 and self.isP==True:
                self.state= self.PUNCH
                self.total_frames=0

        if self.state == 1:
            if self.frame<8:
                self.frame = int(self.total_frames)
            else:
                self.frame = 8
            self.x += -0.5*(self.see*Speed(self.hitxSp))
            self.y += (self.hitySp) -Speed(int(self.total_frames)*3)
            if self.y<=50:
                self.y=50
                self.state=0
                self.total_frames=0
                self.ishit =False
        if self.state == self.PUNCH:
            self.frame = int(self.total_frames)

            if self.frame >16:
                self.state = 0
                self.total_frames = 0
    def draw(self):
        self.font.draw(self.x-10,self.y+250,'HP: %d'%self.HP,(255,255,255))

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
                    LoadRe.dall.Lpunch.clip_draw_to_origin(self.frame * 640, 400, 640, 400, self.x-70, self.y, 320, 200)
                else:
                    LoadRe.dall.Lpunch.clip_draw_to_origin((self.frame-9) * 640, 0, 640, 400, self.x-70, self.y, 320, 200)

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
                    LoadRe.dall.Rpunch.clip_draw_to_origin(self.frame * 640, 400, 640, 400, self.x-70, self.y, 320, 200)
                else:
                    LoadRe.dall.Rpunch.clip_draw_to_origin((self.frame-9) * 640, 0, 640, 400, self.x-70, self.y, 320, 200)
