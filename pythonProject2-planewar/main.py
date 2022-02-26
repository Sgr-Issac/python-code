import pygame #引用第三方模块
from pygame.locals import *
import random
class BasePlane(object):
    def __init__(self,screen,imagePath):
        self.screen=screen
        self.image=pygame.image.load(imagePath)
        self.bulletList=[]
        pass
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        needDelItemList = []
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
        for i in needDelItemList:
            self.bulletList.remove(i)
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
class CommonBullet(object):
    def __init__(self,x,y,screen,bulletType):
        self.type=bulletType
        self.screen=screen
        if self.type=='hero':
            self.x=x+40
            self.y=y-20
            self.imagePath='./feiji/bullet.png'
            self.image = pygame.image.load(self.imagePath)
        elif self.type=='enemy':
            self.x = x
            self.y=y+10
            self.imagePath = './feiji/bullet.png'
            self.image=pygame.image.load(self.imagePath)
    def move(self):
        if self.type=='hero':
            self.y-=2
        elif self.type=='enemy':
            self.y+=2
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def judge(self):
        if self.y>500 or self.y<0:
            return True
        else:
            return False
class HeroPlane(BasePlane):
    def __init__(self,screen): #主窗体对象
       super().__init__(screen,'./feiji/me.png')
       self.x=150
       self.y=450 #飞机的默认位置
       pass
    def moveLeft(self):#左移动
        if self.x>0:
            self.x-=10
        pass
    def moveRight(self):#右移动
        if self.x<280:
            self.x+=10
        pass
    def shootBullet(self):
        newBullet=CommonBullet(self.x,self.y,self.screen,'hero')
        self.bulletList.append(newBullet)
class EnemyPlane(BasePlane):
    def __init__(self,screen):
        super().__init__(screen, './feiji/enemy.png')
        self.direction='right'
        self.x = 0
        self.y = 0  # 飞机的默认位置
        pass
    def shootBullet(self):
        num=random.randint(1,100)
        if num==3:
            newBullet=CommonBullet(self.x,self.y,self.screen,'enemy')
            self.bulletList.append(newBullet)
    def move(self):
        if self.direction=='right':
            self.x+=0.5
            pass
        elif self.direction=='left':
            self.x-=0.5
        if self.x>350-30:
            self.direction='left'
        elif self.x<0:
            self.direction='right'
def key_control(HeroObj):
    '''
    键盘检测
    :param HeroObj:
    :return:
    '''
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('退出')
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                HeroObj.moveLeft()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                HeroObj.moveRight()
            elif event.key == K_SPACE:
                print('K_SPACE')
                HeroObj.shootBullet()
def main():
    screen=pygame.display.set_mode((350,500))
    background=pygame.image.load('./feiji/background.png')
    pygame.display.set_caption('飞机大战')
    hero=HeroPlane(screen)
    enemyPlane=EnemyPlane(screen)
    while True:
        screen.blit(background,(0,0)) #存放在正中
        hero.display()
        enemyPlane.display()
        enemyPlane.move()
        enemyPlane.shootBullet()
        key_control(hero)
        pygame.display.update()
    pass
if __name__=='__main__':
    main()
