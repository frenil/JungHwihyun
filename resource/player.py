from pico2d import *

class Ragna:
    def __init__(self):
        self.x,self.y = 900,450
        self.frame =0
        self.state =0
        self.st2co=0
        self.stcount =0
        self.see = 0
        self.walkframe= 0
        self.Lwalk = load_image('Lwalk.png')
        self.Rwalk = load_image('Rwalk.png')
        self.Lstand = load_image('stand1.png')
        self.Rstand = load_image('Rstand1.png')
        self.stand2 = load_image('stand2.png')
        self.Lpunch = load_image('punch.png')
        self.Rpunch = load_image('Rpunch.png')
        self.nomco1 = load_image('nomco1.png')
        self.Rnomco1 = load_image('Rnomco1.png')
        self.nomco2 = load_image('nomco2.png')
        self.Rnomco2 = load_image('Rnomco2.png')
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
        elif self.state == 3 :
            self.walkframe =(self.walkframe+1)%2
            if self.walkframe == 1:
                self.frame = (self.frame + 1)%9
            self.x += self.see*10
    def draw(self):
        if self.see == -1:
            if self.state == 0:
                if self.frame < 7:
                    self.Lstand.clip_draw_to_origin(self.frame * 350, 0, 350, 450, self.x, self.y, 175, 225)
                else:
                    self.Lstand.clip_draw_to_origin((13 - self.frame) * 350, 0, 350, 450, self.x, self.y, 175, 225)
            elif self.state == 1:
                self.stand2.clip_draw_to_origin(self.frame * 350, 0, 350, 350, self.x, self.y, 175, 225)
            elif self.state == 2:
                self.Lpunch.clip_draw_to_origin(self.frame * 480, 0, 480, 430, self.x - 90, self.y, 240, 215)
            elif self.state == 211:
                if self.frame > 8:
                    self.nomco1.clip_draw_to_origin((self.frame - 9) * 720, 0, 720, 430, self.x - 180, self.y, 360, 215)
                else:
                    self.nomco1.clip_draw_to_origin(self.frame * 720, 430, 720, 430, self.x - 180, self.y, 360, 215)
            elif self.state == 212:
                if self.frame > 8:
                    self.nomco2.clip_draw_to_origin((self.frame - 9) * 800, 0, 800, 430, self.x - 270, self.y, 400, 215)
                else:
                    self.nomco2.clip_draw_to_origin(self.frame * 800, 430, 800, 430, self.x - 270, self.y, 400, 215)
            elif self.state == 213:
                if self.frame < 7:
                    self.nomco3.clip_draw_to_origin(self.frame * 1100, 1000, 1100, 490, self.x - 300, self.y, 550, 250)
                elif self.frame < 14:
                    self.nomco3.clip_draw_to_origin((self.frame - 7) * 1100, 500, 1100, 490, self.x - 330, self.y, 550,
                                                    250)
                else:
                    self.nomco3.clip_draw_to_origin((self.frame - 14) * 1100, 0, 1100, 490, self.x - 330, self.y, 550,
                                                    250)
            elif self.state == 3:
                self.Lwalk.clip_draw_to_origin(self.frame * 300, 0, 300, 450, self.x, self.y, 150, 225)
        elif self.see ==1:
            if self.state == 0:
                if self.frame < 7:
                    self.Rstand.clip_draw_to_origin(self.frame * 350, 0, 350, 450, self.x, self.y, 175, 225)
                else:
                    self.Rstand.clip_draw_to_origin((13 - self.frame) * 350, 0, 350, 450, self.x, self.y, 175, 225)
            elif self.state == 1:
                self.stand2.clip_draw_to_origin(self.frame * 350, 0, 350, 350, self.x, self.y, 175, 225)
            elif self.state == 2:
                self.Rpunch.clip_draw_to_origin(self.frame * 480, 0, 480, 430, self.x -25, self.y, 240, 215)
            elif self.state == 211:
                if self.frame > 8:
                    self.Rnomco1.clip_draw_to_origin((self.frame - 9) * 720, 0, 720, 430, self.x-40 , self.y, 360, 215)
                else:
                    self.Rnomco1.clip_draw_to_origin(self.frame * 720, 430, 720, 430, self.x -40, self.y, 360, 215)
            elif self.state == 212:
                if self.frame > 8:
                    self.Rnomco2.clip_draw_to_origin((self.frame - 9) * 800, 0, 800, 430, self.x , self.y, 400, 215)
                else:
                    self.Rnomco2.clip_draw_to_origin(self.frame * 800, 430, 800, 430, self.x , self.y, 400, 215)
            elif self.state == 213:
                if self.frame < 7:
                    self.nomco3.clip_draw_to_origin(self.frame * 1100, 1000, 1100, 490, self.x - 300, self.y, 550, 250)
                elif self.frame < 14:
                    self.nomco3.clip_draw_to_origin((self.frame - 7) * 1100, 500, 1100, 490, self.x - 330, self.y, 550,
                                                    250)
                else:
                    self.nomco3.clip_draw_to_origin((self.frame - 14) * 1100, 0, 1100, 490, self.x - 330, self.y, 550,
                                                    250)
            elif self.state == 3:
                self.Rwalk.clip_draw_to_origin(self.frame * 300, 0, 300, 450, self.x, self.y, 150, 225)
































