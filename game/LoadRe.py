from pico2d import *

rag = None
back = None
dall = None
LoadCount =0

def Loading():
    global rag
    global dall, back
    global font, sound
    font = load_font('ENCR10B.TTF', 100)
    image = load_image('resource/warp_small.png')
    sound = Sound()
    rag = Ragna_image()
    dall = Dall_image()
    back = Back_image()
    sound.sound_load()
    back.Image_load()
    dall.Image_load(image,font)
    rag.Image_load(image,font)
class Sound:
    def __init__(self):
        pass
    def sound_load(self):
        self.title_bgm = load_music('sound/title_music.mp3')
        self.title_bgm.set_volume(64)
        self.play_bgm = load_music('sound/play_music.mp3')
        self.play_bgm.set_volume(64)
        self.hit_sound = load_wav('sound/hit_effect.wav')
        self.hit_sound.set_volume(64)
class Back_image:
    def __init__(self):
        pass
    def Image_load(self):
        self.back_1 = load_image('back.png')
        self.back_2 = load_image('resource/back_2.png')
        self.help_back = load_image('resource/help.png')
        self.Game_over = load_image('resource/gameover.png')
        self.rank = load_image('resource/rank_back.png')
        self.tier = load_image('resource/Tier.png')
class Dall_image:
    def __init__(self):
        pass
    def Image_load(self,image,font):
        global LoadCount
        clear_canvas()
        self.Lstand = load_image('resource/dallstand.png')
        self.Rstand = load_image('resource/Rdallstand.png')
        self.spin = load_image('resource/spin.png')
        self.Rspin = load_image('resource/Rspin.png')
        LoadCount +=1
        image.draw_now(640, 360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        update_canvas()

        clear_canvas()
        self.Lhit = load_image('resource/dallhit.png')
        self.Rhit = load_image('resource/Rdallhit.png')
        LoadCount +=1
        image.draw_now(640, 360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        update_canvas()

        clear_canvas()
        self.Lpunch = load_image('resource/dallPunch.png')
        self.Rpunch = load_image('resource/RdallPunch.png')


        LoadCount += 1
        image.draw_now(640, 360)
        font.draw(300, 100, "Loading  %d" % LoadCount, (225, 225, 225))
        update_canvas()


class Ragna_image:
    def __init__(self):
        pass
    def Image_load(self,image,font):
        global LoadCount

        clear_canvas()
        self.Lwalk = load_image('resource/Lwalk.png')
        self.Rwalk = load_image('resource/Rwalk.png')
        image.draw_now(640, 360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()

        clear_canvas()
        self.Lstand = load_image('resource/stand1.png')
        self.Rstand = load_image('resource/Rstand1.png')
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()

        clear_canvas()
        self.stand2 = load_image('resource/stand2.png')
        self.Lpunch = load_image('resource/punch.png')
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()

        clear_canvas()
        self.Rpunch = load_image('resource/Rpunch.png')
        self.nomco1 = load_image('resource/nomco1.png')
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()

        clear_canvas()
        self.Rnomco1 = load_image('resource/Rnomco1.png')
        self.nomco2 = load_image('resource/nomco2.png')
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()

        clear_canvas()
        self.Rnomco2 = load_image('resource/Rnomco2.png')
        self.nomco3 = load_image('resource/nomco3.png')
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()

        clear_canvas()
        self.Rnomco3 = load_image('resource/Rnomco3.png')
        self.dash = load_image('resource/dash1.png')
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()

        clear_canvas()
        self.Rdash = load_image('resource/Rdash1.png')
        self.dash2 = load_image('resource/dash2.png')
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()

        clear_canvas()
        self.Rdash2 = load_image('resource/Rdash2.png')
        self.jump_up = load_image('resource/jump_up.png')
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        LoadCount +=1
        update_canvas()

        clear_canvas()
        self.Rjump_up = load_image('resource/Rjump_up.png')
        self.jump_down = load_image('resource/jump_down.png')
        LoadCount +=1
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        update_canvas()

        clear_canvas()
        self.Rjump_down = load_image('resource/Rjump_down.png')
        self.upcom1 = load_image('resource/upcom1.png')
        LoadCount +=1
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        update_canvas()

        clear_canvas()
        self.Rupcom1 = load_image('resource/Rupcom1.png')
        self.upcom2 = load_image('resource/upcom2.png')
        LoadCount +=1
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        update_canvas()

        clear_canvas()
        self.Rupcom2 = load_image('resource/Rupcom2.png')
        self.upcom3 = load_image('resource/upcom3.png')
        LoadCount +=1
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        update_canvas()

        clear_canvas()
        self.Rupcom3 = load_image('resource/Rupcom3.png')
        self.upcom4 = load_image('resource/upcom4.png')
        self.Rupcom4 = load_image('resource/Rupcom4.png')
        LoadCount +=1
        image.draw_now(640,360)
        font.draw(300,100,"Loading  %d"%LoadCount,(225,225,225))
        update_canvas()

        self.hit = load_image('resource/hit.png')
        self.Rhit = load_image('resource/Rhit.png')


