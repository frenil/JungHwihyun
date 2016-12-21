import game_framework
import json

def Speed(kmph):
    PIXEL_PER_METER = (100.0 / 0.8)  # 100픽셀 0.8m
    SPEED_KMPH = kmph
    SPEED_MPM = (SPEED_KMPH * 1000 / 60)
    SPEED_MPS = SPEED_MPM / 60
    SPEED_PPS = SPEED_MPS * PIXEL_PER_METER
    distance = SPEED_PPS * game_framework.frame_time
    return distance

class Stage:
    def __init__(self):
        self.dalls=[1,7,4,-1]
        self.hp = [1000,1000,2000,5000]
        self.x = [800,400,400,600]
        self.distance = [0,100,300,0]
        self.speed = [5,5,10,3]

    def Getdallcount(self,stage):
        return self.dalls[stage]
    def SetStage(self,number,stage,dall):
        dall.x = self.x[stage]+(number*self.distance[stage])
        dall.Wsp = Speed(self.speed[stage])
        dall.HP = self.hp[stage]

