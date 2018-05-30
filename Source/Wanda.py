# Copyright (c) 2018 by Wesley Ferreira. All Rights Reserved.

from pygame import *
from pygame.locals import *
from spritesGame import *
from sobrevivente import *
from zombie import *

class Wanda(Sobrevivente):
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
        self.danoMelee = 20
        self.danoRanged = 30

    def resetMov(self):
        self.ataques = 1
        self.movimentos = 4

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
                            if( isinstance(self.grid[i+1][j+1], zombie) ): self.meleeHit(i, j, i+1, j+1, self.grid[i][j].danoMelee, "chain")
                            if( isinstance(self.grid[i+1][j-1], zombie) ): self.meleeHit(i, j, i+1, j-1, self.grid[i][j].danoMelee, "chain")
                            if( isinstance(self.grid[i-1][j+1], zombie) ): self.meleeHit(i, j, i-1, j+1, self.grid[i][j].danoMelee, "chain")
                            if( isinstance(self.grid[i-1][j-1], zombie) ): self.meleeHit(i, j, i-1, j-1, self.grid[i][j].danoMelee, "chain")
                            if( isinstance(self.grid[i][j+1], zombie) ): self.meleeHit(i, j, i, j+1, self.grid[i][j].danoMelee, "chain")
                            if( isinstance(self.grid[i+1][j], zombie) ): self.meleeHit(i, j, i+1, j, self.grid[i][j].danoMelee, "chain")
                            if( isinstance(self.grid[i][j-1], zombie) ): self.meleeHit(i, j, i, j-1, self.grid[i][j].danoMelee, "chain")
                            if( isinstance(self.grid[i-1][j], zombie) ): self.meleeHit(i, j, i-1, j, self.grid[i][j].danoMelee, "chain")
                        except: pass
                    elif(dis < 4):
                        #try:
                            if( isinstance(self.grid[click[0]][click[1]], zombie) ):
                                self.meleeHit(i, j, click[0], click[1], self.grid[i][j].danoRanged/dis)
                                self.area.pistol_song.play()
                        #except: pass

            if(self.grid[i][j].movimentos > 0):
                self.move(i,j, pos)
