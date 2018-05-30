#!/usr/bin/python2
# -*- coding: latin-1 -*-

from sobrevivente import *
from menuScene import *
from endScene import *

class gameState(object):
    def __init__(self, screen, atualState):
        self.screen = screen
        self.menu = menuScene(self.screen)
        self.end = endScene(self.screen)
        self.atualState = atualState
        self.sobreviventesList = []
        self.zombiesList = []
        self.turno = "zumbis"
        self.action = None

    def callbacks(self):
        self.action.callbacks(self)

    def trocaTurno(self):
        if(self.turno == "humanos"):
            self.turno = "zumbis"
            for i in range(len(self.sobreviventesList)):
                self.sobreviventesList[i].selecionado = False
            for i in range(len(self.zombiesList)):
                self.zombiesList[i].resetMov()

        elif(self.turno == "zumbis"):
            self.turno = "humanos"
            for i in range(len(self.zombiesList)):
                self.zombiesList[i].selecionado = False
            for i in range(len(self.sobreviventesList)):
                self.sobreviventesList[i].resetMov()

    def loadScene(self):
        self.cenario.loadScene(self.screen)

    def loadMenu(self):
        self.menu.loadMenu(self.screen, self)

    def loadEnd(self):
        self.end.loadEnd(self.screen, self)

    def addSobrevivente(self, sobrevivente):
        self.sobreviventesList.append(sobrevivente)

    def addZombie(self, zombie):
        self.zombiesList.append(zombie)

    def removeSobrevivente(self, sobrevivente):
        self.sobreviventesList.remove(sobrevivente)

    def removeZombie(self, zombie):
        self.zombiesList.remove(zombie)
