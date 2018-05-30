# Copyright (c) 2018 by Wesley Ferreira. All Rights Reserved.

from pygame import *
from pygame.locals import *
from spritesGame import *
from sobrevivente import *
from zombie import *

class Phil(Sobrevivente):
    def __init__(self, area, nome, imgSobrevivente = None):
        super(Sobrevivente, self).__init__()
        self.area = area
        self.grid = self.area.grid
        self.selecionado = False
        self.image = image.load(imgSobrevivente)
        self.nome = nome
        self.setPar()
        self.resetMov()

    def setPar(self):
        self.vida = 100
        self.danoMelee = 30
        self.danoRanged = 100

    def resetMov(self):
        self.ataques = 1
        self.movimentos = 2

    def act(self, i, j, pos):
        if(self.grid[i][j].selecionado):

            if(self.grid[i][j].ataques > 0):

                try:
                    click = self.findclick(pos)
                    dis = self.distance(i,j,click)
                except: pass
                if(click):
                    if(dis == 1):
                        try:
                            if( isinstance(self.grid[click[0]][click[1]], zombie) ):
                                self.area.shotgun_song.play()
                                self.meleeHit(i, j, click[0], click[1], self.grid[i][j].danoRanged)
                        except: pass
                    elif(dis < 4):
                        try:
                            if( isinstance(self.grid[click[0]][click[1]], zombie) ):
                                self.area.shotgun_song.play()
                                self.meleeHit(i, j, click[0], click[1], self.grid[i][j].danoRanged/(dis**2))
                                self.knockback(i,j, click, 3)
                        except: pass

            if(self.grid[i][j].movimentos > 0):
                self.move(i,j, pos)
