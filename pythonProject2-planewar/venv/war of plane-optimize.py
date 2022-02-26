import pygame #引用第三方模块
from pygame.locals import *
import random
class BasePlane(object):
    def __init__(self,screen,imagePath):
        self.screen=screen
        self.image=pygame,image.load(imagePath)
        self.bulletList=[]
        pass
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        # 完善子弹的展示逻辑
        needDelItemList = []
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                # 重新遍历
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
            self.x+=13
            self.y-=20
            self.imagePath='./feiji/bullet.png'
        elif self.type=='enemy':
            self.x = x
            self.y+= 10
            self.imagePath = './feiji/bullet.png'
    def move(self):
        if self.type=='hero':
            self.y-=2
        elif self.type=='enemy':
            self.y+=2
    def display(self):
        self.sceen.blit(self.image,(self.x,self.y))
        pass
    def judge(self):
        if self.y>500 or self.y<0:
            return True
        else:
            return False
class HeroPlane(BasePlane):
    def __init__(self,screen): #主窗体对象
       super.__init__(screen,'./feiji/me.png')
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
 # 发射子弹
    def shootBullet(self):
        newBullet=CommonBullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)
class EnemyPlane(BasePlane):
    def __init__(self,screen):
        self.direction='right'
        self.x = 0
        self.y = 0  # 飞机的默认位置
        super().__init__(screen,'./feiji/enemy.png')
        pass
    def shootBullet(self):
        num=random.randint(1,100)
        if num==3:
            newBullet=CommonBullet(self.x,self.y,self.screen)
            self.bulletList.append(newBullet)
    def move(self):
        if self.direction=='right':
            self.x+=0.5
            pass
        elif self.direction=='left':
            self.x-=0.001
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
            if event.type == K_a or event.key == K_LEFT:
                print('left')
                HeroObj.moveLeft()
            elif event.type == K_d or event.key == K_RIGHT:
                print('right')
                HeroObj.moveRight()
            elif event.key == K_SPACE:
                print('K_SPACE')
                HeroObj.shootBullet()
def main():
    ''',
    搭建界面,获取键盘，添加背景音乐
    :return:
    '''
    # 创建窗口对象
    screen=pygame.display.set_mode((350,500))
    # 创建背景图片对象
    background=pygame.image.load('./feiji/background.png')
    # 设置标题
    pygame.display.set_caption('飞机大战')
    # 添加背景音乐
    # pygame.mixer.init()
    # pygame.mixer.music.load()
    # pygame.mixer.music.set_volume(0,2)
    # pygame.mixer.music.play(-1) #无限循环音乐
    # 载入玩家图片
    hero=HeroPlane(screen)
    enemyPlane=EnemyPlane(screen)
    # # 初始化玩家位置
    # x,y=150,380
    while True:
        # 设定显示内容
        screen.blit(background,(0,0)) #存放在正中
        # 显示玩家飞机图片
        hero.display()
        enemyPlane.display()
        enemyPlane.move()
        enemyPlane.shootBullet()
        #获取键盘事件
        key_control(hero)
        # 更新显示内容
        pygame.display.update()
    pass
if __name__=='__main__':
    main()