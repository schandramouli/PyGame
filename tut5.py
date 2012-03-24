import pygame
import random

screen=pygame.display.set_mode((640,480))
flag=1
clock=pygame.time.Clock()
while flag:
 x=random.randint(0,639)
 y=random.randint(0,479)
 r=random.randint(0,255)
 b=random.randint(0,255)
 g=random.randint(0,255)
 screen.set_at((x,y),(r,g,b))
 
 for e in pygame.event.get():
  if e.type==pygame.QUIT:
   flag=0
 
 pygame.display.flip()
 clock.tick(240)


