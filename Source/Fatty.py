# Copyright (c) 2018 by Wesley Ferreira. All Rights Reserved.

from pygame import *
from pygame.locals import *
from spritesGame import *
from zombie import *
from sobrevivente import *

class Fatty(zombie):
    def __init__(self, area, img, tipo):
        super(zombie, self).__init__()
        self.area = area
        self.grid = self.area.grid
        self.selecionado = False
        self.image = img
        self.tipo = tipo
        self.setPar()
        self.resetMov()

    """
    Metodos para definicao de parametros
    """
    def setPar(self):
        self.vida = 100
        self.danoHit = 30
        self.danoExplode = 40

    def resetMov(self):
        self.ataques = 1
        self.movimentos = 2

    """
    Metrodos e acao do objeto
    """
    def morre(self, i ,j):
        if( isinstance(self.grid[i+1][j+1], Sobrevivente) ): self.meleeHit(i, j, i+1, j+1, self.grid[i][j].danoExplode)
        if( isinstance(self.grid[i+1][j-1], Sobrevivente) ): self.meleeHit(i, j, i+1, j-1, self.grid[i][j].danoExplode)
        if( isinstance(self.grid[i-1][j+1], Sobrevivente) ): self.meleeHit(i, j, i-1, j+1, self.grid[i][j].danoExplode)
        if( isinstance(self.grid[i-1][j-1], Sobrevivente) ): self.meleeHit(i, j, i-1, j-1, self.grid[i][j].danoExplode)
        if( isinstance(self.grid[i][j+1], Sobrevivente) ): self.meleeHit(i, j, i, j+1, self.grid[i][j].danoExplode)
        if( isinstance(self.grid[i][j-1], Sobrevivente) ): self.meleeHit(i, j, i, j-1, self.grid[i][j].danoExplode)
        if( isinstance(self.grid[i+1][j], Sobrevivente) ): self.meleeHit(i, j, i+1, j, self.grid[i][j].danoExplode)
        if( isinstance(self.grid[i-1][j], Sobrevivente) ): self.meleeHit(i, j, i-1, j, self.grid[i][j].danoExplode)

    def act(self,i, j, evento):
        pos = evento.pos
        if(evento.button == 1):
            if(self.grid[i][j].selecionado):
                if(self.grid[i][j].ataques > 0):
                    try:
                        click = self.findclick(pos)
                        dis = self.distance(i,j,click)
                    except: pass
                    if(click and dis == 1):
                        try:
                            if( isinstance(self.grid[click[0]][click[1]], Sobrevivente) ):
                                self.meleeHit(i, j, click[0], click[1], self.grid[i][j].dano)
                        except: pass

                if(self.grid[i][j].movimentos > 0):
                    self.move(i,j, pos)
