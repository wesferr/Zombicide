# Copyright (c) 2018 by Wesley Ferreira. All Rights Reserved.

from pygame import *
from pygame.locals import *

class spriteButton(sprite.Sprite):

    def __init__(self, screen, link, (x,y), (wid, hei)):
        sprite.Sprite.__init__(self)
        self.imgButton = image.load(link).convert_alpha()
        self.posButton = (x,y)
        self.imgButton = transform.scale(self.imgButton, (wid, hei))
        screen.blit(self.imgButton, self.posButton)

    def show(self, screen):
        screen.blit(self.imgButton, self.posButton)

    def collide(self, pos):
        return self.imgButton.get_rect(topleft=(self.posButton)).collidepoint(pos)

class spriteSobrevivente(sprite.Sprite):

    def __init__(self, screen, (x,y), imgSobrevivente, (w,h)):
        sprite.Sprite.__init__(self)
        self.imgSobrevivente = image.load(imgSobrevivente).convert_alpha()
        self.imgSobrevivente = transform.scale(self.imgSobrevivente, (w,h))
        self.posSobrevivente = (x,y)

    def show(self, screen):
        screen.blit(self.imgSobrevivente, self.posSobrevivente)

    def collide(self, pos):
        return self.imgSobrevivente.get_rect(topleft=(self.posSobrevivente)).collidepoint(pos)

class spriteEquip(sprite.Sprite):

    def __init__(self, screen, (x,y), imgCard, scale):
        sprite.Sprite.__init__(self)
        self.imgEquip = image.load(imgCard).convert_alpha()
        self.posEquip = (x,y)
        proporcao = 200/scale
        self.background = (x-5,y-5, int(150/proporcao)+10, int(200/proporcao)+10)
        self.imgEquip = transform.scale(self.imgEquip, (int(150/proporcao), int(200/proporcao)))

    def show(self, screen):
        draw.rect(screen, (0,0,0), self.background)
        screen.blit(self.imgEquip, self.posEquip)

    def collide(self, pos):
        return self.imgEquip.get_rect(topleft=(self.posEquip)).collidepoint(pos)
