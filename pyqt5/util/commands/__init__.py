from pygame import mixer
import time

def exiting(tela):
    mixer.init()
    mixer.Sound('sound/exit.mp3').play()
    time.sleep(0.5)
    tela.destroy()
