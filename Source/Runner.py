# Copyright (c) 2018 by Wesley Ferreira. All Rights Reserved.

from pygame import *
from pygame.locals import *
from spritesGame import *
from zombie import *
from sobrevivente import *

class Runner(zombie):
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
        self.dano = 20

    def resetMov(self):
        self.ataques = 2
        self.movimentos = 4

    """
    Metrodos e acao do objeto
    """
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
