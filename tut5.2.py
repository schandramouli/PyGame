import pygame
import random
screen=pygame.display.set_mode((640,480))
flag=1
clock=pygame.time.Clock()
dx=0
dy=0
x=320
y=240
while flag:
 x+=dx
 y+=dy
 if x<0 or y<0 or x>640 or y>480:
  print "Crash"
  flag=0
 screen.fill((0,0,0))
 screen.set_at((x,y),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

 for e in pygame.event.get():
  if e.type==pygame.QUIT:
   flag=0
  elif e.type==pygame.KEYDOWN:
   if e.key==pygame.K_UP:
    dx=0
    dy=-1
   elif e.key==pygame.K_DOWN:
    dx=0
    dy=1
   elif e.key==pygame.K_LEFT:
    dx=-1
    dy=0
   elif e.key==pygame.K_RIGHT:
    dx=1
    dy=0
 pygame.display.flip()
 clock.tick(120)
