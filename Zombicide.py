# Copyright (c) 2018 by Wesley Ferreira. All Rights Reserved.

from pygame import *
from pygame.locals import *
from sys import exit
from Source.gameState import *

def main():

    init()
    mixer.init()

    clock = time.Clock()
    screen = display.set_mode((1280,720), FULLSCREEN)
    screen.set_alpha(255)
    estado = gameState(screen, "inMenu")
    display.set_caption("Zombicide")

    while True:

        if estado.atualState == "inMenu":
            estado.loadMenu()
        if estado.atualState == "inGame":
            estado.loadScene()
        if estado.atualState == "inEnd":
            estado.loadEnd()

        display.update()
        clock.tick(30)


main()
