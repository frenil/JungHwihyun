from pico2d import *


class Ragna:
    def __init__(self):
        self.x,self.y = 900,50
        self.Ldown,self.Rdown = False,False
        self.Ldouble, self.Rdouble = False, False
        self.jumpdo = False
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
        self.jump_up = load_image('resource/jump_up.png')
        self.Rjump_up = load_image('resource/Rjump_up.png')
        self.jump_down = load_image('resource/jump_down.png')
        self.Rjump_down = load_image('resource/Rjump_down.png')
        self.upcom1 = load_image('resource/upcom1.png')
        self.Rupcom1 = load_image('resource/Rupcom1.png')
        self.upcom2 = load_image('resource/upcom2.png')
        self.Rupcom2 = load_image('resource/Rupcom2.png')
        self.upcom3 = load_image('resource/upcom3.png')
        self.Rupcom3 = load_image('resource/Rupcom3.png')
        self.upcom4 = load_image('resource/upcom4.png')
        self.Rupcom4 = load_image('resource/Rupcom4.png')

    def update(self):
        if self.x < 40:
            self.x = 40
        elif self.x > 1280 - 200:
             self.x = 1280 - 200
        if (self.Rdown, self.Ldown) == (False,False):
            self.walking =False
        if self.Rdown == True and (self.state == 0 or self.state == 3or self.state == 8):
            self.see = 1
        if self.Ldown == True and (self.state == 0 or self.state == 3or self.state == 8):
            self.see = -1
        if self.state ==0 :
            self.frame = (self.frame+1)%13
            self.stcount+=1

            if self.Ldown == True or self.Rdown == True:
                self.walking = True
            if self.next == 0 and self.walking == True:
                self.state = 3
            elif self.next == 1:
                self.state = 2
                self.next = 0
                self.frame = 0
            elif self.next == 8:
                self.state = 8
                self.next = 0
                self.frame =0
        elif self.state == 2:
            self.frame = self.frame+1
            if self.frame == 5:
                if self.next == 0:
                    self.state = 0
                elif self.next == 1:
                    self.state = 211
                elif self.next == 8:
                    self.state = 82
                self.next = 0
                self.frame = 0
        elif self.state == 211:
            self.frame = self.frame+1
            if self.frame == 16:
               if self.next == 1:
                    self.state = 212
               else:
                    self.state = 0

               self.frame = 0
               self.next = 0
        elif self.state == 212:
            self.frame = (self.frame+1)%17
            if self.frame ==16:
                if self.next == 1:
                    self.state = 213
                else:
                    self.state=0
                self.frame = 0
                self.next=0
        elif self.state == 213:
            self.frame = (self.frame + 1) % 21
            if self.frame ==20:
                self.state = 0
                self.frame = 0
                self.next = 0
        elif self.state == 3 :
            if self.next == 8:
                self.state = 8
                self.next = 0
                self.frame =0
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
        elif self.state == 8:
            self.frame = self.frame+1
            if self.next==1 and self.jumpdo==False:
                self.state=822
                self.frame=0
                self.next=0
            if self.frame<10:
                self.y += 30
            else:
                self.y-=30
            if self.y<=50:
                self.y=50
                self.state = 81
                self.frame=0
                self.next=0
                self.jumpdo=False
            if self.Ldown== True or self.Rdown == True:
                self.x += self.see*10
        elif self.state == 81:
            self.frame +=1
            if self.frame>4:
                self.state=0
                self.frame=0
        elif self.state == 82:
            self.frame = self.frame+1
            if self.frame>8:
                self.x +=self.see*10
                self.y += 26
            if self.frame>21:
                if self.next==0:
                    self.frame = 80
                    self.state =8
                elif  self.next==1:
                    self.frame =0
                    self.state = 822
                self.next=0
        elif self.state== 822:
            self.frame= self.frame+1
            self.jumpdo=True

            if self.frame>11:
                if self.next==0:
                    self.frame=90
                    self.state=8
                elif self.next==1:
                    self.frame=0
                    self.state=823
                self.next=0
        elif self.state ==823:
            self.frame = self.frame+1
            if self.frame>10:
                if self.next ==1:
                    self.frame = 0
                    self.state=824
                else:
                    self.frame=90
                    self.state=8
        elif self.state == 824:
            if self.frame<6 or self.frame>6:
                self.frame = self.frame+1
            else:
                self.x += self.see*15
                self.y -= 50
            if self.y<=50:
                self.frame+=1
                self.y=50
            if self.frame>10:
                self.state=0
                self.frame=0
                self.next=0
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
            elif self.state== 8:
                if self.frame>6:
                    self.jump_up.clip_draw_to_origin(2400,0,400,530, self.x-40,self.y, 200,265)
                else:
                    self.jump_up.clip_draw_to_origin(self.frame*400,0,400,530, self.x-40,self.y, 200,265)
            elif self.state == 81:
                self.jump_down.clip_draw_to_origin(self.frame*400,0, 400, 448, self.x-40,self.y, 200,224)
            elif self.state==82:
                if self.frame<11:
                    self.upcom1.clip_draw_to_origin(self.frame*660,550,660,550, self.x-150,self.y,330,275)
                else:
                    self.upcom1.clip_draw_to_origin((self.frame-11)*660,0,660,550, self.x-150,self.y,330,275)
            elif self.state == 822:
                self.upcom2.clip_draw_to_origin(self.frame*500,0,500,500,self.x-80,self.y,250,250)
            elif self.state == 823:
                self.upcom3.clip_draw_to_origin(self.frame*500,0,500,500,self.x-50,self.y,250,250)
            elif self.state == 824:
                self.upcom4.clip_draw_to_origin(self.frame*500,0,500,500,self.x-50,self.y,250,250)

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
            elif self.state== 8:
                if self.frame>6:
                    self.Rjump_up.clip_draw_to_origin(2400,0,400,530, self.x-40,self.y, 200,265)
                else:
                    self.Rjump_up.clip_draw_to_origin(self.frame*400,0,400,530, self.x-40,self.y, 200,265)
            elif self.state == 81:
                self.Rjump_down.clip_draw_to_origin(self.frame*400,0, 400, 448, self.x-40,self.y, 200,224)
            elif self.state==82:
                if self.frame<11:
                    self.Rupcom1.clip_draw_to_origin(self.frame*660,550,660,550, self.x,self.y,330,275)
                else:
                    self.Rupcom1.clip_draw_to_origin((self.frame-11)*660,0,660,550, self.x,self.y,330,275)
            elif self.state == 822:
                self.Rupcom2.clip_draw_to_origin(self.frame*500,0,500,500,self.x,self.y,250,250)
            elif self.state == 823:
                self.Rupcom3.clip_draw_to_origin(self.frame*500,0,500,500,self.x,self.y,250,250)
            elif self.state == 824:
                self.Rupcom4.clip_draw_to_origin(self.frame*500,0,500,500,self.x-50,self.y,250,250)

