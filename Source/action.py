# Copyright (c) 2018 by Wesley Ferreira. All Rights Reserved.

from sobrevivente import *
from zombie import *
from pygame import *

class action(object):
    def __init__(self, grid, geometry, tamcells):
        self.grid = grid
        self.geometry = geometry
        self.tamcells = tamcells

    def callbacks(self, estado):
        for evento in event.get():
            if evento.type == QUIT:
                exit()
            if evento.type == MOUSEBUTTONDOWN:
                if(estado.turno == "humanos"):
                    estado.area.click(evento)
                if(estado.turno == "zumbis"):
                    estado.area.click(evento)
                if(estado.endTurn.collide(evento.pos)):
                    estado.trocaTurno()
            if(evento.type == KEYDOWN):
                if(evento.key == K_ESCAPE):
                    exit()
            if(len(estado.sobreviventesList) == 0):
                estado.turno = "zumbis"
                estado.atualState = "inEnd"
            if(len(estado.zombiesList) == 0):
                estado.turno = "humanos"
                estado.atualState = "inEnd"

    def act(self,estado, evento):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if( estado.turno == "humanos" and isinstance( self.grid[i][j], Sobrevivente)):
                    if( self.grid[i][j].collidepoint(evento.pos)):
                        self.grid[i][j].selecionado = True
                    else:
                        self.grid[i][j].act(i, j, evento.pos)
                if( estado.turno == "zumbis" and isinstance( self.grid[i][j], zombie)):
                    try:
                        if( self.grid[i][j].collidepoint(evento.pos)):
                            self.grid[i][j].selecionado = True
                        else:
                            self.grid[i][j].act(i, j, evento)
                    except: pass
