import pygame
from pygame.locals import *
import random
screen=pygame.display.set_mode(300,500)
background=pygame.image.load('./feiji/background.png')
pygame.display.set_caption('war of plane')
class commonPlane(object):
    def __init__(self,screen,imagePath):
        self.screen=screen
        self.image=pygame.image.load(imagePath)
    def display(self):
        self.screen.blit(self.image,(self.x,self.y)

class commonBullet(object):
    def __init__(self,x,y,screen):
        self.screen=screen
        super().__init__()
    pass
class heroPlane(commonPlane):
    pass
class enemyPlane(commonPlane):
    pass




