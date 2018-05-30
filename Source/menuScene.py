#!/usr/bin/python2
# -*- coding: latin-1 -*-

from pygame import *
from pygame.locals import *
from spritesGame import *
from cenario import *

class menuScene(object):
    def __init__(self, screen):
        screen.blit(image.load("./Assets/Background.png") , (0,0))
        self.Logo = spriteButton(screen, "./Assets/Logo.png", (1280//2-350//2, 720//2-200//2), (350,200))

        self.background_sound = mixer.Sound("./Assets/Songs/Footsteps.wav")
        self.zombie = mixer.Sound("./Assets/Songs/Spawn.wav")
        self.background_sound.set_volume(0.5)
        self.background_sound.play(-1)

        font.init()
        self.myfont = font.SysFont('Sans Serif', 50)


    def loadMenu(self, screen, estado):
        textsurface = self.myfont.render( "Nao entre em panico!!", False, (0, 0, 0))
        screen.blit(textsurface,(460,150))
        textsurface = self.myfont.render( "Clique na logo a baixo para comecar", False, (0, 0, 0))
        screen.blit(textsurface,(340,200))
        for evento in event.get():
            if evento.type == QUIT:
                exit()
            if(evento.type == KEYDOWN):
                if(evento.key == K_ESCAPE):
                    exit()
            if evento.type == MOUSEBUTTONDOWN:
                if self.Logo.collide(evento.pos):
                    self.background_sound.stop()
                    self.zombie.play()
                    estado.atualState = "inGame"
                    estado.cenario = Cenario(screen, estado)
