from pico2d import *

rag = None

def Loading():
    global rag
    rag = Ragna_image()

class Ragna_image:
    def __init__(self):
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

