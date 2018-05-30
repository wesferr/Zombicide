# Copyright (c) 2018 by Wesley Ferreira. All Rights Reserved.

from pygame import *
from spritesGame import *
from sobrevivente import *
from zombie import *
from area import *
from action import *

class Area(object):
    def __init__(self, screen, estado, x, y, w, h, ncells):
        self.screen = screen
        self.estado = estado
        self.geometry = (x,y,w,h)
        self.ncells = ncells
        self.tamcells = (w/ncells)
        self.gencells()
        self.action = action(self.grid, self.geometry, self.tamcells)
        self.estado.action = self.action

    def gencells(self):
        self.grid = []
        for i in range(self.ncells):
            self.grid.append([])
            for j in range(self.ncells):
                rect = Rect(self.geometry[0]+(i*self.tamcells),self.geometry[1]+(j*self.tamcells),self.tamcells-1,self.tamcells-1)
                self.grid[i].append(rect)

    def mostraRetangulo(self, i, j):
            rect = self.grid[i][j]
            cell = Surface(rect.size, SRCALPHA, 32)
            cell.fill((255,255,255,32))
            self.screen.blit(cell, (rect.x,rect.y))

    def showcells(self):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if( isinstance(self.grid[i][j], Rect) ):
                    self.mostraRetangulo(i,j)
                elif( isinstance( self.grid[i][j], Sobrevivente) ):
                    if(self.grid[i][j].vida > 0):
                        self.grid[i][j].show(self.screen,w=self.tamcells)
                    else:
                        if(self.grid[i][j].nome == "Amy" or self.grid[i][j].nome == "Wanda"):
                            self.female_death_sound.play()
                        else:
                            self.male_death_sound.play()
                        self.estado.removeSobrevivente(self.grid[i][j])
                        rect = Rect(self.geometry[0]+(i*self.tamcells),self.geometry[1]+(j*self.tamcells),self.tamcells-1,self.tamcells-1)
                        self.grid[i][j] = rect
                elif( isinstance( self.grid[i][j], zombie) ):
                    if(self.grid[i][j].vida > 0):
                        self.grid[i][j].show(self.screen,w=self.tamcells)
                    else:
                        self.die_sound.play()
                        if(self.grid[i][j].tipo == "Fatty"): self.grid[i][j].morre(i,j)
                        self.estado.removeZombie(self.grid[i][j])
                        rect = Rect(self.geometry[0]+(i*self.tamcells),self.geometry[1]+(j*self.tamcells),self.tamcells-1,self.tamcells-1)
                        self.grid[i][j] = rect
    def addSobrevivente(self, sobrevivente, x, y):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if(x == i and y == j):
                    self.grid[i][j] = sobrevivente;
                    self.grid[i][j].setGridGeometry(self.geometry[0], self.geometry[1], self.tamcells)
                    self.grid[i][j].movement(i, j)
                    self.estado.addSobrevivente(sobrevivente)

    def addZombie(self, zombie, x, y):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if(x == i and y == j):
                    self.grid[i][j] = zombie;
                    self.grid[i][j].setGridGeometry(self.geometry[0], self.geometry[1], self.tamcells)
                    self.grid[i][j].movement(i, j)
                    self.estado.addZombie(zombie)

    def getSobrevivente(self, nome):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if( isinstance( self.grid[i][j], Sobrevivente) ):
                    if (self.grid[i][j].nome == nome):
                        return self.grid[i][j]

    def click(self, pos):
        self.action.act(self.estado,pos)
