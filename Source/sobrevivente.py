# Copyright (c) 2018 by Wesley Ferreira. All Rights Reserved.

from pygame import *
from pygame.locals import *
from spritesGame import *
from math import *

class Sobrevivente(object):

    def __init__(self, area, nome, imgPlayer = None):
        self.area = area
        self.grid = self.area.grid
        self.selecionado = False
        self.image = image.load(imgPlayer)
        self.nome = nome

    """
    Metodos de acao sobre o objeto
    """
    def setGridGeometry(self, gridx, gridy, gridtamcel):
        self.gridx = gridx
        self.gridy = gridy
        self.tamcel = gridtamcel
        self.x = self.gridx
        self.y = self.gridy
        self.w = self.tamcel
        self.h = self.tamcel

    def movement(self, i, j):
        self.x = self.gridx + i * self.tamcel
        self.y = self.gridy + j * self.tamcel

    def get_surface(self):
        return self.image

    def mostraRetangulo(self, screen, color):
        self.size = self.area.tamcells
        cell = Surface((self.size,self.size), SRCALPHA, 32)
        cell.fill(color)
        screen.blit(cell, (self.x,self.y))

    def show(self, screen, w = None, h = None):
        rect = self.image.get_rect()
        size = self.image.get_size()
        if(w):
            h = w * size[0] / size[1]
        else:
            w = h * size[0] / size[1]
        self.mostraRetangulo(screen, (255,255,255,128))
        if(self.selecionado):
            self.mostraRetangulo(screen, (0,0,255,128))
        self.mostraRetangulo(screen, (255,0,0,200-2*self.vida))
        self.surface = transform.scale(self.image, (h,w))
        screen.blit(self.surface, (self.x+(self.tamcel//2)-(self.w//3),self.y))
        self.rect = rect.move(self.x,self.y)

    def pos(self, x,y):
        if(self.positionGrid == (x,y)):
            return True
        else:
            return False

    def get_rect(self):
        return self.surface.get_rect().move(self.x, self.y)

    def collidepoint(self, pos):
        return Rect((self.x, self.y), (self.size,self.size)).collidepoint(pos)


    def meleeHit(self, i1, j1, i2, j2, dano, chain = ""):
        if(chain == "chain"):
            self.area.chainsaw_song.play()
        self.grid[i2][j2].vida -= dano
        self.grid[i1][j1].ataques -= 1
        self.grid[i1][j1].selecionado = False

    def move(self, i, j, pos):
        if( self.grid[i][j].selecionado ):
            self.grid[i][j].selecionado = False
            try:
                click = self.findclick(pos)
                dis = self.distance(i,j,click)
            except: pass
            try:
                if(dis == 1):
                        if( isinstance(self.grid[click[0]][click[1]], Rect) ): self.swap(i, j, click[0], click[1])
            except: pass

    def swap(self, i1, j1, i2 , j2):
        aux = self.grid[i2][j2]
        self.grid[i1][j1].movimentos -= 1
        self.grid[i2][j2] = self.grid[i1][j1]
        self.grid[i1][j1] = aux
        self.grid[i1][j1].x = self.area.geometry[0]+(i1*self.area.tamcells)
        self.grid[i1][j1].y = self.area.geometry[1]+(j1*self.area.tamcells)
        self.grid[i2][j2].movement(i2, j2)

    def findclick(self, pos):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                try:
                    if(self.grid[i][j].collidepoint(pos)): return (i,j)
                except: pass


    def distance(self, i1, j1, (i2 , j2)):
        ax, ay, dx, dy = i1, j1, i2, j2
        dis = 0
        while(True):
            if(ax == dx and ay == dy):
                break
            else:
                if(ax > dx and ay > dy):
                    ax-=1
                    ay-=1
                    dis+=1
                elif(ax > dx and ay < dy):
                    ax-=1
                    ay+=1
                    dis+=1
                elif(ax < dx and ay > dy):
                    ax+=1
                    ay-=1
                    dis+=1
                elif(ax > dx and ay < dy):
                    ax+=1
                    ay+=1
                    dis+=1
                elif(ax > dx):
                    ax-=1
                    dis+=1
                elif(ax<dx):
                    ax+=1
                    dis+=1
                elif(ay > dy):
                    ay -=1
                    dis+=1
                elif(ay< dy):
                    ay+=1
                    dis+=1
        return dis

    def knockback(self, i1,j1,(i2,j2), par):
        disx = i2 - i1
        disy = j2 - j1
        if(disx != 0):
            ni2 = i2 + int(par/disx)
        else:
            ni2 = i2
        if(disy != 0):
            nj2 = j2 + int(par/disy)
        else:
            nj2 = j2
        self.swap(i2,j2,ni2,nj2)
