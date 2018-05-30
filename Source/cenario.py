# Copyright (c) 2018 by Wesley Ferreira. All Rights Reserved.

from pygame import *
from spritesGame import *
from area import *
from sobrevivente import *
from zombie import *
from Amy import *
from Phil import *
from Ned import *
from Wanda import *
from Walker import *
from Runner import *
from Fatty import *
from Abomination import *


class Cenario(object):
    def __init__(self, screen, estado):
        self.cenario(screen, estado)

    def displaySprites(self, screen):

        try:
            vida = self.area.getSobrevivente("Amy").vida
            if(vida > 0):
                self.Amy.show(screen)
                textsurface = self.myfont.render( 'Vida: {}'.format(vida) , False, (0, 0, 0))
                screen.blit(textsurface,(840,300))
        except: pass

        try:
            vida = self.area.getSobrevivente("Ned").vida
            if(vida > 0):
                self.Ned.show(screen)
                textsurface = self.myfont.render( 'Vida: {}'.format(vida) , False, (0, 0, 0))
                screen.blit(textsurface,(1040,300))
        except: pass

        try:
            vida = self.area.getSobrevivente("Phil").vida
            if(vida > 0):
                self.Phil.show(screen)
                textsurface = self.myfont.render( 'Vida: {}'.format(vida) , False, (0, 0, 0))
                screen.blit(textsurface,(840,550))
        except: pass

        try:
            vida = self.area.getSobrevivente("Wanda").vida
            if(vida > 0):
                self.Wanda.show(screen)
                textsurface = self.myfont.render( 'Vida: {}'.format(vida) , False, (0, 0, 0))
                screen.blit(textsurface,(1040,550))
        except: pass


    def loadScene(self, screen):
        screen.blit(self.background, (0,0))
        draw.rect(screen, (0,0,0),(5, 5, 710, 710))
        screen.blit(self.tabuleiro, (10,10))
        self.estado.endTurn.show(screen)
        if(self.estado.turno == "zumbis"):
            self.vezzumbi.show(screen)
        if(self.estado.turno == "humanos"):
            self.vezsobreviventes.show(screen)
        self.displaySprites(screen)
        self.area.showcells()
        self.estado.callbacks()


    def cenario(self, screen, estado):

        ncells = 15
        center = (ncells-1)//2

        font.init()
        self.myfont = font.SysFont('Sans Serif', 30)

        self.background = image.load("./Assets/Background.png")

        tabuleiro = image.load("./Assets/Y-zone.png")
        self.tabuleiro = transform.scale(tabuleiro, (700,700))

        estado.endTurn = spriteButton(screen, "./Assets/FinalizarTurno.png", (850,600), (300, 120))
        self.vezzumbi = spriteButton(screen, "./Assets/VezZumbis.png", (850,0), (300, 120))
        self.vezsobreviventes = spriteButton(screen, "./Assets/VezSobreviventes.png", (850,0), (300, 120))

        self.area = Area(screen, estado, 16, 16, 700,700, ncells)


        self.area.background_sound = mixer.Sound("./Assets/Songs/Horde.wav")
        self.area.spawn_sound = mixer.Sound("./Assets/Songs/Spawn.wav")
        self.area.die_sound = mixer.Sound("./Assets/Songs/Die.wav")
        self.area.male_death_sound = mixer.Sound("./Assets/Songs/Male_Death.wav")
        self.area.female_death_sound = mixer.Sound("./Assets/Songs/Female_Death.wav")
        self.area.pistol_song = mixer.Sound("./Assets/Songs/Pistol.wav")
        self.area.rifle_song = mixer.Sound("./Assets/Songs/Rifle.wav")
        self.area.shotgun_song = mixer.Sound("./Assets/Songs/Shotgun.wav")
        self.area.chainsaw_song = mixer.Sound("./Assets/Songs/Chainsaw.wav")
        self.area.katana_song = mixer.Sound("./Assets/Songs/Katana.wav")

        self.area.background_sound.set_volume(0.07)
        self.area.background_sound.play(-1)


        self.Amy   = spriteSobrevivente(screen, (830,100), "./Assets/Personagens/Amy.png", (110, 200))
        self.Ned   = spriteSobrevivente(screen, (1030,100), "./Assets/Personagens/Ned.png", (110, 200))
        self.Phil  = spriteSobrevivente(screen, (830,350), "./Assets/Personagens/Phil.png", (110, 200))
        self.Wanda = spriteSobrevivente(screen, (1030,350), "./Assets/Personagens/Wanda.png", (110, 200))

        self.Walker = image.load("./Assets/Zumbis/Walker.png")
        self.Runner = image.load("./Assets/Zumbis/Runner.png")
        self.Fatty  = image.load("./Assets/Zumbis/Fatty.png")
        self.Abomination  = image.load("./Assets/Zumbis/Abomination.png")

        self.area.addSobrevivente( Amy(self.area, "Amy", "./Assets/Personagens/Amy.png"), center, center)
        self.area.addSobrevivente( Ned(self.area, "Ned", "./Assets/Personagens/Ned.png"), center, center+1)
        self.area.addSobrevivente( Phil(self.area, "Phil", "./Assets/Personagens/Phil.png"), center+1, center)
        self.area.addSobrevivente( Wanda(self.area, "Wanda", "./Assets/Personagens/Wanda.png"), center+1, center+1)

        self.area.addZombie( Abomination(self.area, self.Abomination, "Abomination"), 0, ncells-1)
        self.area.addZombie( Runner(self.area, self.Runner, "Runner"), 1, ncells-1)
        self.area.addZombie( Fatty(self.area, self.Fatty, "Fatty"), 0, ncells-2)

        self.area.addZombie( Abomination(self.area, self.Abomination, "Abomination"), ncells-1, 0)
        self.area.addZombie( Runner(self.area, self.Runner, "Runner"), ncells-1, 1)
        self.area.addZombie( Fatty(self.area, self.Fatty, "Fatty"), ncells-2, 0)

        self.estado = estado
        self.estado.area = self.area
