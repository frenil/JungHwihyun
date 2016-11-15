def Speed(kmph):
    PIXEL_PER_METER = (100.0 / 0.8)  # 100픽셀 0.8m
    SPEED_KMPH = kmph
    SPEED_MPM = (SPEED_KMPH * 1000 / 60)
    SPEED_MPS = SPEED_MPM / 60
    SPEED_PPS = SPEED_MPS * PIXEL_PER_METER
    distance = SPEED_PPS * game_framework.frame_time
    return distance

class stage:
    def __init__(self):
        self.Dallnumber = 0
        self.dallx = [0,0,0,0,0,0,0,0,0,0]
        self.dall_HP = 1000
        self.speed = [0,0,0,0,0,0,0,0,0,0]
        self.Playerx = 300
    def update(self,number):
        if number==0:
            self.Dallnumber = 1
            self.Playerx = 30
            self.dall_HP = 1000
            for i in range(self.Dallnumber):
                self.dallx[i] = 700
                self.speed[i] =  4
        elif number== 1:
            self.Dallnumber=10
            self.Playerx = 300
            self.dall_HP = 1000
            for i in range(self.Dallnumber):
                self.dallx[i]= -300+(250*i)
                self.speed[i] = (i%4)+1
        elif number ==2:
            self.Dallnumber = 5
            self.Playerx = 60
            self.dall_HP = 3000
            for i in range(self.Dallnumber):
                self.dallx[i] = 400+(100 * i)
                self.speed[i] = (i+1 % 5) + 4