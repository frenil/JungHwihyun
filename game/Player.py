from pico2d import *
import LoadRe

class Ragna:
    STAND, WALK, JUMP_UP, JUMP_DOWN = 0, 3, 8 , 81
    def __init__(self):
        self.x,self.y = 300,50
        self.Ldown,self.Rdown = False,False
        self.Ldouble, self.Rdouble = False, False
        self.jumpdo = False
        self.frame =0
        self.state =0
        self.st2co=0
        self.stcount =0
        self.Gjump=80
        self.see = 1
        self.next =0
        self.walking = False
        self.walkframe= 0

    def get_Rect(self):
        if self.see == 1:
            if self.state == 2 and self.frame == 2:
                draw_rectangle(self.x+100,self.y+50, self.x+210,self.y+200)
            elif self.state == 211 and self.frame == 9:
                draw_rectangle(self.x+150,self.y+50, self.x+300,self.y+200)
            elif self.state == 212 and self.frame == 7:
                draw_rectangle(self.x+200,self.y, self.x+400,self.y+200)
            elif self.state == 213 and self.frame>= 8and self.frame<=11:
                draw_rectangle(self.x+100,self.y, self.x+420,self.y+200)
            elif self.state == 4 and self.frame >= 6 and self.frame <= 7:
                draw_rectangle(self.x , self.y, self.x + 300, self.y + 200)
            elif self.state == 41 and self.frame >= 8 and self.frame <= 12:
                draw_rectangle(self.x + 100, self.y, self.x + 440, self.y + 230)
            elif self.state == 82 and self.frame >=6and self.frame<=14:
                draw_rectangle(self.x+130,self.y+50, self.x+260+(self.frame*5),self.y+50+(self.frame*15))
            elif self.state ==822 and self.frame == 7:
                draw_rectangle(self.x+130,self.y+50, self.x+250,self.y+250)
            elif self.state == 823 and self.frame == 6:
                draw_rectangle(self.x+70,self.y, self.x+250,self.y+200)
            elif self.state == 824 and self.frame == 6:
                draw_rectangle(self.x+70,self.y, self.x+250,self.y+200)


        elif self.see == -1:
            if self.state == 2 and self.frame == 2:
                draw_rectangle(self.x-80,self.y+50, self.x+30,self.y+200)
            elif self.state == 211 and self.frame == 9:
                draw_rectangle(self.x-150,self.y+50, self.x,self.y+200)
            elif self.state == 212 and self.frame == 7:
                draw_rectangle(self.x-270,self.y+50, self.x-70,self.y+200)
            elif self.state == 213 and self.frame >= 8 and self.frame <= 11:
                draw_rectangle(self.x - 290, self.y, self.x + 30, self.y + 200)
            elif self.state == 4 and self.frame >= 6 and self.frame <= 7:
                draw_rectangle(self.x -190, self.y, self.x + 110, self.y + 200)
            elif self.state == 41 and self.frame >= 8 and self.frame <= 12:
                draw_rectangle(self.x-310,self.y, self.x+30,self.y+230)
            elif self.state == 82 and self.frame >= 6 and self.frame <= 14:
                draw_rectangle(self.x-80-(self.frame*5),self.y+50, self.x+50,self.y+50+(self.frame*15))
            elif self.state ==822 and self.frame == 7:
                draw_rectangle(self.x-80,self.y+50, self.x+40,self.y+250)
            elif self.state == 823 and self.frame == 6:
                draw_rectangle(self.x-50,self.y+50, self.x+130,self.y+200)
            elif self.state == 824 and self.frame == 6:
                draw_rectangle(self.x-50,self.y, self.x+130,self.y+150)

    def get_bb(self):
        if self.see == 1:
            if self.state == 2 and self.frame == 2:
                return(self.x + 100, self.y + 100, self.x + 210, self.y + 200)
            elif self.state == 211 and self.frame == 9:
                return (self.x+150,self.y+50, self.x+290,self.y+200)
            elif self.state == 212 and self.frame == 7:
                return (self.x+200,self.y, self.x+400,self.y+200)
            elif self.state == 213 and self.frame>= 8 and self.frame<=11:
                return (self.x+100,self.y, self.x+420,self.y+200)
            elif self.state == 4 and self.frame >= 6 and self.frame <= 7:
                return (self.x , self.y, self.x + 300, self.y + 200)
            elif self.state == 41 and self.frame >= 8 and self.frame <= 12:
                return (self.x + 100, self.y, self.x + 440, self.y + 230)
            elif self.state == 82 and self.frame >=6and self.frame<=14:
                return(self.x+130,self.y+50, self.x+260+(self.frame*5),self.y+50+(self.frame*15))
            elif self.state ==822 and self.frame == 7:
                return(self.x+130,self.y+50, self.x+250,self.y+250)
            elif self.state == 823 and self.frame == 6:
                return(self.x+70,self.y, self.x+250,self.y+200)
            elif self.state == 824 and self.frame == 6:
                return(self.x+70,self.y, self.x+250,self.y+200)
        elif self.see == -1:
            if self.state == 2 and self.frame == 2:
                return(self.x - 80, self.y + 100, self.x + 30, self.y + 200)
            elif self.state == 211 and self.frame == 9:
                return (self.x - 140, self.y + 50, self.x, self.y + 200)
            elif self.state == 212 and self.frame == 7:
                return (self.x-270,self.y+50, self.x-70,self.y+200)
            elif self.state == 213 and self.frame >= 8 and self.frame <= 11:
                return (self.x-290,self.y, self.x+30,self.y+200)
            elif self.state == 4 and self.frame >= 6 and self.frame <= 7:
                return (self.x -190, self.y, self.x + 110, self.y + 200)
            elif self.state == 41 and self.frame >= 8 and self.frame <= 12:
                return (self.x-310,self.y, self.x+30,self.y+230)
            elif self.state == 82 and self.frame >= 6 and self.frame <= 14:
                return(self.x-80-(self.frame*5),self.y+50, self.x+50,self.y+50+(self.frame*15))
            elif self.state ==822 and self.frame == 7:
                return(self.x-80,self.y+50, self.x+40,self.y+250)
            elif self.state == 823 and self.frame == 6:
                return(self.x-270,self.y+50, self.x-70,self.y+200)
            elif self.state == 824 and self.frame == 6:
                return(self.x-50,self.y, self.x+130,self.y+150)
        return(0,0,0,0)
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
        if self.state == self.STAND :
            self.frame = (self.frame+1)%13
            self.stcount+=1

            if self.Ldown == True or self.Rdown == True:
                self.walking = True
            if self.next == 0 and self.walking == True:
                self.state = self.WALK
            elif self.next == 1:
                self.state = 2
                self.next = 0
                self.frame = 0
            elif self.next == 8:
                self.state = self.JUMP_UP
                self.next = 0
                self.frame =0
                self.Gjump=80
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
            self.frame = self.frame + 1
            if self.frame ==20:
                self.state = 0
                self.frame = 0
                self.next = 0
        elif self.state == self.WALK :
            if self.next == 8:
                self.state = self.JUMP_UP
                self.next = 0
                self.frame =0
                self.Gjump=80

            self.walkframe =(self.walkframe+1)%2
            if self.walkframe == 1:
                self.frame = (self.frame + 1)%9
            self.x += self.see*10
            if self.walking == False:
                self.walkframe = 0
                self.state = self.STAND
                self.frame = 0
            elif self.Rdouble == True or self.Ldouble == True:
                self.state = 4
                self.frame = 0
                self.next = 0
                self.Rdouble=False
                self.Ldouble = False
        elif self.state ==4:
            self.frame = (self.frame+1)%19
            if self.frame>4 and self.frame < 11:
                self.x += self.see*60
            if self.frame == 12 and self.next == 1:
                self.state = 41
                self.frame = 0
                self.next = 0
            elif self.frame == 17:
                self.state = self.STAND
                self.frame = 0
                self.next = 0
                self.Rdouble = False
                self.Ldouble = False
        elif self.state == 41:
            self.frame = self.frame+1
            if self.frame == 16:
                self.state = self.STAND
                self.frame = 0
                self.next = 0
        elif self.state == self.JUMP_UP:
            self.frame = self.frame+1
            self.Gjump -= 10
            if self.next==1 and self.jumpdo==False:
                self.state=822
                self.frame=0
                self.next=0
            if self.frame<10:
                self.y += self.Gjump
            else:
                self.y+=self.Gjump
            if self.y<=50:
                self.y=50
                self.state = self.JUMP_DOWN
                self.frame=0
                self.next=0
                self.jumpdo=False
            if self.Ldown== True or self.Rdown == True:
                self.x += self.see*10
        elif self.state == self.JUMP_DOWN:
            self.frame +=1
            if self.frame>4:
                self.state=self.STAND
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
                    self.Gjump=0
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
                    self.state=self.JUMP_UP
                    self.Gjump=0

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
                    self.state=self.JUMP_UP
                    self.Gjump=0

        elif self.state == 824:
            if self.frame<6 or self.frame>6:
                self.frame = self.frame+1
            else:
                self.x += self.see*15
                self.y -= 60
            if self.y<=50:
                self.frame+=1
                self.y=50
            if self.frame>10:
                self.state=self.STAND
                self.frame=0
                self.next=0
    def draw(self):
        if self.see == -1:
            if self.state == 0:
                if self.frame < 7:
                    LoadRe.rag.Lstand.clip_draw_to_origin(self.frame * 350, 0, 350, 450, self.x, self.y, 175, 225)
                else:
                    LoadRe.rag.Lstand.clip_draw_to_origin((13 - self.frame) * 350, 0, 350, 450, self.x, self.y, 175, 225)
            elif self.state == 2:
                LoadRe.rag.Lpunch.clip_draw_to_origin(self.frame * 480, 0, 480, 430, self.x - 90, self.y, 240, 215)
            elif self.state == 211:
                if self.frame > 8:
                    LoadRe.rag.nomco1.clip_draw_to_origin((self.frame - 9) * 720, 0, 720, 430, self.x - 180, self.y, 360, 215)
                else:
                    LoadRe.rag.nomco1.clip_draw_to_origin(self.frame * 720, 430, 720, 430, self.x - 180, self.y, 360, 215)
            elif self.state == 212:
                if self.frame > 8:
                    LoadRe.rag.nomco2.clip_draw_to_origin((self.frame - 9) * 800, 0, 800, 430, self.x - 270, self.y, 400, 215)
                else:
                    LoadRe.rag.nomco2.clip_draw_to_origin(self.frame * 800, 430, 800, 430, self.x - 270, self.y, 400, 215)
            elif self.state == 213:
                if self.frame < 7:
                    LoadRe.rag.nomco3.clip_draw_to_origin(self.frame * 1100, 1000, 1100, 490, self.x - 300, self.y, 550, 250)
                elif self.frame < 14:
                    LoadRe.rag.nomco3.clip_draw_to_origin((self.frame - 7) * 1100, 500, 1100, 490, self.x - 330, self.y, 550,
                                                    250)
                else:
                    LoadRe.rag.nomco3.clip_draw_to_origin((self.frame - 14) * 1100, 0, 1100, 490, self.x - 330, self.y, 550,
                                                    250)
            elif self.state == 3:
                LoadRe.rag.Lwalk.clip_draw_to_origin(self.frame * 300, 0, 300, 450, self.x, self.y, 150, 225)
            elif self.state == 4:
                if self.frame < 9:
                    LoadRe.rag.dash.clip_draw_to_origin(self.frame * 800, 500 ,800, 500, self.x-200,self.y , 400, 250)
                else :
                    LoadRe.rag.dash.clip_draw_to_origin((self.frame-9) * 800, 0, 800, 500, self.x-200, self.y, 400, 250)
            elif self.state == 41:
                if self.frame<5:
                    LoadRe.rag.dash2.clip_draw_to_origin(self.frame * 1000, 1040, 1000, 520, self.x-330, self.y-20, 500, 260)
                elif self.frame<11:
                    LoadRe.rag.dash2.clip_draw_to_origin((self.frame-5) * 1000, 520, 1000, 520, self.x-330, self.y-20, 500, 260)
                else:
                    LoadRe.rag.dash2.clip_draw_to_origin((self.frame-11) * 1000, 0, 1000, 520, self.x-330, self.y-20, 500, 260)
            elif self.state== 8:
                if self.frame>6:
                    LoadRe.rag.jump_up.clip_draw_to_origin(2400,0,400,530, self.x-40,self.y, 200,265)
                else:
                    LoadRe.rag.jump_up.clip_draw_to_origin(self.frame*400,0,400,530, self.x-40,self.y, 200,265)
            elif self.state == 81:
                LoadRe.rag.jump_down.clip_draw_to_origin(self.frame*400,0, 400, 448, self.x-40,self.y, 200,224)
            elif self.state==82:
                if self.frame<11:
                    LoadRe.rag.upcom1.clip_draw_to_origin(self.frame*660,550,660,550, self.x-150,self.y,330,275)
                else:
                    LoadRe.rag.upcom1.clip_draw_to_origin((self.frame-11)*660,0,660,550, self.x-150,self.y,330,275)
            elif self.state == 822:
                LoadRe.rag.upcom2.clip_draw_to_origin(self.frame*500,0,500,500,self.x-80,self.y,250,250)
            elif self.state == 823:
                LoadRe.rag.upcom3.clip_draw_to_origin(self.frame*500,0,500,500,self.x-50,self.y,250,250)
            elif self.state == 824:
                LoadRe.rag.upcom4.clip_draw_to_origin(self.frame*500,0,500,500,self.x-50,self.y,250,250)

        elif self.see ==1:
            if self.state == 0:
                if self.frame < 7:
                    LoadRe.rag.Rstand.clip_draw_to_origin(self.frame * 350, 0, 350, 450, self.x, self.y, 175, 225)
                else:
                    LoadRe.rag.Rstand.clip_draw_to_origin((13 - self.frame) * 350, 0, 350, 450, self.x, self.y, 175, 225)
            elif self.state == 1:
                LoadRe.rag.stand2.clip_draw_to_origin(self.frame * 350, 0, 350, 350, self.x, self.y, 175, 225)
            elif self.state == 2:
                LoadRe.rag.Rpunch.clip_draw_to_origin(self.frame * 480, 0, 480, 430, self.x -25, self.y, 240, 215)
            elif self.state == 211:
                if self.frame > 8:
                    LoadRe.rag.Rnomco1.clip_draw_to_origin((self.frame - 9) * 720, 0, 720, 430, self.x-40 , self.y, 360, 215)
                else:
                    LoadRe.rag.Rnomco1.clip_draw_to_origin(self.frame * 720, 430, 720, 430, self.x -40, self.y, 360, 215)
            elif self.state == 212:
                if self.frame > 8:
                    LoadRe.rag.Rnomco2.clip_draw_to_origin((self.frame - 9) * 800, 0, 800, 430, self.x , self.y, 400, 215)
                else:
                    LoadRe.rag.Rnomco2.clip_draw_to_origin(self.frame * 800, 430, 800, 430, self.x , self.y, 400, 215)
            elif self.state == 213:
                if self.frame < 7:
                    LoadRe.rag.Rnomco3.clip_draw_to_origin(self.frame * 1100, 1000, 1100, 490, self.x -90, self.y, 550, 250)
                elif self.frame < 14:
                    LoadRe.rag.Rnomco3.clip_draw_to_origin((self.frame - 7) * 1100, 500, 1100, 490, self.x -90, self.y, 550,
                                                    250)
                else:
                    LoadRe.rag.Rnomco3.clip_draw_to_origin((self.frame - 14) * 1100, 0, 1100, 490, self.x -90, self.y, 550,
                                                        250)
            elif self.state == 3:
                LoadRe.rag.Rwalk.clip_draw_to_origin(self.frame * 300, 0, 300, 450, self.x, self.y, 150, 225)
            elif self.state == 4:
                if self.frame < 9:
                    LoadRe.rag.Rdash.clip_draw_to_origin(self.frame * 800, 500 ,800, 500, self.x-60,self.y , 400, 250)
                else :
                    LoadRe.rag.Rdash.clip_draw_to_origin((self.frame-9) * 800, 0, 800, 500, self.x-60, self.y, 400, 250)
            elif self.state == 41:
                if self.frame<5:
                    LoadRe.rag.Rdash2.clip_draw_to_origin(self.frame * 1000, 1040, 1000, 520, self.x-30, self.y-20, 500, 260)
                elif self.frame<11:
                    LoadRe.rag.Rdash2.clip_draw_to_origin((self.frame-5) * 1000, 520, 1000, 520, self.x-30, self.y-20, 500, 260)
                else:
                    LoadRe.rag.Rdash2.clip_draw_to_origin((self.frame-11) * 1000, 0, 1000, 520, self.x-30, self.y-20, 500, 260)
            elif self.state== 8:
                if self.frame>6:
                    LoadRe.rag.Rjump_up.clip_draw_to_origin(2400,0,400,530, self.x-40,self.y, 200,265)
                else:
                    LoadRe.rag.Rjump_up.clip_draw_to_origin(self.frame*400,0,400,530, self.x-40,self.y, 200,265)
            elif self.state == 81:
                LoadRe.rag.Rjump_down.clip_draw_to_origin(self.frame*400,0, 400, 448, self.x-40,self.y, 200,224)
            elif self.state==82:
                if self.frame<11:
                    LoadRe.rag.Rupcom1.clip_draw_to_origin(self.frame*660,550,660,550, self.x,self.y,330,275)
                else:
                    LoadRe.rag.Rupcom1.clip_draw_to_origin((self.frame-11)*660,0,660,550, self.x,self.y,330,275)
            elif self.state == 822:
                LoadRe.rag.Rupcom2.clip_draw_to_origin(self.frame*500,0,500,500,self.x,self.y,250,250)
            elif self.state == 823:
                LoadRe.rag.Rupcom3.clip_draw_to_origin(self.frame*500,0,500,500,self.x,self.y,250,250)
            elif self.state == 824:
                LoadRe.rag.Rupcom4.clip_draw_to_origin(self.frame*500,0,500,500,self.x-50,self.y,250,250)

