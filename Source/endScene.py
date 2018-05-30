#!/usr/bin/python2
# -*- coding: latin-1 -*-

from pygame import *
from pygame.locals import *
from spritesGame import *
from cenario import *

class endScene(object):
    def __init__(self, screen):
        self.background = image.load("./Assets/Background.png")
        self.Logo = spriteButton(screen, "./Assets/Logo.png", (1280//2-350//2, 720//2-200//2), (350,200))

        font.init()
        self.myfont = font.SysFont('Sans Serif', 50)

    def loadEnd(self, screen, estado):
        screen.blit(self.background, (0,0))
        if(estado.turno == "humanos"):
            textsurface = self.myfont.render( "Uffa, essa foi dificil, os sobreviventes terao mais um dia", False, (0, 0, 0))
            screen.blit(textsurface,(120,300))
        if(estado.turno == "zumbis"):
            textsurface = self.myfont.render( "A chacina aconteceu, os zumbis agora tem mais integrantes", False, (0, 0, 0))
            screen.blit(textsurface,(130,300))
        textsurface = self.myfont.render( "Aperte ESC para sair", False, (0, 0, 0))
        screen.blit(textsurface,(450,600))
        for evento in event.get():
            if evento.type == QUIT:
                exit()
            if(evento.type == KEYDOWN):
                if(evento.key == K_ESCAPE):
                    exit()
