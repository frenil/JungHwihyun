from pico2d import *

rag = None
LoadCount =0

def Loading():
    global rag
    global dall
    global font
    rag = Ragna_image()
    dall = Dall_image()
    rag.Image_load()
class Dall_image:
    def __init__(self):
        self.Lstand = load_image('resource/dallstand.png')
        self.Rstand = load_image('resource/Rdallstand.png')
        self.Lhit = load_image('resource/dallhit.png')
        self.Rhit = load_image('resource/Rdallhit.png')
        self.Lpunch = load_image('resource/dallPunch.png')
        self.Rpunch = load_image('resource/RdallPunch.png')


class Ragna_image:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF',100)

    def Image_load(self):
        global LoadCount

        clear_canvas()
        image = load_image('title.png')
        image.draw_now(640, 360)
        self.Lwalk = load_image('resource/Lwalk.png')
        self.Rwalk = load_image('resource/Rwalk.png')
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1

        update_canvas()
        clear_canvas()
        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        self.Lstand = load_image('resource/stand1.png')
        self.Rstand = load_image('resource/Rstand1.png')
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1

        update_canvas()
        clear_canvas()
        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        self.stand2 = load_image('resource/stand2.png')
        self.Lpunch = load_image('resource/punch.png')
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()
        clear_canvas()
        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))

        self.Rpunch = load_image('resource/Rpunch.png')
        self.nomco1 = load_image('resource/nomco1.png')
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()
        clear_canvas()

        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        self.Rnomco1 = load_image('resource/Rnomco1.png')
        self.nomco2 = load_image('resource/nomco2.png')
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()
        clear_canvas()
        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))

        self.Rnomco2 = load_image('resource/Rnomco2.png')
        self.nomco3 = load_image('resource/nomco3.png')
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()
        clear_canvas()
        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))

        self.Rnomco3 = load_image('resource/Rnomco3.png')
        self.dash = load_image('resource/dash1.png')
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()
        clear_canvas()
        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))

        self.Rdash = load_image('resource/Rdash1.png')
        self.dash2 = load_image('resource/dash2.png')
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()
        clear_canvas()
        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))

        self.Rdash2 = load_image('resource/Rdash2.png')
        self.jump_up = load_image('resource/jump_up.png')
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))

        LoadCount +=1
        update_canvas()
        clear_canvas()
        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))

        self.Rjump_up = load_image('resource/Rjump_up.png')
        self.jump_down = load_image('resource/jump_down.png')
        LoadCount +=1
        update_canvas()
        clear_canvas()
        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))

        self.Rjump_down = load_image('resource/Rjump_down.png')
        self.upcom1 = load_image('resource/upcom1.png')
        LoadCount +=1
        update_canvas()
        clear_canvas()
        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))

        self.Rupcom1 = load_image('resource/Rupcom1.png')
        self.upcom2 = load_image('resource/upcom2.png')
        LoadCount +=1
        update_canvas()
        clear_canvas()
        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))

        self.Rupcom2 = load_image('resource/Rupcom2.png')
        self.upcom3 = load_image('resource/upcom3.png')
        LoadCount +=1
        update_canvas()
        clear_canvas()
        image.draw_now(640,360)
        self.font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))

        self.Rupcom3 = load_image('resource/Rupcom3.png')
        self.upcom4 = load_image('resource/upcom4.png')
        self.Rupcom4 = load_image('resource/Rupcom4.png')
        update_canvas()

        self.hit = load_image('resource/hit.png')
        self.Rhit = load_image('resource/Rhit.png')


