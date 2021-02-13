import pygame

one=pygame.Rect(-10,400,58,68)
two=pygame.Rect(100,400,58,68)
baz1=pygame.Rect(5,4,100,40)
baz2=pygame.Rect(850,630,100,40)
grad1=0
grad2=180
hp1=3
hp2=3
pula=6
pularect=None
def granici(tank):
    if tank.left <=0:
        tank.x=0
    if tank.right >= 1000:
        tank.right = 1000
    if tank.top <= 0:
        tank.y = 0
    if tank.bottom >= 700:
        tank.bottom = 700

def up_down_tank(move,tank):
    tank.y += move
    tank.width = 58
    tank.height = 68
    granici(tank)
def left_right_tank(move,tank):
    tank.x += move
    tank.width = 68
    tank.height = 58
    granici(tank)

def vestrel():
    global pularect
    if grad1 == 90:
        pularect=pygame.Rect(one.left-30, one.centery-10, 30, 20)
    if grad1==-90:
        pularect = pygame.Rect(one.right, one.centery - 10, 30, 20)
    if grad1==0:
        pularect= pygame.Rect(0 , 0, 20, 30)
        pularect.bottom = one.top
        pularect.centerx= one.centerx
    if grad1==180:
        pularect = pygame.Rect(0, 0, 20, 30)
        pularect.top = one.bottom
        pularect.centerx = one.centerx

