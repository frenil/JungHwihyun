from pico2d import *

class Ragna:
    def __init__(self):
        self.x,self.y = 900,150
        self.Ldown,self.Rdown = False,False
        self.Ldouble, self.Rdouble = False, False
        self.frame =0
        self.state =0
        self.st2co=0
        self.stcount =0
        self.see = 1
        self.next =0
        self.walking = False
        self.walkframe= 0
        self.Lwalk = load_image('resource/Lwalk.png')
        self.Rwalk = load_image('resource/Rwalk.png')
        self.Lstand = load_image('resource/stand1.png')
        self.Rstand = load_image('resource/Rstand1.png')
        self.stand2 = load_image('resource/stand2.png')
        self.Lpunch = load_image('resource/punch.png')
        self.Rpunch = load_image('resource/Rpunch.png')
        self.nomco1 = load_image('resource/nomco1.png')
        self.Rnomco1 = load_image('resource/Rnomco1.png')
        self.nomco2 = load_image('resource/nomco2.png')
        self.Rnomco2 = load_image('resource/Rnomco2.png')
        self.nomco3 = load_image('resource/nomco3.png')
        self.Rnomco3 = load_image('resource/Rnomco3.png')
        self.dash = load_image('resource/dash1.png')
        self.Rdash = load_image('resource/Rdash1.png')
        self.dash2 = load_image('resource/dash2.png')
        self.Rdash2 = load_image('resource/Rdash2.png')

    def update(self):
        if (self.Rdown, self.Ldown) == (False,False):
            self.walking =False
        if self.state ==0 :
            self.frame = (self.frame+1)%13
            self.stcount+=1
            if self.Rdown == True and (self.state == 0 or self.state == 3):
                self.see = 1
            if self.Ldown == True and (self.state == 0 or self.state == 3):
                self.see = -1
            if self.Ldown == True or self.Rdown == True:
                self.walking = True
            if self.next == 0 and self.walking == True:
                self.state = 3
            elif self.next == 1:
                self.state = 2
                self.next = 0
                self.frame = 0
        elif self.state == 2:
            self.frame = self.frame+1
            if self.frame == 5:
                if self.next == 0:
                    self.state = 0
                elif self.next == 1:
                    self.state = 211
                self.next = 0
                self.frame = 0
        elif self.state == 211:
            self.frame = self.frame+1
            if self.frame == 16:
                if self.next == 0:
                    self.state = 0
                elif self.next == 1:
                    self.state = 212
                self.frame = 0
                self.next = 0
        elif self.state == 212:
            self.frame = (self.frame+1)%17
            if self.frame ==16:
                if self.next == 0:
                    self.state = 0
                elif self.next == 1:
                    self.state = 213
                self.frame = 0
                self.next=0
        elif self.state == 213:
            self.frame = (self.frame + 1) % 21
            if self.frame ==20:
                self.state = 0
                self.frame = 0
                self.next = 0
        elif self.state == 3 :
            self.walkframe =(self.walkframe+1)%2
            if self.walkframe == 1:
                self.frame = (self.frame + 1)%9
            self.x += self.see*10
            if self.walking == False:
                self.walkframe = 0
                self.state = 0
                self.frame = 0
            elif self.Rdouble == True or self.Ldouble == True:
                self.state = 4
                self.frame = 0
                self.next = 0
        elif self.state ==4:
            self.frame = (self.frame+1)%19
            if self.frame>4 and self.frame < 11:
                self.x += self.see*60
            if self.frame == 12 and self.next == 1:
                self.state = 41
                self.frame = 0
                self.next = 0
            elif self.frame == 17:
                self.state = 0
                self.frame = 0
                self.next = 0
                self.Rdouble = False
                self.Ldouble = False
        elif self.state == 41:
            self.frame = self.frame+1
            if self.frame == 16:
                self.state = 0
                self.frame = 0
                self.next = 0
    def draw(self):
        if self.see == -1:
            if self.state == 0:
                if self.frame < 7:
                    self.Lstand.clip_draw_to_origin(self.frame * 350, 0, 350, 450, self.x, self.y, 175, 225)
                else:
                    self.Lstand.clip_draw_to_origin((13 - self.frame) * 350, 0, 350, 450, self.x, self.y, 175, 225)
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
            elif self.state == 4:
                if self.frame < 9:
                    self.dash.clip_draw_to_origin(self.frame * 800, 500 ,800, 500, self.x-200,self.y , 400, 250)
                else :
                    self.dash.clip_draw_to_origin((self.frame-9) * 800, 0, 800, 500, self.x-200, self.y, 400, 250)
            elif self.state == 41:
                if self.frame<5:
                    self.dash2.clip_draw_to_origin(self.frame * 1000, 1040, 1000, 520, self.x-330, self.y-20, 500, 260)
                elif self.frame<11:
                    self.dash2.clip_draw_to_origin((self.frame-5) * 1000, 520, 1000, 520, self.x-330, self.y-20, 500, 260)
                else:
                    self.dash2.clip_draw_to_origin((self.frame-11) * 1000, 0, 1000, 520, self.x-330, self.y-20, 500, 260)


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
                    self.Rnomco3.clip_draw_to_origin(self.frame * 1100, 1000, 1100, 490, self.x -90, self.y, 550, 250)
                elif self.frame < 14:
                    self.Rnomco3.clip_draw_to_origin((self.frame - 7) * 1100, 500, 1100, 490, self.x -90, self.y, 550,
                                                    250)
                else:
                    self.Rnomco3.clip_draw_to_origin((self.frame - 14) * 1100, 0, 1100, 490, self.x -90, self.y, 550,
                                                        250)
            elif self.state == 3:
                self.Rwalk.clip_draw_to_origin(self.frame * 300, 0, 300, 450, self.x, self.y, 150, 225)
            elif self.state == 4:
                if self.frame < 9:
                    self.Rdash.clip_draw_to_origin(self.frame * 800, 500 ,800, 500, self.x-60,self.y , 400, 250)
                else :
                    self.Rdash.clip_draw_to_origin((self.frame-9) * 800, 0, 800, 500, self.x-60, self.y, 400, 250)
            elif self.state == 41:
                if self.frame<5:
                    self.Rdash2.clip_draw_to_origin(self.frame * 1000, 1040, 1000, 520, self.x-30, self.y-20, 500, 260)
                elif self.frame<11:
                    self.Rdash2.clip_draw_to_origin((self.frame-5) * 1000, 520, 1000, 520, self.x-30, self.y-20, 500, 260)
                else:
                    self.Rdash2.clip_draw_to_origin((self.frame-11) * 1000, 0, 1000, 520, self.x-30, self.y-20, 500, 260)
































